import os
import subprocess
import sys
import unittest
import yaml


class TestSubmitPrs(unittest.TestCase):
    def setUp(self):
        self.test_file = "export_pages_test.yaml"
        self.review_key = "test_review"
        # Reset test file content for each test
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
        with open(self.test_file, "w") as f:
            yaml.dump(self.initial_content, f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_skip(self):
        # Simulate entering 'S' for the first item and then 'Q' to quit
        p = subprocess.Popen(
            [
                "python3",
                "review_packages.py",
                "--review-key",
                self.review_key,
                self.test_file,
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out, err = p.communicate(input="S\nQ\n")

        print("STDOUT:", out)
        print("STDERR:", err)

        with open(self.test_file, "r") as f:
            data = yaml.safe_load(f)

        # Verify that no state changed for the first item
        self.assertNotIn(self.review_key, data["abb_irb1200_support"])

    def test_ready(self):
        # Simulate entering 'R' for the first item and then 'Q' to quit
        p = subprocess.Popen(
            [
                "python3",
                "review_packages.py",
                "--review-key",
                self.review_key,
                self.test_file,
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out, err = p.communicate(input="R\nQ\n")

        print("STDOUT:", out)
        print("STDERR:", err)

        with open(self.test_file, "r") as f:
            data = yaml.safe_load(f)

        # Verify that review_key is 'ready' for the first item
        self.assertEqual(data["abb_irb1200_support"].get(self.review_key), "ready")

    def test_ignore(self):
        # Simulate entering 'I' for the first item and then 'Q' to quit
        p = subprocess.Popen(
            [
                "python3",
                "review_packages.py",
                "--review-key",
                self.review_key,
                self.test_file,
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        out, err = p.communicate(input="I\nQ\n")

        print("STDOUT:", out)
        print("STDERR:", err)

        with open(self.test_file, "r") as f:
            data = yaml.safe_load(f)

        # Verify that review_key is 'ignored' for the first item
        self.assertEqual(
            data["abb_irb1200_support"].get(self.review_key), "ignored"
        )

    def test_edit(self):
        # Simulate entering 'E' for the first item, and then 'Q' to quit.
        # We use EDITOR='echo' to mock the editor.
        env = os.environ.copy()
        env["EDITOR"] = "echo"

        p = subprocess.Popen(
            [
                "python3",
                "review_packages.py",
                "--review-key",
                self.review_key,
                self.test_file,
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        # We need to send 'E' then 'Q' because after 'E' it returns to prompt.
        out, err = p.communicate(input="E\nQ\n")

        print("STDOUT:", out)
        print("STDERR:", err)

        with open(self.test_file, "r") as f:
            data = yaml.safe_load(f)

        # Verify that edited is True for the first item
        self.assertTrue(data["abb_irb1200_support"].get("edited"))


if __name__ == "__main__":
    unittest.main()
