import os
import re
import subprocess
import sys
import tempfile
import unittest
import yaml


class TestReviewPackages(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = os.path.join(self.temp_dir.name, "export_pages_test.yaml")
        self.review_key = "test_review"
        self.initial_content = {
            "abb_irb1200_support": {
                "branch": "noetic-devel",
                "markdown_file": "markdown_output/abb_irb1200_support.md",
                "package_xml_match": True,
                "readme_exists": False,
                "repository": "https://github.com/ros-industrial/abb.git",
                "repository_archived": False,
                "source_file": "pages/abb_irb1200_support/revisions/00000002",
                "subdirectory": "abb_irb1200_support",
            },
            "abb_irb120_support": {
                "branch": "noetic-devel",
                "markdown_file": "markdown_output/abb_irb120_support.md",
                "package_xml_match": True,
                "readme_exists": False,
                "repository": "https://github.com/ros-industrial/abb.git",
                "repository_archived": False,
                "source_file": "pages/abb_irb120_support/revisions/00000004",
                "subdirectory": "abb_irb120_support",
            },
        }
        with open(self.test_file, "w", encoding="utf-8") as f:
            yaml.dump(self.initial_content, f)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _run_cli(self, user_input, extra_args=None, env=None):
        cmd = [
            sys.executable,
            "review_packages.py",
            "--review-key",
            self.review_key,
            *(extra_args or []),
            self.test_file,
        ]
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        out, err = p.communicate(input=user_input)
        self.assertEqual(p.returncode, 0, msg=f"STDERR: {err}\nSTDOUT: {out}")
        return out, err

    @staticmethod
    def _presented_packages(stdout_text):
        return re.findall(r"^Package: (.+)$", stdout_text, flags=re.MULTILINE)

    def test_skip(self):
        self._run_cli("S\nQ\n")

        with open(self.test_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for pkg in self.initial_content:
            self.assertNotIn(self.review_key, data[pkg])

    def test_ready(self):
        out, _ = self._run_cli("R\nQ\n")
        first_pkg = self._presented_packages(out)[0]

        with open(self.test_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self.assertEqual(data[first_pkg].get(self.review_key), "ready")
        other_pkgs = set(self.initial_content) - {first_pkg}
        for pkg in other_pkgs:
            self.assertNotIn(self.review_key, data[pkg])

    def test_ignore(self):
        out, _ = self._run_cli("I\nQ\n")
        first_pkg = self._presented_packages(out)[0]

        with open(self.test_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self.assertEqual(data[first_pkg].get(self.review_key), "ignored")
        other_pkgs = set(self.initial_content) - {first_pkg}
        for pkg in other_pkgs:
            self.assertNotIn(self.review_key, data[pkg])

    def test_edit(self):
        env = os.environ.copy()
        env["EDITOR"] = "echo"

        out, _ = self._run_cli("E\nQ\n", env=env)
        first_pkg = self._presented_packages(out)[0]

        with open(self.test_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self.assertTrue(data[first_pkg].get("edited"))

    def test_random_order_by_default_and_preserves_sorted_yaml(self):
        many_packages = {
            f"pkg_{i:02d}": {
                "branch": "noetic-devel",
                "markdown_file": "markdown_output/abb_irb1200_support.md",
                "repository": f"https://github.com/example/repo_{i:02d}.git",
                "subdirectory": f"pkg_{i:02d}",
            }
            for i in range(25)
        }
        with open(self.test_file, "w", encoding="utf-8") as f:
            yaml.dump(many_packages, f)

        # Mark the first presented package ready, skip the remaining 24.
        out, _ = self._run_cli("R\n" + "S\n" * 24)
        presented = self._presented_packages(out)

        expected_sorted = sorted(many_packages.keys())
        self.assertEqual(sorted(presented), expected_sorted)
        self.assertNotEqual(presented, expected_sorted)

        # Ensure saved YAML keeps keys sorted cleanly rather than shuffled.
        with open(self.test_file, "r", encoding="utf-8") as f:
            raw_lines = [
                line.rstrip(":\n")
                for line in f
                if line and not line[0].isspace()
            ]
        self.assertEqual(raw_lines, expected_sorted)

    def test_sequential_flag_preserves_file_order(self):
        many_packages = {
            f"pkg_{i:02d}": {
                "branch": "noetic-devel",
                "markdown_file": "markdown_output/abb_irb1200_support.md",
                "repository": f"https://github.com/example/repo_{i:02d}.git",
                "subdirectory": f"pkg_{i:02d}",
            }
            for i in range(10)
        }
        with open(self.test_file, "w", encoding="utf-8") as f:
            yaml.dump(many_packages, f)

        out, _ = self._run_cli("S\n" * 10, extra_args=["--sequential"])
        presented = self._presented_packages(out)
        self.assertEqual(presented, sorted(many_packages.keys()))

    def test_skips_already_reviewed_packages(self):
        content = dict(self.initial_content)
        content["abb_irb1200_support"] = dict(
            content["abb_irb1200_support"], **{self.review_key: "ignored"}
        )
        with open(self.test_file, "w", encoding="utf-8") as f:
            yaml.dump(content, f)

        out, _ = self._run_cli("S\n")
        self.assertIn(
            f"Skipping 1 package(s) already processed for {self.review_key} (1 remaining).",
            out,
        )
        self.assertEqual(self._presented_packages(out), ["abb_irb120_support"])

    def test_all_packages_already_reviewed(self):
        content = {
            pkg: dict(info, **{self.review_key: "ready"})
            for pkg, info in self.initial_content.items()
        }
        with open(self.test_file, "w", encoding="utf-8") as f:
            yaml.dump(content, f)

        out, _ = self._run_cli("")
        self.assertIn("No unreviewed packages remaining.", out)
        self.assertEqual(self._presented_packages(out), [])


if __name__ == "__main__":
    unittest.main()
