#!/usr/bin/env python3
"""Refresh public repository metadata and the bounded catalogue section.

Python 3.11+, standard library only. Uses GITHUB_TOKEN and
GITHUB_PROFILE_LOGIN, like update_profile_metrics.py. No CI status, quality
verdict, private repository metadata or commit messages are requested.
All pages, counts and generated documents are validated before files change.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html import escape
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import unicodedata
from urllib.parse import quote


# A file-based import also works when this module is loaded by spec_from_file_location
# or invoked directly, without depending on the current working directory.
_METRICS_NAME = "lofrano_profile_metrics_shared"
if _METRICS_NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(
        _METRICS_NAME, Path(__file__).with_name("update_profile_metrics.py"))
    if _spec is None or _spec.loader is None:
        raise RuntimeError("Módulo compartilhado de métricas indisponível.")
    _module = importlib.util.module_from_spec(_spec)
    sys.modules[_METRICS_NAME] = _module
    _spec.loader.exec_module(_module)
metrics = sys.modules[_METRICS_NAME]
CatalogError = metrics.MetricsError
require = metrics.require

BEGIN = "<!-- PUBLIC-PROJECTS:BEGIN -->"
END = "<!-- PUBLIC-PROJECTS:END -->"
MAX_PAGES = 100
LATEST_COUNT = 8

REPOSITORIES_QUERY = """
query PublicProjectCatalog($login: String!, $after: String) {
  user(login: $login) {
    login
    repositories(first: 100, after: $after, privacy: PUBLIC,
                 ownerAffiliations: [OWNER], orderBy: {field: NAME, direction: ASC}) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        name description url createdAt pushedAt isFork isArchived isPrivate
        owner { login }
        defaultBranchRef {
          name
          target { ... on Commit { oid committedDate url } }
        }
      }
    }
  }
}
"""


def validate_login(value: object) -> str:
    require(isinstance(value, str) and
            re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})", value) is not None,
            "Usuário GitHub inválido.")
    return value


def github_url(owner: str, repository: str, oid: str | None = None) -> str:
    url = f"https://github.com/{quote(owner, safe='')}/{quote(repository, safe='')}"
    return f"{url}/commit/{oid}" if oid else url


def validate_repository(raw: object, username: str) -> dict:
    repository = metrics.object_value(raw)
    fields = {"name", "description", "url", "createdAt", "pushedAt", "isFork",
              "isArchived", "isPrivate", "owner", "defaultBranchRef"}
    require(fields <= repository.keys(), "Metadados públicos incompletos; arquivos anteriores preservados.")
    name = repository["name"]
    require(isinstance(name, str) and re.fullmatch(r"[A-Za-z0-9_.-]{1,100}", name) is not None
            and name not in (".", ".."))
    owner = metrics.object_value(repository["owner"])
    login = validate_login(owner.get("login"))
    require(login.casefold() == username.casefold() and repository["isPrivate"] is False,
            "Consulta retornou repositório fora do escopo público próprio.")
    require(type(repository["isFork"]) is bool and type(repository["isArchived"]) is bool)
    description = repository["description"]
    require(description is None or isinstance(description, str) and len(description) <= 2000)
    metrics.timestamp(repository["createdAt"])
    if repository["pushedAt"] is not None:
        metrics.timestamp(repository["pushedAt"])
    canonical = github_url(login, name)
    require(repository["url"] == canonical, "URL pública inesperada; publicação cancelada.")
    branch = repository["defaultBranchRef"]
    if branch is not None:
        branch = metrics.object_value(branch)
        require(isinstance(branch.get("name"), str) and 0 < len(branch["name"]) <= 1024)
        require(not any(unicodedata.category(ch).startswith("C") for ch in branch["name"]))
        target = metrics.object_value(branch.get("target"))
        oid = target.get("oid")
        require(isinstance(oid, str) and re.fullmatch(r"[0-9a-f]{40}", oid) is not None)
        metrics.timestamp(target.get("committedDate"))
        require(target.get("url") == github_url(login, name, oid),
                "URL de commit inesperada; publicação cancelada.")
        branch = {"name": branch["name"], "target": {
            "oid": oid, "committedDate": target["committedDate"], "url": target["url"]}}
    # Keep only the explicitly requested public metadata, even for injected fetchers.
    return {"name": name, "description": description, "url": canonical,
            "createdAt": repository["createdAt"], "pushedAt": repository["pushedAt"],
            "isFork": repository["isFork"], "isArchived": repository["isArchived"],
            "isPrivate": False, "owner": {"login": login}, "defaultBranchRef": branch}


def fetch_inventory(username: str, token: str, now: datetime,
                    fetcher=metrics.graphql) -> dict:
    validate_login(username)
    require(isinstance(token, str) and bool(token.strip()),
            "GITHUB_TOKEN ausente; arquivos anteriores preservados.")
    require(isinstance(now, datetime) and now.tzinfo is not None,
            "A data de coleta precisa incluir fuso horário.")
    repositories, names, cursors = [], set(), set()
    expected_count, canonical_login, cursor = None, None, None
    for _ in range(MAX_PAGES):
        data = metrics.object_value(fetcher(REPOSITORIES_QUERY, {"login": username, "after": cursor}, token))
        # The shared HTTP fetcher rejects GraphQL errors. Reject them here too for
        # custom fetchers; partial data must never become a published inventory.
        require(not data.get("errors"), "Resposta GraphQL parcial; arquivos anteriores preservados.")
        user = metrics.object_value(data.get("user"))
        current_login = validate_login(user.get("login"))
        require(current_login.casefold() == username.casefold())
        connection = metrics.object_value(user.get("repositories"))
        count = metrics.nonnegative_int(connection.get("totalCount"))
        if expected_count is None:
            expected_count, canonical_login = count, current_login
        require(count == expected_count and canonical_login == current_login,
                "Inventário mudou durante a consulta; arquivos anteriores preservados.")
        nodes = metrics.array_value(connection.get("nodes"))
        require(len(nodes) <= 100)
        for raw in nodes:
            repository = validate_repository(raw, current_login)
            name_key = repository["name"].casefold()
            require(name_key not in names, "Repositório repetido na paginação; publicação cancelada.")
            names.add(name_key)
            repositories.append(repository)
        require(len(repositories) <= expected_count)
        page = metrics.object_value(connection.get("pageInfo"))
        require("endCursor" in page and type(page.get("hasNextPage")) is bool)
        end_cursor = page["endCursor"]
        require(end_cursor is None or isinstance(end_cursor, str) and bool(end_cursor))
        if not page["hasNextPage"]:
            require(len(repositories) == expected_count,
                    "Inventário público truncado; arquivos anteriores preservados.")
            return {"collectedAt": now.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
                    "login": canonical_login, "publicRepositoryCount": expected_count,
                    "repositories": sorted(repositories, key=lambda item: (item["name"].casefold(), item["name"]))}
        require(bool(nodes) and len(repositories) < expected_count and
                isinstance(end_cursor, str) and end_cursor not in cursors,
                "Paginação pública incompleta; arquivos anteriores preservados.")
        cursors.add(end_cursor)
        cursor = end_cursor
    raise CatalogError("Paginação pública excedeu o limite; arquivos anteriores preservados.")


def markdown_text(value: str | None, limit: int = 180) -> str:
    clean = "".join(" " if ch.isspace() or unicodedata.category(ch).startswith("C") else ch
                    for ch in (value or ""))
    clean = " ".join(clean.split())
    if len(clean) > limit:
        clean = clean[:limit - 1].rstrip() + "…"
    clean = escape(clean, quote=False)
    return re.sub(r"([\\`*{}\[\]()#+.!_|>~\-])", r"\\\1", clean)


def render_section(inventory: dict) -> str:
    collected = metrics.timestamp(inventory.get("collectedAt"))
    login = validate_login(inventory.get("login"))
    count = metrics.nonnegative_int(inventory.get("publicRepositoryCount"))
    repositories = [validate_repository(item, login)
                    for item in metrics.array_value(inventory.get("repositories"))]
    require(len(repositories) == count and len({item["name"].casefold() for item in repositories}) == count)
    latest = sorted(repositories, key=lambda item: (metrics.timestamp(item["createdAt"]), item["name"].casefold()),
                    reverse=True)[:LATEST_COUNT]
    parts = [BEGIN, "## Repositórios públicos · atualização automática", "",
             f"**{count} repositórios públicos próprios**, incluindo forks e arquivados quando existirem. "
             f"Metadados consultados no GitHub em **{collected.astimezone(timezone.utc).strftime('%d/%m/%Y às %H:%M UTC')}**.", "",
             "Os oito repositórios criados mais recentemente, com o último commit da branch padrão. "
             "As coleções abaixo têm curadoria manual; as validações técnicas estão em "
             "[EVIDENCIAS.md](EVIDENCIAS.md).", "",
             "[Inventário público completo em JSON](evidencias/public-projects.json).", ""]
    if latest:
        parts += ["| Projeto | Descrição pública | Último commit da branch padrão (UTC) |",
                  "| --- | --- | --- |"]
        for repository in latest:
            branch = repository["defaultBranchRef"]
            commit = "Sem commit na branch padrão"
            if branch is not None:
                target = branch["target"]
                date = metrics.timestamp(target["committedDate"]).astimezone(timezone.utc).strftime("%d/%m/%Y %H:%M")
                commit = f"[{date} · {target['oid'][:7]}]({target['url']})"
            description = markdown_text(repository["description"]) or "Sem descrição pública."
            parts.append(f"| [{markdown_text(repository['name'])}]({repository['url']}) | {description} | {commit} |")
    else:
        parts.append("Nenhum repositório público próprio foi retornado nesta coleta completa.")
    parts += ["", END]
    return "\n".join(parts)


def replace_generated_section(catalogue: str, section: str) -> str:
    require(catalogue.count(BEGIN) == 1 and catalogue.count(END) == 1,
            "Marcadores do catálogo ausentes ou duplicados; arquivos anteriores preservados.")
    start, end = catalogue.index(BEGIN), catalogue.index(END)
    require(start < end, "Marcadores do catálogo fora de ordem; arquivos anteriores preservados.")
    return catalogue[:start] + section + catalogue[end + len(END):]


def atomic_write_documents(documents: dict[Path, str]) -> None:
    staged = []
    try:
        for destination, content in documents.items():
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=destination.parent,
                                             prefix=f".{destination.name}.", suffix=".tmp", delete=False) as temporary:
                staged.append((Path(temporary.name), destination))
                temporary.write(content)
                temporary.flush()
                os.fsync(temporary.fileno())
        for temporary, destination in staged:
            os.replace(temporary, destination)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)


def update_catalog(username: str, output_directory: Path, token: str,
                   now: datetime | None = None, fetcher=metrics.graphql) -> dict:
    now = now or datetime.now(timezone.utc)
    inventory = fetch_inventory(username, token, now, fetcher)
    catalogue_path = output_directory / "PROJETOS-ABERTOS.md"
    catalogue = catalogue_path.read_text(encoding="utf-8")
    updated = replace_generated_section(catalogue, render_section(inventory))
    snapshot = json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
    atomic_write_documents({output_directory / "evidencias" / "public-projects.json": snapshot,
                            catalogue_path: updated})
    return inventory


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default=os.environ.get("GITHUB_PROFILE_LOGIN", metrics.DEFAULT_USERNAME))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    try:
        inventory = update_catalog(arguments.username, arguments.output_dir, os.environ.get("GITHUB_TOKEN", ""))
    except CatalogError as exc:
        print(f"project-catalog: {exc}", file=sys.stderr)
        return 1
    except OSError:
        print("project-catalog: falha ao ler ou gravar arquivos; atualização não concluída.", file=sys.stderr)
        return 1
    print(f"project-catalog: {inventory['publicRepositoryCount']} repositórios públicos consultados e catálogo atualizado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
