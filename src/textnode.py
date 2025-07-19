from enum import Enum

class TextType(Enum):
    PLAIN = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    text: str
    text_type: TextType
    url: str | None = None

    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        if self.text_type in [TextType.IMAGE, TextType.LINK] and not url:
            raise ValueError("image and link must have an url provided")

        self.url = url

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TextNode):
            return NotImplemented
        return self.text == value.text and self.text_type == value.text_type and self.url == value.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
