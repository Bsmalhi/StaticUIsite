from enum import Enum

class TextType(Enum):
   TEXT = "text"
   BOLD = "bold"
   ITALIC = "italic"
   CODE = "code"
   IMAGE = "image"
   LINK = "link"

class TextNode:
   Enum = Enum('TEXT', 'TEXT IMAGE VIDEO')
   def __init__(self, text: str, text_type: TextType, url: str = None):
      self.text = text
      self.text_type = text_type
      self.url = url

   def __eq__(self, value):
      return ( self.text == value.text 
              and self.text_type == value.text_type 
              and self.url == value.url )
   
   def __repr__(self):
      return f"TextNode({self.text}, {self.text_type.value}, {self.url}"
   
   def __str__(self):
      return f"{self.text} ({self.text_type.value})"

   
