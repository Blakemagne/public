import unittest
from ssg import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")
    
    def test_extract_title_with_whitespace(self):
        markdown = "#     Hello    "
        self.assertEqual(extract_title(markdown), "Hello")
    
    def test_extract_title_multiline(self):
        markdown = """
        Some text here
        # The Title
        Some more text
        """
        self.assertEqual(extract_title(markdown), "The Title")
    
    def test_extract_title_no_h1(self):
        markdown = """
        Some text here
        ## Not an h1
        Some more text
        """
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()