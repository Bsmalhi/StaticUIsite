from htmlnode import HTMLNode
from typing import Dict, List

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: List[HTMLNode], props: Dict[str, str] = None):
        super().__init__(tag=tag, children=children, props=props)
        # self.children = children or []
        # self.tag = tag
        # self.props = props or {}
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        return f"<{self.tag}{self.props_to_html()}>{self.children_to_html()}</{self.tag}>"
    
    def children_to_html(self):
        return "".join([child.to_html() for child in self.children])