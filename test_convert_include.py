import os
import sys
import unittest
from unittest.mock import mock_open, patch

# Add the directory containing the script to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from convert_to_markdown import preprocess


class TestIncludeMacro(unittest.TestCase):
    @patch("os.path.exists")
    def test_include_success(self, mock_exists):
        # Setup mocks
        def exists_side_effect(path):
            if path == "pages/IncludedPage/current":
                return True
            if path == "pages/IncludedPage/revisions/00000002":
                return True
            return False

        mock_exists.side_effect = exists_side_effect

        mock_files = {
            "pages/IncludedPage/current": mock_open(read_data="00000002\n").return_value,
            "pages/IncludedPage/revisions/00000002": mock_open(
                read_data="Included Content"
            ).return_value,
        }

        def open_side_effect(path, *args, **kwargs):
            if path in mock_files:
                return mock_files[path]
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            content = "Some text <<Include(IncludedPage)>> more text"
            preprocessed, code_blocks = preprocess(content)

            self.assertEqual(
                preprocessed, "Some text Included Content more text"
            )

    @patch("os.path.exists")
    def test_include_missing_current(self, mock_exists):
        mock_exists.return_value = False

        content = "Some text <<Include(IncludedPage)>> more text"
        preprocessed, code_blocks = preprocess(content)

        self.assertIn(
            "[[Included page IncludedPage not found]]", preprocessed
        )

    @patch("os.path.exists")
    def test_include_recursive(self, mock_exists):
        def exists_side_effect(path):
            valid_paths = [
                "pages/PageA/current",
                "pages/PageA/revisions/00000001",
                "pages/PageB/current",
                "pages/PageB/revisions/00000002",
            ]
            return path in valid_paths

        mock_exists.side_effect = exists_side_effect

        mock_files = {
            "pages/PageA/current": mock_open(read_data="00000001\n").return_value,
            "pages/PageA/revisions/00000001": mock_open(
                read_data="Content A <<Include(PageB)>>"
            ).return_value,
            "pages/PageB/current": mock_open(read_data="00000002\n").return_value,
            "pages/PageB/revisions/00000002": mock_open(
                read_data="Content B"
            ).return_value,
        }

        def open_side_effect(path, *args, **kwargs):
            if path in mock_files:
                return mock_files[path]
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            content = "<<Include(PageA)>>"
            preprocessed, code_blocks = preprocess(content)

            self.assertEqual(preprocessed, "Content A Content B")

    @patch("os.path.exists")
    def test_include_infinite_loop(self, mock_exists):
        def exists_side_effect(path):
            valid_paths = [
                "pages/PageA/current",
                "pages/PageA/revisions/00000001",
                "pages/PageB/current",
                "pages/PageB/revisions/00000002",
            ]
            return path in valid_paths

        mock_exists.side_effect = exists_side_effect

        mock_files = {
            "pages/PageA/current": mock_open(read_data="00000001\n").return_value,
            "pages/PageA/revisions/00000001": mock_open(
                read_data="Content A <<Include(PageB)>>"
            ).return_value,
            "pages/PageB/current": mock_open(read_data="00000002\n").return_value,
            "pages/PageB/revisions/00000002": mock_open(
                read_data="Content B <<Include(PageA)>>"
            ).return_value,
        }

        def open_side_effect(path, *args, **kwargs):
            if path in mock_files:
                return mock_files[path]
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=open_side_effect):
            content = "<<Include(PageA)>>"
            preprocessed, code_blocks = preprocess(content)

            self.assertTrue(len(preprocessed) > 0)


if __name__ == "__main__":
    unittest.main()
