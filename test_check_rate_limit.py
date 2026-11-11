import datetime
import io
import json
import unittest
import urllib.error
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import check_rate_limit as crl


SAMPLE_PAYLOAD = {
    "resources": {
        "core": {"limit": 5000, "used": 188, "remaining": 4812, "reset": 1794351600},
        "graphql": {"limit": 5000, "used": 0, "remaining": 5000, "reset": 1794353600},
        "search": {"limit": 30, "used": 2, "remaining": 28, "reset": 1794350160},
        "code_search": {"limit": 10, "used": 0, "remaining": 10, "reset": 1794350160},
        "source_import": {"limit": 100, "used": 5, "remaining": 95, "reset": 1794350160},
    },
    "rate": {"limit": 5000, "used": 188, "remaining": 4812, "reset": 1794351600},
}

SAMPLE_HEADERS = {
    "x-oauth-scopes": "public_repo, read:org",
    "github-authentication-token-expiration": "2027-01-01 00:00:00 UTC",
}


class TestCheckRateLimit(unittest.TestCase):
    def test_format_duration(self):
        self.assertEqual(crl.format_duration(-5), "now")
        self.assertEqual(crl.format_duration(0), "now")
        self.assertEqual(crl.format_duration(45), "in 45s")
        self.assertEqual(crl.format_duration(125), "in 2m 05s")
        self.assertEqual(crl.format_duration(3661), "in 1h 01m 01s")

    def test_select_buckets_default_vs_all(self):
        resources = SAMPLE_PAYLOAD["resources"]
        default_names = [name for name, _ in crl.select_buckets(resources, show_all=False)]
        # Includes core, graphql, search, plus source_import (used > 0), omits code_search (used == 0)
        self.assertEqual(default_names, ["core", "graphql", "search", "source_import"])

        all_names = [name for name, _ in crl.select_buckets(resources, show_all=True)]
        self.assertIn("code_search", all_names)

    def test_print_report_authenticated(self):
        buf = io.StringIO()
        crl.print_report(
            SAMPLE_PAYLOAD,
            SAMPLE_HEADERS,
            authenticated=True,
            now=1794350100,
            tz=datetime.timezone.utc,
            out=buf,
        )
        text = buf.getvalue()
        self.assertIn("Authenticated (GITHUB_TOKEN)", text)
        self.assertIn("public_repo, read:org", text)
        self.assertIn("2027-01-01 00:00:00 UTC", text)
        self.assertIn("4812 / 5000 (96%)", text)
        self.assertIn("in 25m 00s", text)
        self.assertIn("secondary content-creation rate limit", text)

    def test_main_json_output(self):
        out = io.StringIO()
        with patch.object(
            crl,
            "fetch_rate_limit",
            return_value=(SAMPLE_PAYLOAD, SAMPLE_HEADERS, True),
        ), redirect_stdout(out):
            rc = crl.main(["--json"])
        self.assertEqual(rc, 0)
        parsed = json.loads(out.getvalue())
        self.assertTrue(parsed["authenticated"])
        self.assertEqual(parsed["scopes"], "public_repo, read:org")
        self.assertEqual(parsed["resources"]["core"]["remaining"], 4812)

    def test_main_handles_http_error(self):
        err_body = io.BytesIO(b'{"message": "Bad credentials"}')
        http_err = urllib.error.HTTPError(
            crl.RATE_LIMIT_URL, 401, "Unauthorized", {}, err_body
        )
        err = io.StringIO()
        with patch.object(crl, "fetch_rate_limit", side_effect=http_err), redirect_stderr(err):
            rc = crl.main([])
        self.assertEqual(rc, 1)
        self.assertIn("(401 Unauthorized): Bad credentials", err.getvalue())


if __name__ == "__main__":
    unittest.main()
