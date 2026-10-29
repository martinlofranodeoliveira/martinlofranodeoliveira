#!/usr/bin/env python3
"""Generate original LOFRANO profile SVGs from GitHub's public GraphQL data.

Python 3.11+; standard library only. Use the repository's automatic GITHUB_TOKEN.
No repository names, issue titles, commit messages, or credentials are requested
or written. The calendar follows GitHub's visible contribution counts, which
may include anonymous private counts when the user has made those public.
Languages include only owned, public, non-fork repositories, measured in bytes.

Both API reads and both renders must succeed before any destination is touched.
Each SVG is staged in its destination directory and atomically replaced. A
failed query never becomes a zero-valued card or an error image.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Callable, Mapping
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo


GRAPHQL_URL = "https://api.github.com/graphql"
SAO_PAULO = ZoneInfo("America/Sao_Paulo")
DEFAULT_USERNAME = "martinlofranodeoliveira"
LEVELS = {
    "NONE": "#171E2D",
    "FIRST_QUARTILE": "#54223F",
    "SECOND_QUARTILE": "#91315E",
    "THIRD_QUARTILE": "#D84D91",
    "FOURTH_QUARTILE": "#FF95CA",
}
MONTHS = ("", "JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ")
FALLBACK_COLORS = ("#F06AA6", "#79B8FF", "#C4A7E7", "#72D6BD", "#FFD580", "#A7B8D5", "#F5A5A5", "#5F6D85")

ACTIVITY_QUERY = """
query ProfileActivity($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    login
    contributionsCollection(from: $from, to: $to) {
      startedAt endedAt
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalPullRequestReviewContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date contributionCount contributionLevel color weekday
          }
        }
      }
    }
  }
}
"""

REPOSITORIES_QUERY = """
query ProfileLanguages($login: String!, $after: String) {
  user(login: $login) {
    login
    publicRepos: repositories(privacy: PUBLIC, ownerAffiliations: [OWNER]) {
      totalCount
    }
    repositories(first: 100, after: $after, privacy: PUBLIC, isFork: false,
                 ownerAffiliations: [OWNER], orderBy: {field: NAME, direction: ASC}) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        id isPrivate isFork
        owner { login }
        languages(first: 100, orderBy: {field: SIZE, direction: DESC}) {
          totalCount totalSize
          pageInfo { hasNextPage endCursor }
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

LANGUAGES_QUERY = """
query MoreRepositoryLanguages($id: ID!, $after: String!) {
  node(id: $id) {
    ... on Repository {
      id isPrivate isFork
      owner { login }
      languages(first: 100, after: $after, orderBy: {field: SIZE, direction: DESC}) {
        totalCount totalSize
        pageInfo { hasNextPage endCursor }
        edges { size node { name color } }
      }
    }
  }
}
"""


class MetricsError(RuntimeError):
    """A sanitized error safe to print in a public Actions log."""


@dataclass(frozen=True)
class ContributionDay:
    date: date
    count: int
    weekday: int
    level: str


@dataclass(frozen=True)
class Activity:
    login: str
    start: datetime
    end: datetime
    collected_at: datetime
    total: int
    commits: int
    pull_requests: int
    issues: int
    reviews: int
    restricted: int
    weeks: tuple[tuple[ContributionDay, ...], ...]


@dataclass(frozen=True)
class Language:
    name: str
    size: int
    color: str


@dataclass(frozen=True)
class RepositoryLanguages:
    public_count: int
    nonfork_count: int
    languages: tuple[Language, ...]


def require(condition: bool, message: str = "Resposta incompleta ou inconsistente do GitHub.") -> None:
    if not condition:
        raise MetricsError(message)


def nonnegative_int(value: object) -> int:
    require(type(value) is int and value >= 0)
    return value


def object_value(value: object) -> dict:
    require(isinstance(value, dict))
    return value


def array_value(value: object) -> list:
    require(isinstance(value, list))
    return value


def timestamp(value: object) -> datetime:
    require(isinstance(value, str))
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        raise MetricsError("Data inválida na resposta do GitHub.") from None
    require(parsed.tzinfo is not None)
    return parsed


def xml_text(value: object) -> str:
    # XML 1.0 does not permit most ASCII controls, even when HTML-escaped.
    clean = "".join(ch for ch in str(value) if ch in "\t\n\r" or
                    0x20 <= ord(ch) <= 0xD7FF or 0xE000 <= ord(ch) <= 0xFFFD or
                    0x10000 <= ord(ch) <= 0x10FFFF)
    return escape(clean, quote=True)


def validate_graphql_payload(payload: object) -> dict:
    data = object_value(payload)
    require(not data.get("errors"), "GitHub retornou erro GraphQL; imagens anteriores preservadas.")
    return object_value(data.get("data"))


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Never forward Authorization to another origin.
        return None


def graphql(query: str, variables: dict, token: str) -> dict:
    request = Request(
        GRAPHQL_URL,
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "Accept": "application/vnd.github+json", "User-Agent": "lofrano-profile-metrics/1"},
        method="POST",
    )
    try:
        with build_opener(NoRedirect()).open(request, timeout=30) as response:
            raw = response.read(12_000_001)
        require(len(raw) <= 12_000_000, "Resposta do GitHub excedeu o limite esperado.")
        return validate_graphql_payload(json.loads(raw))
    except HTTPError as exc:
        raise MetricsError(f"Consulta GitHub falhou (HTTP {exc.code}); imagens anteriores preservadas.") from None
    except (URLError, TimeoutError, OSError, json.JSONDecodeError, UnicodeDecodeError):
        raise MetricsError("Consulta GitHub indisponível; imagens anteriores preservadas.") from None


Fetcher = Callable[[str, dict, str], dict]


def parse_activity(data: dict, username: str, collected_at: datetime) -> Activity:
    user = object_value(object_value(data).get("user"))
    require(isinstance(user.get("login"), str) and user["login"].casefold() == username.casefold())
    collection = object_value(user.get("contributionsCollection"))
    calendar = object_value(collection.get("contributionCalendar"))
    total = nonnegative_int(calendar.get("totalContributions"))
    start, end = timestamp(collection.get("startedAt")), timestamp(collection.get("endedAt"))
    require(start <= end and end - start <= timedelta(days=367))
    raw_weeks = array_value(calendar.get("weeks"))
    require(len(raw_weeks) <= 54)
    weeks, seen_dates = [], set()
    previous_date = None
    for raw_week in raw_weeks:
        raw_days = array_value(object_value(raw_week).get("contributionDays"))
        require(1 <= len(raw_days) <= 7)
        days = []
        for raw_day in raw_days:
            day = object_value(raw_day)
            require(isinstance(day.get("date"), str))
            try:
                day_date = date.fromisoformat(day["date"])
            except ValueError:
                raise MetricsError("Data inválida no calendário do GitHub.") from None
            count = nonnegative_int(day.get("contributionCount"))
            weekday = nonnegative_int(day.get("weekday"))
            level = day.get("contributionLevel")
            require(weekday <= 6 and weekday == day_date.isoweekday() % 7)
            require(isinstance(level, str) and level in LEVELS and (count == 0) == (level == "NONE"))
            require(day_date not in seen_dates and (previous_date is None or day_date > previous_date))
            require(start.date() - timedelta(days=1) <= day_date <= end.date() + timedelta(days=1))
            if days:
                require(weekday > days[-1].weekday)
            seen_dates.add(day_date)
            previous_date = day_date
            days.append(ContributionDay(day_date, count, weekday, level))
        weeks.append(tuple(days))
    require(sum(day.count for week in weeks for day in week) == total,
            "Calendário e total de contribuições divergem; imagens anteriores preservadas.")
    commits = nonnegative_int(collection.get("totalCommitContributions"))
    pull_requests = nonnegative_int(collection.get("totalPullRequestContributions"))
    issues = nonnegative_int(collection.get("totalIssueContributions"))
    reviews = nonnegative_int(collection.get("totalPullRequestReviewContributions"))
    restricted = nonnegative_int(collection.get("restrictedContributionsCount"))
    require(restricted <= total)
    return Activity(user["login"], start, end, collected_at, total, commits,
                    pull_requests, issues, reviews, restricted, tuple(weeks))


def next_cursor(connection: dict) -> str | None:
    page = object_value(connection.get("pageInfo"))
    require(type(page.get("hasNextPage")) is bool)
    if not page["hasNextPage"]:
        return None
    cursor = page.get("endCursor")
    require(isinstance(cursor, str) and bool(cursor))
    return cursor


def assert_public_owned_repository(repository: dict, username: str) -> None:
    require(repository.get("isPrivate") is False and repository.get("isFork") is False,
            "Consulta retornou repositório fora do escopo público; publicação cancelada.")
    owner = object_value(repository.get("owner"))
    require(isinstance(owner.get("login"), str) and owner["login"].casefold() == username.casefold())
    require(isinstance(repository.get("id"), str) and bool(repository["id"]))


def repository_languages(repository: dict, username: str, token: str, fetcher: Fetcher) -> tuple[Language, ...]:
    assert_public_owned_repository(repository, username)
    connection = object_value(repository.get("languages"))
    expected_size = nonnegative_int(connection.get("totalSize"))
    expected_count = nonnegative_int(connection.get("totalCount"))
    result, seen_names, seen_cursors = [], set(), set()
    for _ in range(20):
        require(nonnegative_int(connection.get("totalSize")) == expected_size)
        require(nonnegative_int(connection.get("totalCount")) == expected_count)
        for edge in array_value(connection.get("edges")):
            edge = object_value(edge)
            node = object_value(edge.get("node"))
            name = node.get("name")
            require(isinstance(name, str) and 0 < len(name) <= 1000 and name not in seen_names)
            size = nonnegative_int(edge.get("size"))
            color = node.get("color")
            require(color is None or isinstance(color, str))
            if color is None or not re.fullmatch(r"#[0-9A-Fa-f]{6}", color):
                color = "#A7B8D5"
            result.append(Language(name, size, color))
            seen_names.add(name)
        cursor = next_cursor(connection)
        if cursor is None:
            require(len(result) == expected_count and sum(item.size for item in result) == expected_size,
                    "Distribuição de linguagens incompleta; imagens anteriores preservadas.")
            return tuple(result)
        require(cursor not in seen_cursors)
        seen_cursors.add(cursor)
        node = object_value(fetcher(LANGUAGES_QUERY, {"id": repository["id"], "after": cursor}, token).get("node"))
        assert_public_owned_repository(node, username)
        require(node["id"] == repository["id"])
        connection = object_value(node.get("languages"))
    raise MetricsError("Paginação de linguagens excedeu o limite; imagens anteriores preservadas.")


def fetch_languages(username: str, token: str, fetcher: Fetcher = graphql) -> RepositoryLanguages:
    sizes, colors = defaultdict(int), {}
    cursor, public_count, nonfork_count = None, None, None
    seen_repositories, seen_cursors = set(), set()
    for _ in range(100):
        data = fetcher(REPOSITORIES_QUERY, {"login": username, "after": cursor}, token)
        user = object_value(object_value(data).get("user"))
        require(isinstance(user.get("login"), str) and user["login"].casefold() == username.casefold())
        current_public = nonnegative_int(object_value(user.get("publicRepos")).get("totalCount"))
        connection = object_value(user.get("repositories"))
        current_nonfork = nonnegative_int(connection.get("totalCount"))
        require(current_public >= current_nonfork)
        if public_count is None:
            public_count, nonfork_count = current_public, current_nonfork
        require(public_count == current_public and nonfork_count == current_nonfork)
        for repository in array_value(connection.get("nodes")):
            repository = object_value(repository)
            assert_public_owned_repository(repository, username)
            require(repository["id"] not in seen_repositories)
            seen_repositories.add(repository["id"])
            for item in repository_languages(repository, username, token, fetcher):
                sizes[item.name] += item.size
                colors.setdefault(item.name, item.color)
        cursor = next_cursor(connection)
        if cursor is None:
            require(len(seen_repositories) == nonfork_count,
                    "Lista pública de repositórios incompleta; imagens anteriores preservadas.")
            languages = tuple(Language(name, size, colors[name]) for name, size in
                              sorted(sizes.items(), key=lambda item: (-item[1], item[0].casefold())) if size > 0)
            return RepositoryLanguages(public_count, nonfork_count, languages)
        require(cursor not in seen_cursors)
        seen_cursors.add(cursor)
    raise MetricsError("Paginação de repositórios excedeu o limite; imagens anteriores preservadas.")


def integer_label(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def updated_label(collected_at: datetime) -> str:
    return collected_at.astimezone(SAO_PAULO).strftime("%d/%m/%Y · %H:%M BRT")


def svg_start(width: int, height: int, title: str, description: str) -> list[str]:
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
            f'<title id="title">{xml_text(title)}</title><desc id="description">{xml_text(description)}</desc>',
            '<defs><linearGradient id="card-bg" x2="1" y2="1"><stop stop-color="#0C101B"/><stop offset="1" stop-color="#101321"/></linearGradient></defs>',
            f'<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="22" fill="url(#card-bg)" stroke="#293044"/>',
            '<g font-family="Arial, Helvetica, sans-serif">']


def text_element(x: float, y: float, text: object, size: int = 14,
                 color: str = "#B7C1D6", weight: int = 400, anchor: str = "start") -> str:
    return (f'<text x="{x:g}" y="{y:g}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" fill="{color}">{xml_text(text)}</text>')


def active_days_and_longest_streak(activity: Activity) -> tuple[int, int]:
    """Count active dates and the longest uninterrupted sequence in this period."""
    active_days = longest = current = 0
    previous_date = None
    for week in activity.weeks:
        for day in week:
            if day.count > 0:
                active_days += 1
                current = current + 1 if previous_date is not None and day.date == previous_date + timedelta(days=1) else 1
                longest = max(longest, current)
            else:
                current = 0
            previous_date = day.date
    return active_days, longest


def render_metrics(activity: Activity, public_repository_count: int) -> str:
    public_repository_count = nonnegative_int(public_repository_count)
    active_days, longest = active_days_and_longest_streak(activity)
    period = f'{activity.start.astimezone(SAO_PAULO):%d/%m/%Y} a {activity.end.astimezone(SAO_PAULO):%d/%m/%Y}'
    parts = svg_start(1200, 420, "Atividade de Martin Lofrano no GitHub",
                      f"{activity.total} contribuições visíveis no período de {period}; {active_days} dias ativos e maior sequência de {longest} dias nesse período. {public_repository_count} repositórios públicos.")
    parts += [text_element(32, 42, "ATIVIDADE NO GITHUB", 22, "#F3F5FA", 700),
              text_element(32, 67, f"{activity.login} · Período consultado: {period}", 14),
              text_element(1168, 42, "LOFRANO / ENGINEERING", 13, "#F38AB7", 700, "end")]
    counters = [("CONTRIBUIÇÕES", integer_label(activity.total)), ("DIAS ATIVOS", integer_label(active_days)),
                ("MAIOR SEQUÊNCIA", f"{integer_label(longest)} {'dia' if longest == 1 else 'dias'}"),
                ("REPOS PÚBLICOS", integer_label(public_repository_count))]
    for index, (label, value) in enumerate(counters):
        x = 32 + index * 288
        parts += [f'<rect x="{x}" y="88" width="272" height="90" rx="12" fill="#151B29" stroke="#263047"/>',
                  text_element(x + 18, 131, value, 34, "#FF91C3" if index == 0 else "#F1F5FB", 700),
                  text_element(x + 18, 157, label, 12, "#9EACC4", 700)]
    parts.append('<path d="M32 194H1168" stroke="#263047"/>')
    if activity.weeks:
        pitch = min(19.5, 1034 / max(len(activity.weeks), 1))
        cell = min(15.5, pitch - 3)
        month_starts = []
        previous_month = None
        for column, week in enumerate(activity.weeks):
            month = week[0].date.month
            if month != previous_month:
                month_starts.append((column, month))
                previous_month = month
        # A short leading/trailing partial month should not collide with the
        # neighboring month's label when the card is reduced inside a README.
        if len(month_starts) > 1 and month_starts[1][0] - month_starts[0][0] < 3:
            month_starts.pop(0)
        if len(month_starts) > 1 and len(activity.weeks) - month_starts[-1][0] < 2:
            month_starts.pop()
        for column, month in month_starts:
            parts.append(text_element(100 + column * pitch, 216, MONTHS[month], 11, "#8D9BB4", 700))
        for column, week in enumerate(activity.weeks):
            x = 100 + column * pitch
            for day in week:
                y = 230 + day.weekday * 19
                caption = f"{day.date:%d/%m/%Y}: {integer_label(day.count)} contribuições"
                parts.append(f'<rect x="{x:.2f}" y="{y}" width="{cell:.2f}" height="15.5" rx="3" fill="{LEVELS[day.level]}"><title>{xml_text(caption)}</title></rect>')
        for weekday, label in ((1, "SEG"), (3, "QUA"), (5, "SEX")):
            parts.append(text_element(56, 242 + weekday * 19, label, 10, "#7D8BA3", 500, "end"))
    else:
        parts.append(text_element(600, 286, "Sem contribuições no período consultado.", 18, "#AAB6CB", 400, "middle"))
    parts.append(text_element(32, 395, f"Calendário visível no perfil; repositórios públicos · Atualizado {updated_label(activity.collected_at)}", 12, "#8391A9"))
    parts.append(text_element(983, 395, "MENOS", 9, "#8391A9", 700, "end"))
    for index, color in enumerate(LEVELS.values()):
        parts.append(f'<rect x="{992 + index * 20}" y="383" width="14" height="14" rx="3" fill="{color}"/>')
    parts.append(text_element(1101, 395, "MAIS", 9, "#8391A9", 700))
    parts += ["</g></svg>\n"]
    return "\n".join(parts)


def language_segments(languages: tuple[Language, ...], limit: int = 8) -> list[tuple[Language, int]]:
    """Return chart entries and tenths of a percent; displayed values sum to 100%."""
    require(limit >= 2)
    nonempty = sorted((item for item in languages if item.size > 0), key=lambda item: (-item.size, item.name.casefold()))
    if not nonempty:
        return []
    if len(nonempty) > limit:
        nonempty = nonempty[:limit - 1] + [Language("Outras", sum(item.size for item in nonempty[limit - 1:]), "#5F6D85")]
    total = sum(item.size for item in nonempty)
    tenths = [item.size * 1000 // total for item in nonempty]
    remainder_order = sorted(range(len(nonempty)), key=lambda i: (-(nonempty[i].size * 1000 % total), i))
    for index in remainder_order[:1000 - sum(tenths)]:
        tenths[index] += 1
    return list(zip(nonempty, tenths))


def render_languages(summary: RepositoryLanguages, collected_at: datetime) -> str:
    total = sum(language.size for language in summary.languages)
    parts = svg_start(1200, 270, "Linguagens dos repositórios públicos",
                      f"Distribuição de {total} bytes de código em {summary.nonfork_count} repositórios próprios, públicos e não forks. {summary.public_count} repositórios públicos no total.")
    parts += [text_element(32, 42, "LINGUAGENS / CÓDIGO PÚBLICO", 22, "#F3F5FA", 700),
              text_element(32, 67, "Distribuição por bytes · Repositórios próprios, sem forks", 14),
              text_element(1168, 42, f"{integer_label(summary.public_count)} REPOSITÓRIOS PÚBLICOS", 14, "#F38AB7", 700, "end"),
              text_element(1168, 66, f"{integer_label(summary.nonfork_count)} considerados nesta distribuição", 12, "#8391A9", 400, "end")]
    segments = language_segments(summary.languages)
    parts.append('<defs><clipPath id="language-bar"><rect x="32" y="92" width="1136" height="18" rx="9"/></clipPath></defs>')
    parts.append('<rect x="32" y="92" width="1136" height="18" rx="9" fill="#1A2232"/>')
    offset = 32.0
    for index, (language, tenths) in enumerate(segments):
        width = language.size / total * 1136
        color = language.color if re.fullmatch(r"#[0-9A-Fa-f]{6}", language.color) else FALLBACK_COLORS[index]
        parts.append(f'<rect x="{offset:.6f}" y="92" width="{width:.6f}" height="18" fill="{color}" clip-path="url(#language-bar)"/>')
        offset += width
        x, y = 32 + index % 4 * 286, 146 + index // 4 * 48
        visible_name = language.name if len(language.name) <= 21 else language.name[:20] + "…"
        parts += [f'<circle cx="{x + 6}" cy="{y - 5}" r="5" fill="{color}"/>',
                  text_element(x + 22, y, visible_name, 15, "#DCE3F1", 600),
                  text_element(x + 265, y, f"{tenths / 10:.1f}%".replace(".", ","), 15, "#F3A2C6", 600, "end"),
                  text_element(x + 22, y + 18, f"{integer_label(language.size)} bytes", 11, "#7E8DA6")]
    if not segments:
        parts.append(text_element(600, 168, "Ainda não há bytes de linguagens classificados pelo GitHub.", 18, "#AAB6CB", 400, "middle"))
    parts += [text_element(32, 246, f"Fonte: GitHub Languages · Atualizado {updated_label(collected_at)}", 12, "#8391A9"),
              text_element(1168, 246, "LOFRANO TECNOLOGIA", 12, "#8391A9", 700, "end"), "</g></svg>\n"]
    return "\n".join(parts)


def atomic_write_svgs(output_directory: Path, documents: Mapping[str, str]) -> None:
    """Stage and validate all SVGs before atomically replacing each destination."""
    for name, content in documents.items():
        require(Path(name).name == name and name.endswith(".svg"), "Nome de imagem inválido.")
        try:
            root = ET.fromstring(content)
            require(root.tag == "{http://www.w3.org/2000/svg}svg", "SVG inválido.")
        except ET.ParseError:
            raise MetricsError("SVG inválido; imagens anteriores preservadas.") from None
    output_directory.mkdir(parents=True, exist_ok=True)
    staged = []
    try:
        for name, content in documents.items():
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=output_directory,
                                             prefix=f".{name}.", suffix=".tmp", delete=False) as temporary:
                staged.append((Path(temporary.name), output_directory / name))
                temporary.write(content)
                temporary.flush()
                os.fsync(temporary.fileno())
        for temporary, destination in staged:
            os.replace(temporary, destination)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)


def update_profile(username: str, output_directory: Path, token: str,
                   now: datetime | None = None, fetcher: Fetcher = graphql) -> None:
    require(bool(re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})", username)), "Usuário GitHub inválido.")
    require(isinstance(token, str) and bool(token.strip()), "GITHUB_TOKEN ausente; imagens anteriores preservadas.")
    now = now or datetime.now(timezone.utc)
    require(now.tzinfo is not None, "A data de coleta precisa incluir fuso horário.")
    local_today = now.astimezone(SAO_PAULO).date()
    beginning = datetime.combine(local_today - timedelta(days=364), time.min, SAO_PAULO)
    data = fetcher(ACTIVITY_QUERY, {"login": username, "from": beginning.isoformat(), "to": now.isoformat()}, token)
    activity = parse_activity(data, username, now)
    languages = fetch_languages(username, token, fetcher)
    documents = {"github-metrics.svg": render_metrics(activity, languages.public_count),
                 "github-languages.svg": render_languages(languages, now)}
    atomic_write_svgs(output_directory, documents)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default=os.environ.get("GITHUB_PROFILE_LOGIN", DEFAULT_USERNAME))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1] / "assets")
    arguments = parser.parse_args()
    try:
        update_profile(arguments.username, arguments.output_dir, os.environ.get("GITHUB_TOKEN", ""))
    except MetricsError as exc:
        print(f"profile-metrics: {exc}", file=sys.stderr)
        return 1
    except OSError:
        print("profile-metrics: falha ao gravar imagens; atualização não concluída.", file=sys.stderr)
        return 1
    print("profile-metrics: os dois SVGs foram atualizados com dados do GitHub.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
