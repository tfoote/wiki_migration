import io
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import check_pr_status as cps

PRS = {
    "ros/angles/pulls/50": {"state": "closed", "merged_at": "2026-10-20T10:00:00Z",
                            "merged_by": {"login": "maint"}, "comments": 1,
                            "additions": 120, "deletions": 0, "changed_files": 3,
                            "review_comments": 0, "base": {"ref": "noetic-devel"},
                            "created_at": "2026-10-14T10:00:00Z",
                            "updated_at": "2026-10-20T10:00:00Z"},
    "ros/bond_core/pulls/118": {"state": "open", "draft": False, "comments": 2,
                                "additions": 40, "deletions": 2, "changed_files": 1,
                                "review_comments": 3, "base": {"ref": "noetic-devel"},
                                "created_at": "2026-10-21T10:00:00Z",
                                "updated_at": "2026-10-25T10:00:00Z"},
    "ros/bond_core/pulls/119": {"state": "closed", "merged_at": None,
                                "closed_at": "2026-10-22T10:00:00Z", "comments": 0,
                                "review_comments": 0, "base": {"ref": "ros2"},
                                "created_at": "2026-10-21T10:00:00Z",
                                "updated_at": "2026-10-22T10:00:00Z"},
}
REVIEWS = {
    "ros/bond_core/pulls/118": [
        {"state": "COMMENTED", "user": {"login": "a"}},
        {"state": "CHANGES_REQUESTED", "user": {"login": "b"}},
    ],
}


def fake_api(url, method="GET", data=None, token=None, accept_statuses=None):
    path = url.replace("https://api.github.com/repos/", "")
    if path.endswith("/reviews?per_page=100"):
        return REVIEWS.get(path.split("/reviews")[0], [])
    if path == "ros/missing/pulls/1":
        import urllib.error
        raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
    return PRS[path]


SUBMITTED = {
    "angles": {"pr_url": "https://github.com/ros/angles/pull/50",
               "source_queue": "export_pages.yaml"},
    "bond": {"pr_url": "https://github.com/ros/bond_core/pull/118",
             "default_branch_pr_url": "https://github.com/ros/bond_core/pull/119"},
    "gone": {"pr_url": "https://github.com/ros/missing/pull/1"},
}


class TestCheckPrStatus(unittest.TestCase):
    def test_parse_pr_url(self):
        self.assertEqual(cps.parse_pr_url("https://github.com/ros/angles/pull/50"),
                         ("ros", "angles", 50))
        with self.assertRaises(ValueError):
            cps.parse_pr_url("https://example.com/x")

    def test_review_state_latest_per_reviewer(self):
        self.assertEqual(cps.latest_review_state([
            {"state": "CHANGES_REQUESTED", "user": {"login": "a"}},
            {"state": "APPROVED", "user": {"login": "a"}},
        ]), "APPROVED")
        self.assertEqual(cps.latest_review_state([]), "")

    def test_collect_states(self):
        with patch("check_pr_status.github_api_request", side_effect=fake_api):
            rows = cps.collect(SUBMITTED)
        states = {(r["package"], r["kind"]): r["state"] for r in rows}
        self.assertEqual(states, {
            ("angles", "main"): "MERGED",
            ("bond", "main"): "OPEN",
            ("bond", "default-branch"): "CLOSED",
            ("gone", "main"): "ERROR",
        })
        bond = [r for r in rows if r["package"] == "bond" and r["kind"] == "main"][0]
        self.assertEqual(bond["review"], "CHANGES_REQUESTED")
        self.assertEqual(bond["comments"], 5)

    def test_listing_and_summary_output(self):
        with patch("check_pr_status.github_api_request", side_effect=fake_api):
            rows = cps.collect(SUBMITTED)
        out = io.StringIO()
        cps.print_listing(rows, out)
        cps.print_summary(rows, SUBMITTED, out)
        text = out.getvalue()
        self.assertIn("ros/angles#50", text)
        self.assertIn("bond (default)", text)
        self.assertIn("changes requested", text)
        self.assertIn("Merged:", text)
        self.assertIn("Packages with a merged PR:          1", text)
        self.assertIn("Changes requested (open):", text)
        self.assertIn("Could not check:", text)
        self.assertIn("(1 could not be checked)", text)
        # lines changed: per PR in the listing, totals by state in the summary
        self.assertIn("+120/-0", text)
        self.assertIn("+40/-2", text)
        self.assertIn("Lines changed:", text)
        self.assertIn("All PRs:            +160/-2 in 4 file(s)", text)
        self.assertIn("Merged:             +120/-0 in 3 file(s)", text)
        self.assertIn("Open/draft:         +40/-2 in 1 file(s)", text)
        self.assertIn("Closed:             +0/-0 in 0 file(s)", text)

    def test_main_does_not_modify_submitted_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "submitted.yaml")
            with open(path, "w") as f:
                yaml.dump(SUBMITTED, f)
            before = open(path).read()
            with patch("check_pr_status.github_api_request", side_effect=fake_api), \
                 patch("sys.stdout", new_callable=io.StringIO) as out, \
                 patch("sys.stderr", new_callable=io.StringIO):
                cps.main(["--submitted-file", path])
            self.assertIn("Summary", out.getvalue())
            self.assertEqual(open(path).read(), before)


if __name__ == "__main__":
    unittest.main()
