import unittest
from htmlnode import HTMLNode, LeafNode

#Tests for main HTMLNode class
class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class="container" id="main"')

    def test_repr(self):
        node = HTMLNode(tag="span", value="Sample text", props={"style": "color: red;"})
        expected_repr = "HTMLNode(tag=span, value=Sample text, children=None, props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected_repr)

#Tests for leaf HTMLNodes
class TestLeafNode(unittest.TestCase):
    def test_to_html_without_tag(self):
        node = LeafNode(tag=None, value="Plain text")
        self.assertEqual(node.to_html(), "Plain text")

    def test_to_html_with_tag(self):
        node = LeafNode(tag="p", value="Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_to_html_with_props(self):
        node = LeafNode(
            tag="a",
            value="Click Me!",
            props={"href": "https://www.bing.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.bing.com">Click Me!</a>',
        )

    def test_to_html_without_value_raises_value_error(self):
        node = LeafNode(tag="p", value=None) # type: ignore
        self.assertRaises(ValueError, node.to_html)

if __name__ == "__main__":
  unittest.main()