"""Offline regression tests for public data validation and SVG publication."""

import copy
from datetime import date, datetime, timezone
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "update_profile_metrics.py"
SPEC = importlib.util.spec_from_file_location("profile_metrics", MODULE_PATH)
metrics = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = metrics
SPEC.loader.exec_module(metrics)

NOW = datetime(2026, 10, 29, 1, 45, tzinfo=timezone.utc)
LOGIN = "martinlofranodeoliveira"


def activity_response(counts=(2, 0, 3)):
    days = []
    for index, count in enumerate(counts):
        days.append({"date": f"2026-10-{26 + index:02d}", "weekday": index + 1,
                     "contributionCount": count, "color": "#000000",
                     "contributionLevel": "FOURTH_QUARTILE" if count else "NONE"})
    return {"user": {"login": LOGIN, "contributionsCollection": {
        "startedAt": "2026-10-26T03:00:00Z", "endedAt": NOW.isoformat(),
        "totalCommitContributions": sum(counts), "totalPullRequestContributions": 0,
        "totalIssueContributions": 0, "totalPullRequestReviewContributions": 0,
        "restrictedContributionsCount": 0,
        "contributionCalendar": {"totalContributions": sum(counts),
                                 "weeks": [{"contributionDays": days}] if days else []},
    }}}


def language_connection(items, next_page=None, total_size=None, total_count=None):
    return {"totalCount": len(items) if total_count is None else total_count,
            "totalSize": sum(size for _, size in items) if total_size is None else total_size,
            "edges": [{"size": size, "node": {"name": name, "color": "#F06AA6"}} for name, size in items],
            "pageInfo": {"hasNextPage": next_page is not None, "endCursor": next_page}}


def repository(identifier, languages):
    return {"id": identifier, "isPrivate": False, "isFork": False,
            "owner": {"login": LOGIN}, "languages": languages}


def repositories_response(nodes=(), next_page=None, total_count=None, public_count=None):
    total_count = len(nodes) if total_count is None else total_count
    return {"user": {"login": LOGIN,
                     "publicRepos": {"totalCount": total_count if public_count is None else public_count},
                     "repositories": {"totalCount": total_count, "nodes": list(nodes),
                                      "pageInfo": {"hasNextPage": next_page is not None, "endCursor": next_page}}}}


