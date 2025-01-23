import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_objects(self):
        """Test that two TextNode objects with the same properties are equal."""
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_different_text(self):
        """Test that TextNode objects with different text properties are not equal."""
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        """Test that TextNode objects with different text_type properties are not equal."""
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_url_none_vs_not_none(self):
        """Test that TextNode objects with None URL and a valid URL are not equal."""
        node1 = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        """Test the __repr__ method of the TextNode class."""
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://example.com)")


if __name__ == "__main__":
    unittest.main()
