from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
# returns True if all of the properties of two TextNode objects are equal
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

# returns a string representation of the TextNode object. Note: value is used to get the string value of the TextType enum
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    