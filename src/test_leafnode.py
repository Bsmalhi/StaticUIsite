import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode(tag="p", value="Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="Google", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Google</a>')