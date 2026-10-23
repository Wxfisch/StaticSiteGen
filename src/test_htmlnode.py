import unittest
from htmlnode import HTMLNode


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

if __name__ == "__main__":
  unittest.main()