import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        equal_pairs = [
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a text node", TextType.BOLD),
            ),
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a text node", TextType.BOLD, None),
            ),
            (
                TextNode("This is a text node", TextType.BOLD, "https://example.com"),
                TextNode("This is a text node", TextType.BOLD, "https://example.com"),
            ),
        ]
        not_equal_pairs = [
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a different text node", TextType.BOLD),
            ),
            (
                TextNode("This is a text node", TextType.BOLD, "https://example.com"),
                TextNode("This is a different text node", TextType.BOLD, "https://example.com"),
            ),
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a text node", TextType.ITALIC),
            ),
            (
                TextNode("This is a text node", TextType.BOLD, "https://example.com"),
                TextNode("This is a text node", TextType.ITALIC, "https://example.com"),
            ),
            (
                TextNode("This is a text node", TextType.BOLD, "https://example.com"),
                TextNode("This is a text node", TextType.BOLD, "https://example.org"),
            ),
            (
                TextNode("This is a text node", TextType.BOLD),
                TextNode("This is a text node", TextType.BOLD, "https://example.com"),
            ),
        ]

        for left, right in equal_pairs:
            with self.subTest(left=left, right=right):
                self.assertEqual(left, right)

        for left, right in not_equal_pairs:
            with self.subTest(left=left, right=right):
                self.assertNotEqual(left, right)



if __name__ == "__main__":
    unittest.main()