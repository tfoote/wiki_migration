import os
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import convert_to_markdown as ctm


class TestConvertMainSafety(unittest.TestCase):
    def setUp(self):
        self.orig_cwd = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
        os.chdir(self.tmp.name)
        os.makedirs("markdown_output")
        os.makedirs("pages/src")

        def entry(pkg, **extra):
            src = f"pages/src/{pkg}"
            with open(src, "w") as f:
                f.write("wiki")
            with open(f"markdown_output/{pkg}.md", "w") as f:
                f.write("OLD")
            return {"source_file": src,
                    "markdown_file": f"markdown_output/{pkg}.md", **extra}

        self.export = {
            "fresh": entry("fresh", tully2="ready"),
            "edited": entry("edited", edited=True),
            "dirty": entry("dirty"),
        }
        self.extend = {"ext": entry("ext")}
        self.submitted = {"done": entry("done")}
        for name, data in [("export_pages.yaml", self.export),
                           ("extend_pages.yaml", self.extend),
                           ("submitted_pages.yaml", self.submitted),
                           ("current_pages.yaml", {"done": self.submitted["done"],
                                                   "other": entry("other")})]:
            with open(name, "w") as f:
                yaml.dump(data, f)
        with open("export_pages.yaml") as f:
            self.export_text = f.read()

    def tearDown(self):
        os.chdir(self.orig_cwd)
        self.tmp.cleanup()

    def read(self, pkg):
        with open(f"markdown_output/{pkg}.md") as f:
            return f.read()

    def run_main(self, *argv):
        with patch.object(ctm, "convert_file", return_value="NEW"), \
             patch.object(ctm, "git_modified_files",
                          return_value={"markdown_output/dirty.md"}), \
             patch("builtins.print"):
            return ctm.main(list(argv))

    def test_default_only_touches_safe_queue_entries(self):
        self.assertEqual(self.run_main(), 0)
        self.assertEqual(self.read("fresh"), "NEW")
        self.assertEqual(self.read("ext"), "NEW")
        self.assertEqual(self.read("edited"), "OLD")
        self.assertEqual(self.read("dirty"), "OLD")
        self.assertEqual(self.read("done"), "OLD")
        self.assertEqual(self.read("other"), "OLD")  # not in a queue
        with open("export_pages.yaml") as f:
            self.assertEqual(f.read(), self.export_text)  # queue untouched

    def test_dry_run_writes_nothing(self):
        self.run_main("--dry-run")
        for pkg in ["fresh", "ext", "edited", "dirty", "done", "other"]:
            self.assertEqual(self.read(pkg), "OLD")

    def test_force_edited_still_skips_submitted(self):
        self.run_main("--force-edited")
        self.assertEqual(self.read("edited"), "NEW")
        self.assertEqual(self.read("dirty"), "NEW")
        self.assertEqual(self.read("done"), "OLD")

    def test_only(self):
        self.run_main("--only", "ext")
        self.assertEqual(self.read("ext"), "NEW")
        self.assertEqual(self.read("fresh"), "OLD")


if __name__ == "__main__":
    unittest.main()
