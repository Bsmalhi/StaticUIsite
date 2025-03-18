from typing import Dict
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: Dict[str, str] = None):
        super().__init__(tag=tag, value=value, props=props)
        self.value = value
        self.tag = tag
        self.props = props or {}
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    