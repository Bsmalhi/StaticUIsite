import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        props = {
                    "href": "https://www.google.com",
                    "target": "_blank",
                }
        node1 = HTMLNode("This is a text node", "div", props = props)
        prop_str = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), prop_str)

    def test_not_eq(self):
        node = HTMLNode("This is a text node", "div")
        node2 = HTMLNode("This is a italic node", "div")
        self.assertNotEqual(node, node2)

    def test_not_eq_with_links(self):
        node = HTMLNode("This is a link node", "a", {"href": "https://www.google.com"})
        node2 = HTMLNode("This is a image node", "img", {"src": "https://www.imgur.com/drawing"})
        self.assertNotEqual(node, node2)