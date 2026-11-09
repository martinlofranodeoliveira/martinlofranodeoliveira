"""Offline checks for complete public inventory and bounded Markdown publication."""

import copy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "update_project_catalog.py"
SPEC = importlib.util.spec_from_file_location("project_catalog", MODULE_PATH)
catalog = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = catalog
SPEC.loader.exec_module(catalog)

NOW = datetime(2026, 11, 9, 12, 30, tzinfo=timezone.utc)
LOGIN = "martinlofranodeoliveira"
OID = "a" * 40


def repository(name="sample", created="2026-11-09T10:00:00Z", branch=True):
    url = f"https://github.com/{LOGIN}/{name}"
    return {"name": name, "description": "Public example", "url": url,
            "createdAt": created, "pushedAt": "2026-11-09T11:00:00Z",
            "isFork": False, "isArchived": False, "isPrivate": False,
            "owner": {"login": LOGIN},
            "defaultBranchRef": {"name": "main", "target": {
                "oid": OID, "committedDate": "2026-11-09T10:30:00Z", "url": f"{url}/commit/{OID}"}}
            if branch else None}


def response(nodes=(), total=None, next_cursor=None):
    return {"user": {"login": LOGIN, "repositories": {
        "totalCount": len(nodes) if total is None else total, "nodes": list(nodes),
        "pageInfo": {"hasNextPage": next_cursor is not None, "endCursor": next_cursor}}}}


def inventory(nodes=()):
    return catalog.fetch_inventory(LOGIN, "test-token", NOW, lambda *args: response(nodes))


class InventoryTests(unittest.TestCase):
    def test_pagination_includes_forks_and_archived_and_sorts_names(self):
        fork = repository("z-fork")
        fork.update(isFork=True, isArchived=True)
        pages = [response([fork], total=2, next_cursor="next"), response([repository("a-own")], total=2)]
        calls = []

        def fetcher(query, variables, token):
            calls.append((query, variables, token))
            return pages.pop(0)

        actual = catalog.fetch_inventory(LOGIN, "test-token", NOW, fetcher)
        self.assertEqual(actual["publicRepositoryCount"], 2)
        self.assertEqual([item["name"] for item in actual["repositories"]], ["a-own", "z-fork"])
        self.assertTrue(actual["repositories"][1]["isFork"])
        self.assertTrue(actual["repositories"][1]["isArchived"])
        self.assertEqual(calls[0][1], {"login": LOGIN, "after": None})
        self.assertEqual(calls[1][1], {"login": LOGIN, "after": "next"})
        self.assertNotIn("isFork:", calls[0][0])
        self.assertNotIn("isArchived:", calls[0][0])
        self.assertIn("privacy: PUBLIC", calls[0][0])
        self.assertIn("ownerAffiliations: [OWNER]", calls[0][0])

    def test_zero_is_valid_only_for_an_explicit_complete_inventory(self):
        actual = inventory()
        self.assertEqual(actual["publicRepositoryCount"], 0)
        self.assertEqual(actual["repositories"], [])
        section = catalog.render_section(actual)
        self.assertIn("**0 repositórios públicos", section)
        self.assertIn("Nenhum repositório público", section)

    def test_empty_repository_with_no_default_branch_is_valid(self):
        item = repository(branch=False)
        item["pushedAt"] = None
        actual = inventory([item])
        self.assertIsNone(actual["repositories"][0]["defaultBranchRef"])
        self.assertIn("Sem commit na branch padrão", catalog.render_section(actual))

    def test_boolean_negative_missing_and_string_counts_fail(self):
        for bad in (True, -1, None, "1", 1.0):
            with self.subTest(bad=bad):
                data = response([repository()])
                data["user"]["repositories"]["totalCount"] = bad
                with self.assertRaises(catalog.CatalogError):
                    catalog.fetch_inventory(LOGIN, "test-token", NOW, lambda *args: data)

    def test_truncated_and_null_nodes_fail(self):
        cases = [response([], total=1), response([None]), response([repository()], total=0)]
        for data in cases:
            with self.subTest(data=data), self.assertRaises(catalog.CatalogError):
                catalog.fetch_inventory(LOGIN, "test-token", NOW, lambda *args: data)

    def test_missing_metadata_never_becomes_no_branch_or_zero(self):
        for field in repository():
            with self.subTest(field=field):
                item = repository()
                del item[field]
                with self.assertRaises(catalog.CatalogError):
                    inventory([item])
        item = repository()
        item["defaultBranchRef"]["target"] = {}
        with self.assertRaises(catalog.CatalogError):
            inventory([item])

    def test_private_nonowned_and_nonboolean_flags_fail(self):
        for changes in ({"isPrivate": True}, {"owner": {"login": "other"}},
                        {"isFork": 1}, {"isArchived": "false"}):
            item = repository()
            item.update(changes)
            with self.subTest(changes=changes), self.assertRaises(catalog.CatalogError):
                inventory([item])

    def test_duplicate_names_repeated_cursors_and_changed_counts_fail(self):
        scenarios = [
            [response([repository("one")], 2, "next"), response([repository("one")], 2)],
            [response([repository("one")], 3, "next"), response([repository("two")], 3, "next")],
            [response([repository("one")], 2, "next"), response([repository("two")], 3)],
            [response([], 2, "next")],
        ]
        for pages in scenarios:
            with self.subTest(pages=pages), self.assertRaises(catalog.CatalogError):
                catalog.fetch_inventory(LOGIN, "test-token", NOW, lambda *args: pages.pop(0))

    def test_missing_or_invalid_pageinfo_fails(self):
        for page in ({}, {"hasNextPage": 1, "endCursor": None},
                     {"hasNextPage": True, "endCursor": None},
                     {"hasNextPage": False, "endCursor": 2}):
            data = response([repository()])
            data["user"]["repositories"]["pageInfo"] = page
            with self.subTest(page=page), self.assertRaises(catalog.CatalogError):
                catalog.fetch_inventory(LOGIN, "test-token", NOW, lambda *args: data)

    def test_graphql_errors_are_sanitized_and_fail_closed(self):
        data = response([repository()])
        data["errors"] = [{"message": "DO-NOT-PRINT-REMOTE-DATA"}]
        with self.assertRaises(catalog.CatalogError) as raised:
            catalog.fetch_inventory(LOGIN, "test-token", NOW, lambda *args: data)
        self.assertNotIn("DO-NOT-PRINT", str(raised.exception))
        with self.assertRaises(catalog.CatalogError):
            catalog.metrics.validate_graphql_payload({"data": data, "errors": [{"message": "partial"}]})


