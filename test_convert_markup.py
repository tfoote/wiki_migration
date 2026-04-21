import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from convert_to_markdown import preprocess


class TestMarkupConversion(unittest.TestCase):

    def test_bold_conversion(self):
        content = "Some text '''bold text''' more text"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(preprocessed, "Some text **bold text** more text")

    def test_italic_conversion(self):
        content = "Some text ''italic text'' more text"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(preprocessed, "Some text //italic text// more text")

    def test_nested_bold_italic(self):
        content = "'''''Bold and italics''' italics only''"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(
            preprocessed, "//**Bold and italics** italics only//"
        )

    def test_nested_italic_bold(self):
        content = "'''''Italics and bold'' bold only'''"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(
            preprocessed, "**//Italics and bold// bold only**"
        )

    def test_italics_nested_in_bold(self):
        content = "'''''italics'' bold'''"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(preprocessed, "**//italics// bold**")

    def test_markup_in_code_block(self):
        content = "{{{\n'''Bold in code'''\n}}}"
        preprocessed, code_blocks = preprocess(content)
        self.assertEqual(preprocessed, "PLACEHOLDER_CODE_BLOCK_0")
        self.assertEqual(code_blocks, ["\n'''Bold in code'''\n"])


if __name__ == "__main__":
    unittest.main()
