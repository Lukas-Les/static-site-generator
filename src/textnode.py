from enum import Enum

class TextType(Enum):
    TEXT_PLAIN = "text"
    BOLD_TEXT = "bold_text"
    ITALIC_TEXT = "italic_text"
    CODE_TEXT = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    text: str
    text_type: TextType
    url: str | None = None

    def __init__(self, text: str, text_type: str, url: str | None = None) -> None:
        self.text = text
        self.text_type = TextType(value=text_type)
        if self.text_type in [TextType.IMAGE, TextType.LINK] and not url:
            raise ValueError("image and link must have an url provided")

        self.url = url

    def __eq__(self, value: object, /) -> bool:
        return self == value

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