class ActivityValidationTests(unittest.TestCase):
    def test_calendar_sum_and_cells_are_preserved(self):
        activity = metrics.parse_activity(activity_response(), LOGIN, NOW)
        self.assertEqual(activity.total, 5)
        self.assertEqual(sum(day.count for week in activity.weeks for day in week), 5)
        root = ET.fromstring(metrics.render_metrics(activity, 42))
        labels = [node.text for node in root.iter("{http://www.w3.org/2000/svg}title")]
        self.assertIn("26/10/2026: 2 contribuições", labels)
        self.assertIn("27/10/2026: 0 contribuições", labels)

    def test_genuinely_empty_data_is_valid(self):
        activity = metrics.parse_activity(activity_response(()), LOGIN, NOW)
        self.assertEqual(activity.total, 0)
        self.assertIn("Sem contribuições", metrics.render_metrics(activity, 0))
        summary = metrics.fetch_languages(LOGIN, "test", lambda *args: repositories_response())
        self.assertEqual(summary.nonfork_count, 0)
        self.assertIn("Ainda não há bytes", metrics.render_languages(summary, NOW))

    def test_missing_fields_never_become_zeros(self):
        data = activity_response()
        del data["user"]["contributionsCollection"]["totalIssueContributions"]
        with self.assertRaises(metrics.MetricsError):
            metrics.parse_activity(data, LOGIN, NOW)

    def test_wrong_sum_duplicate_date_and_weekday_are_rejected(self):
        for alteration in ("total", "duplicate", "weekday"):
            with self.subTest(alteration=alteration):
                data = activity_response()
                calendar = data["user"]["contributionsCollection"]["contributionCalendar"]
                if alteration == "total":
                    calendar["totalContributions"] += 1
                elif alteration == "duplicate":
                    calendar["weeks"][0]["contributionDays"][1] = copy.deepcopy(calendar["weeks"][0]["contributionDays"][0])
                else:
                    calendar["weeks"][0]["contributionDays"][0]["weekday"] = 4
                with self.assertRaises(metrics.MetricsError):
                    metrics.parse_activity(data, LOGIN, NOW)

    def test_negative_and_boolean_counts_are_rejected(self):
        for invalid in (-1, True, None, "5"):
            with self.subTest(invalid=invalid):
                data = activity_response()
                data["user"]["contributionsCollection"]["totalCommitContributions"] = invalid
                with self.assertRaises(metrics.MetricsError):
                    metrics.parse_activity(data, LOGIN, NOW)

    def test_sao_paulo_date_does_not_use_utc_day(self):
        self.assertEqual(metrics.updated_label(NOW), "28/10/2026 · 22:45 BRT")

    def test_streak_crosses_weeks_and_resets_on_zero_days_and_gaps(self):
        cases = [
            ([('2026-10-23', 1), ('2026-10-24', 1), ('2026-10-25', 1),
              ('2026-10-26', 1), ('2026-10-27', 1), ('2026-10-28', 0),
              ('2026-10-29', 1)], (6, 5)),
            ([('2026-10-29', 1), ('2026-10-31', 1), ('2026-11-01', 1)], (3, 2)),
        ]
        for dates, expected in cases:
            with self.subTest(dates=dates):
                weeks, days = [], []
                for iso_date, count in dates:
                    current = date.fromisoformat(iso_date)
                    weekday = current.isoweekday() % 7
                    if days and weekday <= days[-1]["weekday"]:
                        weeks.append({"contributionDays": days})
                        days = []
                    days.append({"date": iso_date, "weekday": weekday, "contributionCount": count,
                                 "contributionLevel": "FIRST_QUARTILE" if count else "NONE"})
                weeks.append({"contributionDays": days})
                data = activity_response()
                collection = data["user"]["contributionsCollection"]
                collection["startedAt"] = "2026-10-23T03:00:00Z"
                collection["endedAt"] = "2026-11-02T03:00:00Z"
                collection["contributionCalendar"] = {"totalContributions": sum(count for _, count in dates), "weeks": weeks}
                activity = metrics.parse_activity(data, LOGIN, NOW)
                self.assertEqual(metrics.active_days_and_longest_streak(activity), expected)

    def test_metrics_card_uses_consistent_calendar_and_public_repo_counters(self):
        activity = metrics.parse_activity(activity_response(), LOGIN, NOW)
        svg = metrics.render_metrics(activity, 42)
        root = ET.fromstring(svg)
        texts = [node.text for node in root.iter("{http://www.w3.org/2000/svg}text")]
        for expected in ("CONTRIBUIÇÕES", "DIAS ATIVOS", "MAIOR SEQUÊNCIA", "REPOS PÚBLICOS", "42", "1 dia"):
            self.assertIn(expected, texts)
        for removed in ("COMMITS", "PULL REQUESTS", "ISSUES", "REVIEWS"):
            self.assertNotIn(removed, texts)


