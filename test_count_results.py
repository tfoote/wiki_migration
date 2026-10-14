import io
import os
import tempfile
import unittest
from contextlib import redirect_stdout
import yaml

from count_results import count_results, summarize_group_reviews


class TestCountResults(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.current_file = os.path.join(self.temp_dir.name, "current.yaml")
        self.export_file = os.path.join(self.temp_dir.name, "export.yaml")
        self.extend_file = os.path.join(self.temp_dir.name, "extend.yaml")

        self.current_data = {
            "pkg_unmatched": {
                "source_file": "pages/pkg_unmatched/revisions/1",
                "unmatched": True,
            },
            "pkg_archived": {
                "source_file": "pages/pkg_archived/revisions/1",
                "repository": "https://github.com/example/archived.git",
                "repository_archived": True,
                "readme_exists": False,
            },
            "pkg_export_1": {
                "source_file": "pages/pkg_export_1/revisions/1",
                "repository": "https://github.com/example/exp1.git",
                "repository_archived": False,
                "readme_exists": False,
            },
            "pkg_export_2": {
                "source_file": "pages/pkg_export_2/revisions/1",
                "repository": "https://github.com/example/exp2.git",
                "repository_archived": False,
                "readme_exists": False,
            },
            "pkg_export_3": {
                "source_file": "pages/pkg_export_3/revisions/1",
                "repository": "https://github.com/example/exp3.git",
                "repository_archived": False,
                "readme_exists": False,
            },
            "pkg_extend_1": {
                "source_file": "pages/pkg_extend_1/revisions/1",
                "repository": "https://github.com/example/ext1.git",
                "repository_archived": False,
                "readme_exists": True,
            },
            "pkg_extend_2": {
                "source_file": "pages/pkg_extend_2/revisions/1",
                "repository": "https://github.com/example/ext2.git",
                "repository_archived": False,
                "readme_exists": True,
            },
        }

        with open(self.current_file, "w") as f:
            yaml.dump(self.current_data, f)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_count_results_unreviewed_and_readonly(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            res = count_results(
                current_file=self.current_file,
                export_file=self.export_file,
                extend_file=self.extend_file,
            )

        self.assertEqual(res["total"], 7)
        self.assertEqual(res["matched"], 6)
        self.assertEqual(res["unmatched"], 1)
        self.assertEqual(res["archived"], 1)
        self.assertEqual(res["exported"]["total"], 3)
        self.assertEqual(res["exported"]["edited"], 0)
        self.assertEqual(res["exported"]["reviews"], {})
        self.assertEqual(res["extended"]["total"], 2)
        self.assertEqual(res["extended"]["edited"], 0)
        self.assertEqual(res["extended"]["reviews"], {})

        # Verify read-only behavior: export.yaml and extend.yaml were not created
        self.assertFalse(os.path.exists(self.export_file))
        self.assertFalse(os.path.exists(self.extend_file))

    def test_count_results_with_reviews_in_export_and_extend_files(self):
        export_reviews = {
            "pkg_export_1": {
                "repository": "https://github.com/example/exp1.git",
                "readme_exists": False,
                "repository_archived": False,
                "pass1": "ready",
                "edited": True,
            },
            "pkg_export_2": {
                "repository": "https://github.com/example/exp2.git",
                "readme_exists": False,
                "repository_archived": False,
                "pass1": "ignored",
            },
        }
        extend_reviews = {
            "pkg_extend_1": {
                "repository": "https://github.com/example/ext1.git",
                "readme_exists": True,
                "repository_archived": False,
                "pass1": "ready",
            },
        }

        with open(self.export_file, "w") as f:
            yaml.dump(export_reviews, f)
        with open(self.extend_file, "w") as f:
            yaml.dump(extend_reviews, f)

        export_mtime = os.path.getmtime(self.export_file)

        buf = io.StringIO()
        with redirect_stdout(buf):
            res = count_results(
                current_file=self.current_file,
                export_file=self.export_file,
                extend_file=self.extend_file,
            )

        output = buf.getvalue()
        self.assertIn("Review [pass1]:", output)
        self.assertEqual(res["exported"]["edited"], 1)
        self.assertEqual(
            res["exported"]["reviews"]["pass1"],
            {"ready": 1, "ignored": 1, "other": {}, "unreviewed": 1},
        )
        self.assertEqual(res["extended"]["edited"], 0)
        self.assertEqual(
            res["extended"]["reviews"]["pass1"],
            {"ready": 1, "ignored": 0, "other": {}, "unreviewed": 1},
        )

        # Ensure export_file was not modified
        self.assertEqual(os.path.getmtime(self.export_file), export_mtime)

    def test_filter_by_review_key(self):
        group_data = {
            "pkg1": {"pass1": "ready", "pass2": "ignored"},
            "pkg2": {"pass1": "ready"},
        }
        summary = summarize_group_reviews(group_data, review_key="pass2")
        self.assertEqual(list(summary["reviews"].keys()), ["pass2"])
        self.assertEqual(
            summary["reviews"]["pass2"],
            {"ready": 0, "ignored": 1, "other": {}, "unreviewed": 1},
        )


if __name__ == "__main__":
    unittest.main()
