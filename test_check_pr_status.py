import io
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import check_pr_status as cps

cps.MERGEABLE_RETRY_DELAY = 0

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


def row(state="OPEN", review="", merge="clean", **kw):
    r = {"state": state, "review": review, "mergeable_state": merge}
    r.update(kw)
    return r


class TestNextStep(unittest.TestCase):
    def test_classification(self):
        cases = [
            (row(review="APPROVED", merge="clean"), "READY"),
            (row(review="APPROVED", merge="unstable"), "READY"),
            (row(review="APPROVED", merge="unknown"), "READY"),
            (row(review="APPROVED", merge="behind"), "BEHIND"),
            (row(review="APPROVED", merge="blocked"), "BLOCKED"),
            (row(review="APPROVED", merge="dirty"), "CONFLICT"),
            (row(review="", merge="clean"), "REVIEW"),
            (row(review="COMMENTED", merge="blocked"), "REVIEW"),
            (row(review="", merge="dirty"), "CONFLICT"),
            (row(review="CHANGES_REQUESTED", merge="dirty"), "CHANGES"),
            (row(state="DRAFT", review="APPROVED"), "DRAFT"),
            (row(state="MERGED", review="APPROVED"), ""),
            (row(state="CLOSED"), ""),
        ]
        for r, expected in cases:
            self.assertEqual(cps.next_step(r), expected, r)

    def test_summary_groups_ready_and_review(self):
        base = {"comments": 0, "additions": 1, "deletions": 0, "changed_files": 1,
                "created_at": "2026-10-01T00:00:00Z", "updated_at": "2026-10-02T00:00:00Z",
                "closed_at": "", "kind": "main", "base": "main", "number": 1, "repo": "o/r"}
        rows = [
            dict(base, package="ready_pkg", url="https://github.com/o/r/pull/1", state="OPEN",
                 review="APPROVED", mergeable_state="unstable", next="READY"),
            dict(base, package="review_pkg", url="https://github.com/o/r/pull/2", state="OPEN",
                 review="", mergeable_state="clean", next="REVIEW",
                 requested_reviewers=["maint"]),
        ]
        out = io.StringIO()
        cps.print_summary(rows, {"ready_pkg": {}, "review_pkg": {}}, out)
        text = out.getvalue()
        self.assertIn("Ready to merge:     1", text)
        self.assertIn("Needs review:       1", text)
        self.assertIn("Ready to merge (approved and mergeable):\n  ready_pkg: "
                      "https://github.com/o/r/pull/1", text)
        self.assertIn("some checks failing", text)
        self.assertIn("Needs review (no approving review yet):\n  review_pkg:", text)
        self.assertIn("requested: maint", text)

    def test_mergeability_refetched_when_not_computed(self):
        calls = []
        responses = [{"state": "open", "mergeable": None, "mergeable_state": "unknown"},
                     {"state": "open", "mergeable": True, "mergeable_state": "clean"}]

        def api(url, method="GET", data=None, token=None, accept_statuses=None):
            calls.append(url)
            if url.endswith("/reviews?per_page=100"):
                return [{"state": "APPROVED", "user": {"login": "m"}}]
            return responses.pop(0)

        with patch("check_pr_status.github_api_request", side_effect=api), \
             patch("check_pr_status.MERGEABLE_RETRY_DELAY", 0.01), \
             patch("check_pr_status.time.sleep"):
            r = cps.fetch_pr_status("https://github.com/o/r/pull/5")
        self.assertEqual(r["mergeable_state"], "clean")
        self.assertEqual(r["next"], "READY")
        self.assertEqual(len([c for c in calls if c.endswith("/pulls/5")]), 2)


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
        self.assertIn("Changes requested (a reviewer requested changes):", text)
        self.assertIn("Next steps for open PRs:", text)
        self.assertIn("CHANGES", text)  # Next column
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
