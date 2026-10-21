import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node6 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node7 = TextNode("This is a different text node", TextType.BOLD, "https://example.org")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node6, node7)



if __name__ == "__main__":
    unittest.main()