from enum import Enum
from re import match

from leafnode import LeafNode


class TextType(Enum):
   TEXT = "text"
   BOLD = "bold"
   ITALIC = "italic"
   CODE = "code"
   IMAGE = "image"
   LINK = "link"

class TextNode:
   def __init__(self, text: str, text_type: TextType, url: str = None):
      self.text = text
      self.text_type = text_type
      self.url = url

   def __eq__(self, value):
      return ( self.text == value.text 
              and self.text_type == value.text_type 
              and self.url == value.url )
   
   def __repr__(self):
      if self.url is None:
         return f"TextNode({self.text}, {self.text_type.value})"
      else:
         return f"TextNode({self.text}, {self.text_type.value}, {self.url}"
   
   def __str__(self):
      return f"{self.text} ({self.text_type.value})"

   def text_node_to_html_node(text_node):
      match text_node.text_type:
         case TextType.TEXT:
            return LeafNode(value=text_node.text)
         case TextType.BOLD:
            return LeafNode(value=text_node.text, tag="b")
         case TextType.ITALIC:
            return LeafNode(value=text_node.text, tag="i")
         case TextType.CODE:
            return LeafNode(value=text_node.text, tag="code")
         case TextType.IMAGE:
            return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
         case TextType.LINK:
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
         case _:
            raise ValueError("Invalid TextType")
         

   