class LanguageValidationTests(unittest.TestCase):
    def test_repository_and_language_pagination_are_complete(self):
        calls = []
        first_languages = language_connection([("TypeScript", 80)], "lang-next", 100, 2)
        responses = [repositories_response([repository("repo-1", first_languages)], "repo-next", 2, 3),
                     {"node": repository("repo-1", language_connection([("CSS", 20)], None, 100, 2))},
                     repositories_response([repository("repo-2", language_connection([("TypeScript", 50)]))], None, 2, 3)]

        def fetcher(query, variables, token):
            calls.append((query, variables))
            return responses.pop(0)

        summary = metrics.fetch_languages(LOGIN, "test", fetcher)
        self.assertEqual(summary.public_count, 3)
        self.assertEqual(summary.nonfork_count, 2)
        self.assertEqual({item.name: item.size for item in summary.languages}, {"TypeScript": 130, "CSS": 20})
        self.assertEqual(calls[1][1], {"id": "repo-1", "after": "lang-next"})
        self.assertEqual(calls[2][1]["after"], "repo-next")

    def test_private_forks_and_nonowned_repositories_are_rejected(self):
        for field in ("private", "fork", "owner"):
            with self.subTest(field=field):
                repo = repository("repo-1", language_connection([]))
                if field == "owner":
                    repo["owner"]["login"] = "another-user"
                else:
                    repo["isPrivate" if field == "private" else "isFork"] = True
                with self.assertRaises(metrics.MetricsError):
                    metrics.fetch_languages(LOGIN, "test", lambda *args: repositories_response([repo]))

    def test_truncated_bytes_and_repository_count_are_rejected(self):
        incomplete_languages = repository("repo-1", language_connection([("JS", 10)], total_size=20))
        incomplete_repos = repositories_response([], total_count=1)
        for data in (repositories_response([incomplete_languages]), incomplete_repos):
            with self.assertRaises(metrics.MetricsError):
                metrics.fetch_languages(LOGIN, "test", lambda *args: data)

    def test_rounding_and_other_group_preserve_distribution(self):
        items = tuple(metrics.Language(f"Lang-{i}", i + 1, "#F06AA6") for i in range(12))
        result = metrics.language_segments(items)
        self.assertEqual(len(result), 8)
        self.assertEqual(sum(item.size for item, _ in result), sum(item.size for item in items))
        self.assertEqual(sum(percentage for _, percentage in result), 1000)
        self.assertEqual(result[-1][0].name, "Outras")

    def test_svg_escapes_language_text_and_ignores_unsafe_color(self):
        unsafe = metrics.Language('<script>&"\x01', 100, 'red" onload="alert(1)')
        svg = metrics.render_languages(metrics.RepositoryLanguages(1, 1, (unsafe,)), NOW)
        root = ET.fromstring(svg)
        self.assertFalse(any(node.tag.endswith("script") for node in root.iter()))
        self.assertNotIn("onload", svg)
        texts = [node.text for node in root.iter("{http://www.w3.org/2000/svg}text")]
        self.assertIn('<script>&"', texts)


class FailureAndPublicationTests(unittest.TestCase):
    def test_graphql_partial_data_with_errors_fails_closed(self):
        with self.assertRaises(metrics.MetricsError) as raised:
            metrics.validate_graphql_payload({"data": activity_response(), "errors": [{"message": "SECRET"}]})
        self.assertNotIn("SECRET", str(raised.exception))

    def test_second_query_failure_keeps_both_existing_files(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            names = ("github-metrics.svg", "github-languages.svg")
            for name in names:
                (destination / name).write_text("original-" + name)

            def fetcher(query, variables, token):
                if query == metrics.ACTIVITY_QUERY:
                    return activity_response()
                raise metrics.MetricsError("network unavailable")

            with self.assertRaises(metrics.MetricsError):
                metrics.update_profile(LOGIN, destination, "test", NOW, fetcher)
            for name in names:
                self.assertEqual((destination / name).read_text(), "original-" + name)

    def test_invalid_second_svg_keeps_first_file(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            (destination / "first.svg").write_text("original")
            with self.assertRaises(metrics.MetricsError):
                metrics.atomic_write_svgs(destination, {"first.svg": '<svg xmlns="http://www.w3.org/2000/svg"/>',
                                                        "second.svg": "<invalid"})
            self.assertEqual((destination / "first.svg").read_text(), "original")

    def test_successful_pipeline_publishes_valid_svgs_without_temp_files(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)

            def fetcher(query, variables, token):
                if query == metrics.ACTIVITY_QUERY:
                    self.assertEqual(variables["from"], "2025-10-29T00:00:00-03:00")
                    return activity_response()
                return repositories_response([repository("repo-1", language_connection([("TypeScript", 100)]))])

            metrics.update_profile(LOGIN, destination, "test", NOW, fetcher)
            self.assertEqual(sorted(path.name for path in destination.iterdir()), ["github-languages.svg", "github-metrics.svg"])
            for path in destination.iterdir():
                self.assertEqual(ET.fromstring(path.read_text()).tag, "{http://www.w3.org/2000/svg}svg")


if __name__ == "__main__":
    unittest.main()
