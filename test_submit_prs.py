import base64
import io
import json
import os
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stdout
from unittest.mock import patch
import yaml

import submit_prs


class TestSubmitPrsWorkflow(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.export_file = os.path.join(self.temp_dir.name, "export_pages.yaml")
        self.extend_file = os.path.join(self.temp_dir.name, "extend_pages.yaml")
        self.submitted_file = os.path.join(self.temp_dir.name, "submitted_pages.yaml")

        self.md_export = os.path.join(self.temp_dir.name, "pkg_export.md")
        self.md_extend = os.path.join(self.temp_dir.name, "pkg_extend.md")

        with open(self.md_export, "w", encoding="utf-8") as f:
            f.write("# pkg_export\n\nExported documentation content.\n")

        with open(self.md_extend, "w", encoding="utf-8") as f:
            f.write("## Wiki Documentation\n\nExtended documentation content.\n")

        self.export_data = {
            "pkg_export": {
                "branch": "noetic-devel",
                "markdown_file": self.md_export,
                "package_xml_match": True,
                "readme_exists": False,
                "repository": "https://github.com/ros-industrial/abb.git",
                "repository_archived": False,
                "source_file": "pages/pkg_export/revisions/00000002",
                "subdirectory": "pkg_export",
                "my_review": "ready",
            },
            "pkg_ignored": {
                "branch": "noetic-devel",
                "markdown_file": self.md_export,
                "package_xml_match": True,
                "readme_exists": False,
                "repository": "https://github.com/ros-industrial/abb.git",
                "repository_archived": False,
                "source_file": "pages/pkg_ignored/revisions/00000001",
                "subdirectory": "pkg_ignored",
                "my_review": "ignored",
            },
        }

        self.extend_data = {
            "pkg_extend": {
                "branch": "master",
                "markdown_file": self.md_extend,
                "package_xml_match": True,
                "readme_exists": True,
                "repository": "https://github.com/example/single_pkg_repo.git",
                "repository_archived": False,
                "source_file": "pages/pkg_extend/revisions/00000005",
                "subdirectory": "",
                "my_review": "ready",
            },
        }

        with open(self.export_file, "w", encoding="utf-8") as f:
            yaml.dump(self.export_data, f)

        with open(self.extend_file, "w", encoding="utf-8") as f:
            yaml.dump(self.extend_data, f)

    def tearDown(self):
        self.temp_dir.cleanup()

    def run(self, result=None):
        # These workflow tests simulate a first-time fork; the existing-fork
        # lookup is covered by TestForkLookup below.
        with patch("submit_prs.find_existing_fork", return_value=None):
            return super().run(result)

    def test_create_new_readme_same_default_branch(self):
        api_calls = []

        def fake_github_api(url, method="GET", data=None, token=None, accept_statuses=(200, 201, 202)):
            api_calls.append((method, url, data))
            if method == "POST" and url.endswith("/repos/ros-industrial/abb/forks"):
                self.assertEqual(data["organization"], submit_prs.FORK_ORG)
                return {
                    "owner": {"login": submit_prs.FORK_ORG},
                    "name": "abb",
                    "default_branch": "noetic-devel",
                }
            if method == "GET" and url.endswith("/git/ref/heads/noetic-devel"):
                return {"object": {"sha": "1234567890abcdef"}}
            if method == "POST" and url.endswith("/merge-upstream"):
                return {}
            if method == "POST" and url.endswith("/git/refs"):
                self.assertEqual(data["ref"], "refs/heads/ros-wiki-migration-pkg_export")
                self.assertEqual(data["sha"], "1234567890abcdef")
                return {"ref": data["ref"]}
            if method == "GET" and "/contents/pkg_export/README.md" in url:
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
            if method == "PUT" and url.endswith("/contents/pkg_export/README.md"):
                decoded = base64.b64decode(data["content"]).decode("utf-8")
                self.assertEqual(decoded, "# pkg_export\n\nExported documentation content.\n")
                self.assertNotIn("sha", data)
                self.assertIn("wiki.ros.org/pkg_export", data["message"])
                return {"commit": {"sha": "commitsha111"}}
            if method == "POST" and url.endswith("/repos/ros-industrial/abb/pulls"):
                self.assertEqual(
                    data["head"], f"{submit_prs.FORK_ORG}:ros-wiki-migration-pkg_export"
                )
                self.assertEqual(data["base"], "noetic-devel")
                self.assertIn("GitHub Markdown format", data["body"])
                self.assertIn("not be able to iterate", data["body"])
                self.assertIn("won't fix", data["body"])
                return {"html_url": "https://github.com/ros-industrial/abb/pull/42"}
            raise AssertionError(f"Unexpected API call: {method} {url}")

        buf = io.StringIO()
        with patch("submit_prs.github_api_request", side_effect=fake_github_api), patch(
            "sys.stdin", io.StringIO("Y\n")
        ), redirect_stdout(buf):
            submit_prs.process_yaml_file(
                yaml_file=self.export_file,
                submitted_file=self.submitted_file,
                review_key="my_review",
                token="fake-token",
            )

        output = buf.getvalue()
        self.assertIn("Submission Preview for Package: pkg_export", output)
        self.assertIn("Create new pkg_export/README.md", output)

        # Verify pkg_export was removed from export_pages.yaml, while pkg_ignored remains
        with open(self.export_file, "r", encoding="utf-8") as f:
            remaining_export = yaml.safe_load(f)
        self.assertNotIn("pkg_export", remaining_export)
        self.assertIn("pkg_ignored", remaining_export)

        # Verify pkg_export was added to submitted_pages.yaml without a second PR
        with open(self.submitted_file, "r", encoding="utf-8") as f:
            submitted = yaml.safe_load(f)
        self.assertIn("pkg_export", submitted)
        self.assertEqual(
            submitted["pkg_export"]["pr_url"],
            "https://github.com/ros-industrial/abb/pull/42",
        )
        self.assertNotIn("default_branch_pr_url", submitted["pkg_export"])
        self.assertEqual(submitted["pkg_export"]["action"], "create")

    def test_second_pr_opened_when_target_differs_from_default_branch(self):
        pr_payloads = []

        def fake_github_api(url, method="GET", data=None, token=None, accept_statuses=(200, 201, 202)):
            if method == "POST" and url.endswith("/repos/ros-industrial/abb/forks"):
                return {
                    "owner": {"login": submit_prs.FORK_ORG},
                    "name": "abb",
                    "parent": {"default_branch": "rolling"},
                }
            if method == "GET" and url.endswith("/git/ref/heads/noetic-devel"):
                return {"object": {"sha": "1111111111111111"}}
            if method == "GET" and url.endswith("/git/ref/heads/rolling"):
                return {"object": {"sha": "2222222222222222"}}
            if method == "POST" and url.endswith("/merge-upstream"):
                return {}
            if method == "POST" and url.endswith("/git/refs"):
                return {"ref": data["ref"]}
            if method == "GET" and "/contents/pkg_export/README.md" in url:
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
            if method == "PUT" and url.endswith("/contents/pkg_export/README.md"):
                return {"commit": {"sha": f"commit_{data['branch']}"}}
            if method == "POST" and url.endswith("/repos/ros-industrial/abb/pulls"):
                pr_payloads.append(data)
                if data["base"] == "noetic-devel":
                    return {"html_url": "https://github.com/ros-industrial/abb/pull/42"}
                elif data["base"] == "rolling":
                    return {"html_url": "https://github.com/ros-industrial/abb/pull/43"}
            raise AssertionError(f"Unexpected API call: {method} {url}")

        buf = io.StringIO()
        with patch("submit_prs.github_api_request", side_effect=fake_github_api), patch(
            "sys.stdin", io.StringIO("Y\n")
        ), redirect_stdout(buf):
            submit_prs.process_yaml_file(
                yaml_file=self.export_file,
                submitted_file=self.submitted_file,
                review_key="my_review",
                token="fake-token",
            )

        self.assertEqual(len(pr_payloads), 2)
        first_pr, second_pr = pr_payloads[0], pr_payloads[1]
        self.assertEqual(first_pr["base"], "noetic-devel")
        self.assertEqual(
            first_pr["head"], f"{submit_prs.FORK_ORG}:ros-wiki-migration-pkg_export"
        )
        self.assertNotIn("CAVEAT:", first_pr["body"])

        self.assertEqual(second_pr["base"], "rolling")
        self.assertEqual(
            second_pr["head"],
            f"{submit_prs.FORK_ORG}:ros-wiki-migration-pkg_export-rolling",
        )
        self.assertTrue(second_pr["body"].startswith("> [!WARNING]"))
        self.assertIn("duplicate of https://github.com/ros-industrial/abb/pull/42", second_pr["body"])
        self.assertIn("targeting the default branch (`rolling`)", second_pr["body"])
        self.assertIn("for better visibility", second_pr["body"])
        self.assertIn("not confirmed to be up to date", second_pr["body"])

        with open(self.submitted_file, "r", encoding="utf-8") as f:
            submitted = yaml.safe_load(f)
        self.assertEqual(
            submitted["pkg_export"]["pr_url"],
            "https://github.com/ros-industrial/abb/pull/42",
        )
        self.assertEqual(
            submitted["pkg_export"]["default_branch_pr_url"],
            "https://github.com/ros-industrial/abb/pull/43",
        )
        self.assertEqual(submitted["pkg_export"]["default_branch"], "rolling")

    def test_append_existing_readme_in_extend_pages(self):
        existing_readme = "# Existing Title\n\nExisting intro.\n"
        existing_b64 = base64.b64encode(existing_readme.encode("utf-8")).decode("ascii")

        def fake_github_api(url, method="GET", data=None, token=None, accept_statuses=(200, 201, 202)):
            if method == "POST" and url.endswith("/repos/example/single_pkg_repo/forks"):
                return {
                    "owner": {"login": submit_prs.FORK_ORG},
                    "name": "single_pkg_repo",
                    "default_branch": "master",
                }
            if method == "GET" and url.endswith("/git/ref/heads/master"):
                return {"object": {"sha": "abcdef1234567890"}}
            if method == "POST" and url.endswith("/merge-upstream"):
                return {}
            if method == "POST" and url.endswith("/git/refs"):
                return {"ref": data["ref"]}
            if method == "GET" and "/contents/README.md" in url:
                return {"content": existing_b64, "sha": "existingsha999"}
            if method == "PUT" and url.endswith("/contents/README.md"):
                decoded = base64.b64decode(data["content"]).decode("utf-8")
                self.assertEqual(
                    decoded,
                    "# Existing Title\n\nExisting intro.\n\n## Wiki Documentation\n\nExtended documentation content.\n",
                )
                self.assertEqual(data["sha"], "existingsha999")
                self.assertIn("Append pkg_extend README.md", data["message"])
                return {"commit": {"sha": "commitsha222"}}
            if method == "POST" and url.endswith("/repos/example/single_pkg_repo/pulls"):
                self.assertIn("appends the converted wiki documentation to `README.md`", data["body"])
                return {"html_url": "https://github.com/example/single_pkg_repo/pull/7"}
            raise AssertionError(f"Unexpected API call: {method} {url}")

        buf = io.StringIO()
        with patch("submit_prs.github_api_request", side_effect=fake_github_api), patch(
            "sys.stdin", io.StringIO("Y\n")
        ), redirect_stdout(buf):
            submit_prs.process_yaml_file(
                yaml_file=self.extend_file,
                submitted_file=self.submitted_file,
                review_key="my_review",
                token="fake-token",
            )

        with open(self.extend_file, "r", encoding="utf-8") as f:
            remaining_extend = yaml.safe_load(f) or {}
        self.assertNotIn("pkg_extend", remaining_extend)

        with open(self.submitted_file, "r", encoding="utf-8") as f:
            submitted = yaml.safe_load(f)
        self.assertIn("pkg_extend", submitted)
        self.assertEqual(submitted["pkg_extend"]["action"], "append")
        self.assertEqual(
            submitted["pkg_extend"]["pr_url"],
            "https://github.com/example/single_pkg_repo/pull/7",
        )

    def test_skip_does_not_submit_or_modify_files(self):
        buf = io.StringIO()
        with patch("submit_prs.github_api_request") as mock_api, patch(
            "sys.stdin", io.StringIO("S\n")
        ), redirect_stdout(buf):
            submit_prs.process_yaml_file(
                yaml_file=self.export_file,
                submitted_file=self.submitted_file,
                review_key="my_review",
                token="fake-token",
            )

        mock_api.assert_not_called()
        self.assertFalse(os.path.exists(self.submitted_file))
        with open(self.export_file, "r", encoding="utf-8") as f:
            remaining_export = yaml.safe_load(f)
        self.assertIn("pkg_export", remaining_export)


class TestForkLookup(unittest.TestCase):
    """Regression tests for duplicate forks (bond_core-1, bond_core-2, ...)."""

    UPSTREAM_FORK = {
        "fork": True, "name": "bond_core", "full_name": "org/bond_core",
        "owner": {"login": "org"},
        "parent": {"full_name": "ros/bond_core", "default_branch": "ros2"},
    }

    def test_existing_fork_is_reused_without_creating_a_new_one(self):
        calls = []

        def fake_api(url, method="GET", data=None, token=None, accept_statuses=None):
            calls.append((method, url))
            if url == "https://api.github.com/repos/org/bond_core":
                return self.UPSTREAM_FORK
            if "/git/ref/heads/" in url:
                return {"object": {"sha": "abc123"}}
            return {}

        with patch("submit_prs.github_api_request", side_effect=fake_api), \
             redirect_stdout(io.StringIO()):
            owner, repo, sha, default = submit_prs.ensure_fork(
                "ros", "bond_core", "org", "noetic-devel", "tok")
        self.assertEqual((owner, repo, sha, default), ("org", "bond_core", "abc123", "ros2"))
        self.assertFalse(any(m == "POST" and u.endswith("/forks") for m, u in calls))

    def test_renamed_fork_found_via_upstream_fork_list(self):
        renamed = dict(self.UPSTREAM_FORK, name="bond_core_fork",
                       full_name="org/bond_core_fork")

        def fake_api(url, method="GET", data=None, token=None, accept_statuses=None):
            if url == "https://api.github.com/repos/org/bond_core":
                raise urllib.error.HTTPError(url, 404, "Not Found", {}, None)
            if "/repos/ros/bond_core/forks?" in url:
                return [{"owner": {"login": "someone"}, "url": "x"},
                        {"owner": {"login": "org"},
                         "url": "https://api.github.com/repos/org/bond_core_fork"}]
            if url == "https://api.github.com/repos/org/bond_core_fork":
                return renamed
            raise AssertionError(url)

        with patch("submit_prs.github_api_request", side_effect=fake_api):
            info = submit_prs.find_existing_fork("ros", "bond_core", "org", "tok")
        self.assertEqual(info["name"], "bond_core_fork")

    def test_unrelated_repo_with_same_name_is_not_used(self):
        def fake_api(url, method="GET", data=None, token=None, accept_statuses=None):
            if url == "https://api.github.com/repos/org/bond_core":
                return {"fork": False, "name": "bond_core", "owner": {"login": "org"}}
            if "/forks?" in url:
                return []
            raise AssertionError(url)

        with patch("submit_prs.github_api_request", side_effect=fake_api):
            self.assertIsNone(submit_prs.find_existing_fork("ros", "bond_core", "org", "tok"))

    def test_pull_request_names_head_repo(self):
        sent = {}

        def fake_api(url, method="GET", data=None, token=None, accept_statuses=None):
            sent.update(data or {})
            return {"html_url": "https://github.com/ros/bond_core/pull/1"}

        with patch("submit_prs.github_api_request", side_effect=fake_api), \
             redirect_stdout(io.StringIO()):
            submit_prs.create_pull_request(
                "ros", "bond_core", "org", "ros-wiki-migration-bondpy", "noetic-devel",
                "bondpy", "src", "bondpy/README.md", "create", "tok", fork_repo="bond_core")
        self.assertEqual(sent["head"], "org:ros-wiki-migration-bondpy")
        self.assertEqual(sent["head_repo"], "bond_core")

    def test_http_errors_include_github_message(self):
        body = io.BytesIO(b'{"message": "Validation Failed", "errors": '
                          b'[{"message": "A pull request already exists"}]}')
        err = urllib.error.HTTPError("https://api.github.com/x", 422,
                                     "Unprocessable Entity", {}, body)
        with patch.object(submit_prs, "MUTATION_DELAY", 0), \
             patch("urllib.request.urlopen", side_effect=err):
            with self.assertRaises(urllib.error.HTTPError) as ctx:
                submit_prs.github_api_request("https://api.github.com/x", method="POST",
                                              data={}, token="tok")
        self.assertIn("Validation Failed; A pull request already exists", str(ctx.exception))
        self.assertIn("POST https://api.github.com/x", str(ctx.exception))


class _FakeHTTPResponse:
    def __init__(self, payload, status=200):
        self._bytes = json.dumps(payload).encode("utf-8")
        self.status = status

    def read(self):
        return self._bytes

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class TestRateLimitAndPacing(unittest.TestCase):
    def setUp(self):
        submit_prs._last_mutation_time = 0.0

    def test_primary_exhaustion_uses_ratelimit_reset(self):
        sleep_s, kind, desc = submit_prs.compute_rate_limit_sleep(
            403,
            {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1100"},
            {"message": "API rate limit exceeded"},
            "API rate limit exceeded",
            now=1000.0,
        )
        self.assertEqual(kind, "primary")
        self.assertEqual(sleep_s, 105.0)
        self.assertIn("Primary rate limit exhausted", desc)

    def test_secondary_prefers_retry_after_header_over_ratelimit_reset(self):
        sleep_s, kind, desc = submit_prs.compute_rate_limit_sleep(
            403,
            {
                "X-RateLimit-Remaining": "4900",
                "X-RateLimit-Reset": "4600",
                "Retry-After": "45",
            },
            {
                "message": "You have exceeded a secondary rate limit. "
                           "Please wait a few minutes before you try again."
            },
            "You have exceeded a secondary rate limit. "
            "Please wait a few minutes before you try again.",
            now=1000.0,
        )
        self.assertEqual(kind, "secondary")
        self.assertEqual(sleep_s, 45.0)
        self.assertIn("Retry-After: 45s", desc)

    def test_retry_after_http_date_header(self):
        wait = submit_prs.parse_retry_after_header(
            "Tue, 10 Nov 2026 22:05:00 GMT",
            now=1794348240.0,  # 2026-11-10 22:04:00 UTC
        )
        self.assertEqual(wait, 60.0)

    def test_body_duration_parsing_variants(self):
        # JSON numeric field
        self.assertEqual(
            submit_prs.parse_retry_after_body({"retry_after": 75}, "throttled"),
            (75.0, True),
        )
        # Explicit minutes / seconds / hours in prose
        self.assertEqual(
            submit_prs.parse_retry_after_body(
                {}, "You have exceeded a secondary rate limit. Please wait 5 minutes."
            ),
            (300.0, True),
        )
        self.assertEqual(
            submit_prs.parse_retry_after_body({}, "Please retry after 90 seconds."),
            (90.0, True),
        )
        self.assertEqual(
            submit_prs.parse_retry_after_body({}, "Temporarily blocked for 1 hour."),
            (3600.0, True),
        )
        self.assertEqual(
            submit_prs.parse_retry_after_body({}, "Please wait a minute before retrying."),
            (60.0, True),
        )
        # Fuzzy 'a few minutes'
        self.assertEqual(
            submit_prs.parse_retry_after_body(
                {}, "Please wait a few minutes before you try again."
            ),
            (180.0, False),
        )
        # UTC timestamp in message
        self.assertEqual(
            submit_prs.parse_retry_after_body(
                {},
                "Blocked until 2026-11-10T22:05:00Z.",
                now=1794348240.0,  # 22:04:00 UTC -> 60s + 5s buffer
            ),
            (65.0, True),
        )
        # Rate description ('80 requests per minute') is not misread as a duration
        self.assertEqual(
            submit_prs.parse_retry_after_body(
                {}, "You exceeded 80 requests per minute; retry later."
            ),
            (None, False),
        )

    def test_explicit_body_updates_sleep_even_with_shorter_header(self):
        sleep_s, kind, _ = submit_prs.compute_rate_limit_sleep(
            403,
            {"X-RateLimit-Remaining": "4900", "Retry-After": "30"},
            {"message": "Secondary rate limit: please wait 2 minutes before retrying."},
            "Secondary rate limit: please wait 2 minutes before retrying.",
            now=1000.0,
        )
        self.assertEqual(kind, "secondary")
        self.assertEqual(sleep_s, 120.0)

    def test_exponential_backoff_when_no_duration_given(self):
        msg = "You have exceeded a secondary rate limit. Please retry your request again later."
        waits = [
            submit_prs.compute_rate_limit_sleep(
                403, {"X-RateLimit-Remaining": "4900"}, {"message": msg}, msg, secondary_attempt=i
            )[0]
            for i in range(3)
        ]
        self.assertEqual(waits, [60.0, 120.0, 240.0])

    def test_permission_403_fails_immediately_without_sleeping(self):
        body = io.BytesIO(
            b'{"message": "Resource not accessible by personal access token"}'
        )
        err = urllib.error.HTTPError(
            "https://api.github.com/repos/o/r/pulls",
            403,
            "Forbidden",
            {"X-RateLimit-Remaining": "4950", "X-RateLimit-Reset": "9999999999"},
            body,
        )
        with patch.object(submit_prs, "MUTATION_DELAY", 0), \
             patch("urllib.request.urlopen", side_effect=err), \
             patch("time.sleep") as mock_sleep:
            with self.assertRaises(urllib.error.HTTPError) as ctx:
                submit_prs.github_api_request(
                    "https://api.github.com/repos/o/r/pulls",
                    method="POST",
                    data={},
                    token="tok",
                )
        mock_sleep.assert_not_called()
        self.assertIn("Resource not accessible", str(ctx.exception))

    def test_github_api_request_retries_secondary_limit_using_body_wait(self):
        body = io.BytesIO(
            b'{"message": "You have exceeded a secondary rate limit. '
            b'Please wait 2 minutes before you try again."}'
        )
        err = urllib.error.HTTPError(
            "https://api.github.com/repos/o/r/pulls",
            403,
            "Forbidden",
            {"X-RateLimit-Remaining": "4900", "X-RateLimit-Reset": "9999999999"},
            body,
        )
        ok_resp = _FakeHTTPResponse({"html_url": "https://github.com/o/r/pull/1"}, status=201)
        out = io.StringIO()
        with patch.object(submit_prs, "MUTATION_DELAY", 0), \
             patch("urllib.request.urlopen", side_effect=[err, ok_resp]), \
             patch("time.sleep") as mock_sleep, \
             redirect_stdout(out):
            resp = submit_prs.github_api_request(
                "https://api.github.com/repos/o/r/pulls",
                method="POST",
                data={},
                token="tok",
            )
        self.assertEqual(resp["html_url"], "https://github.com/o/r/pull/1")
        mock_sleep.assert_called_once_with(120.0)
        self.assertIn("Please wait 2 minutes", out.getvalue())

    def test_mutation_pacing_delays_consecutive_writes_only(self):
        responses = [
            _FakeHTTPResponse({"ok": 1}, status=201),
            _FakeHTTPResponse({"ok": 2}, status=200),
            _FakeHTTPResponse({"ok": 3}, status=201),
        ]
        # Monotonic timestamps:
        # POST #1 finishes at t=100.0
        # GET runs (does not check or update _last_mutation_time)
        # POST #2 checks at t=100.4 -> sleeps 1.5 - 0.4 = 1.1s, finishes at t=101.6
        clock = iter([100.0, 100.4, 101.6])
        with patch.object(submit_prs, "MUTATION_DELAY", 1.5), \
             patch("urllib.request.urlopen", side_effect=responses), \
             patch("time.monotonic", side_effect=lambda: next(clock)), \
             patch("time.sleep") as mock_sleep:
            submit_prs.github_api_request("https://api.github.com/a", method="POST", data={})
            submit_prs.github_api_request("https://api.github.com/b", method="GET")
            submit_prs.github_api_request("https://api.github.com/c", method="POST", data={})

        self.assertEqual(mock_sleep.call_count, 1)
        self.assertAlmostEqual(mock_sleep.call_args[0][0], 1.1, places=5)


if __name__ == "__main__":
    unittest.main()