class MarkdownTests(unittest.TestCase):
    def test_latest_eight_use_creation_order_and_link_default_branch_commit(self):
        nodes = [repository(f"repo-{i:02d}", f"2026-11-{i + 1:02d}T00:00:00Z") for i in range(10)]
        nodes[0]["pushedAt"] = "2026-12-01T00:00:00Z"
        section = catalog.render_section(inventory(nodes))
        rows = [line for line in section.splitlines() if line.startswith("| [")]
        self.assertEqual(len(rows), 8)
        self.assertIn("repo\\-09", rows[0])
        self.assertNotIn("repo\\-00", section)
        self.assertIn(f"09/11/2026 10:30 · {OID[:7]}", section)
        self.assertIn(f"/commit/{OID})", section)
        self.assertIn("curadoria manual", section)

    def test_description_markup_controls_pipes_and_newlines_are_escaped(self):
        item = repository("sample_name")
        item["description"] = '<script>x</script> | [click](javascript:alert(1))\n*bold*\x00\u202e tail'
        section = catalog.render_section(inventory([item]))
        self.assertNotIn("<script>", section)
        self.assertNotIn("\x00", section)
        self.assertNotIn("\u202e", section)
        self.assertIn("&lt;script&gt;", section)
        self.assertIn("\\|", section)
        self.assertIn(r"\[click\]\(javascript:alert\(1\)\)", section)
        self.assertIn(r"\*bold\*", section)
        self.assertIn("sample\\_name", section)
        self.assertEqual(len([line for line in section.splitlines() if line.startswith("| [")]), 1)

    def test_urls_cannot_escape_github_or_markdown(self):
        for field, bad in (("url", "https://example.com/sample"),
                           ("url", f"https://github.com/{LOGIN}/sample)"),
                           ("name", "sample](https://example.com)")):
            item = repository()
            item[field] = bad
            with self.subTest(field=field, bad=bad), self.assertRaises(catalog.CatalogError):
                inventory([item])
        item = repository()
        item["defaultBranchRef"]["target"]["url"] = "javascript:alert(1)"
        with self.assertRaises(catalog.CatalogError):
            inventory([item])


class PublicationTests(unittest.TestCase):
    def prepare(self, directory):
        root = Path(directory)
        (root / "evidencias").mkdir()
        catalogue = "intro\n" + catalog.BEGIN + "\nold generated\n" + catalog.END + "\neditorial delivery\n"
        (root / "PROJETOS-ABERTOS.md").write_text(catalogue)
        (root / "evidencias" / "public-projects.json").write_text("original snapshot\n")
        return root, catalogue

    def test_later_page_failure_preserves_both_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root, before = self.prepare(directory)
            calls = []

            def fetcher(*args):
                calls.append(args)
                if len(calls) == 1:
                    return response([repository()], total=2, next_cursor="next")
                raise catalog.CatalogError("network unavailable")

            with self.assertRaises(catalog.CatalogError):
                catalog.update_catalog(LOGIN, root, "test-token", NOW, fetcher)
            self.assertEqual((root / "PROJETOS-ABERTOS.md").read_text(), before)
            self.assertEqual((root / "evidencias" / "public-projects.json").read_text(), "original snapshot\n")
            self.assertFalse(list(root.rglob("*.tmp")))

    def test_invalid_markers_preserve_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root, _ = self.prepare(directory)
            (root / "PROJETOS-ABERTOS.md").write_text("editorial only")
            with self.assertRaises(catalog.CatalogError):
                catalog.update_catalog(LOGIN, root, "test-token", NOW, lambda *args: response([repository()]))
            self.assertEqual((root / "evidencias" / "public-projects.json").read_text(), "original snapshot\n")
            self.assertEqual((root / "PROJETOS-ABERTOS.md").read_text(), "editorial only")

    def test_success_changes_only_generated_section_and_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root, before = self.prepare(directory)
            actual = catalog.update_catalog(LOGIN, root, "test-token", NOW,
                                            lambda *args: response([repository("b"), repository("a")]))
            saved = json.loads((root / "evidencias" / "public-projects.json").read_text())
            self.assertEqual(saved, actual)
            self.assertEqual(saved["collectedAt"], "2026-11-09T12:30:00Z")
            self.assertEqual([item["name"] for item in saved["repositories"]], ["a", "b"])
            updated = (root / "PROJETOS-ABERTOS.md").read_text()
            self.assertEqual(updated.split(catalog.BEGIN)[0], before.split(catalog.BEGIN)[0])
            self.assertEqual(updated.split(catalog.END)[1], before.split(catalog.END)[1])
            self.assertFalse(list(root.rglob("*.tmp")))
            self.assertEqual(set(saved), {"collectedAt", "login", "publicRepositoryCount", "repositories"})


if __name__ == "__main__":
    unittest.main()
