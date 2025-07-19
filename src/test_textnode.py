import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertEqual(node.url, None)
        self.assertEqual(str(node), "TextNode(This is a text node, bold, None)")

        node3 = TextNode("t", TextType.LINK, url="t")
        self.assertNotEqual(node, node3)

if __name__ == "__main__":
    unittest.main()
