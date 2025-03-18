import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a italic node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_with_links(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a image node", TextType.IMAGE, "https://www.imgur.com/drawing")
        self.assertNotEqual(node, node2)
    



if __name__ == "__main__":
    unittest.main()
