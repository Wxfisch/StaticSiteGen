import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
# Tests for Parent HTML nodes
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children_preserves_order(self):
        parent_node = ParentNode(
            "ul",
            [LeafNode("li", "first"), LeafNode("li", "second")],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<ul><li>first</li><li>second</li></ul>",
        )

    def test_to_html_with_mixed_leaf_and_parent_children(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("p", "intro"),
                ParentNode("section", [LeafNode("span", "body")]),
                LeafNode("p", "outro"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>intro</p><section><span>body</span></section><p>outro</p></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_no_children_and_props(self):
        parent_node = ParentNode("div", [], props={"class": "empty"})
        self.assertEqual(parent_node.to_html(), '<div class="empty"></div>')

    def test_to_html_with_empty_nested_parent(self):
        parent_node = ParentNode("div", [ParentNode("span", [])])
        self.assertEqual(parent_node.to_html(), "<div><span></span></div>")

    def test_to_html_without_tag_raises_value_error(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])  # type: ignore
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_without_children_raises_value_error(self):
        parent_node = ParentNode("div", None)  # type: ignore
        self.assertRaises(ValueError, parent_node.to_html)

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(
            "div", [child_node], props={"class": "container", "id": "main"}
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><span>child</span></div>',
        )
    

if __name__ == "__main__":
  unittest.main()
