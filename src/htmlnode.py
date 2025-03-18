"""
tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
"""

from typing import Dict, List

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: List["HTMLNode"] = None, props: Dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    
