import unittest
from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node(self):
        cases = [
            (TextNode("plain", TextType.PLAIN), None, "plain", None),
            (TextNode("bold", TextType.BOLD), "b", "bold", None),
            (TextNode("italic", TextType.ITALIC), "i", "italic", None),
            (TextNode("code", TextType.CODE), "code", "code", None),
            (
                TextNode("link", TextType.LINKS, "https://example.com"),
                "a",
                "link",
                {"href": "https://example.com"},
            ),
            (
                TextNode("image alt", TextType.IMAGES, "image.png"),
                "img",
                "",
                {"src": "image.png", "alt": "image alt"},
            ),
        ]

        for node, tag, value, props in cases:
            with self.subTest(text_type=node.text_type):
                html_node = text_node_to_html_node(node)
                self.assertEqual(html_node.tag, tag)
                self.assertEqual(html_node.value, value)
                self.assertEqual(html_node.props, props)

    def test_link_and_image_require_url(self):
        for text_type in (TextType.LINKS, TextType.IMAGES):
            with self.subTest(text_type=text_type):
                node = TextNode("text", text_type)
                with self.assertRaisesRegex(ValueError, "must have a URL"):
                    text_node_to_html_node(node)

    def test_unsupported_text_type(self):
        node = TextNode("text", None) # type: ignore
        with self.assertRaisesRegex(ValueError, "Unsupported TextType"):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()