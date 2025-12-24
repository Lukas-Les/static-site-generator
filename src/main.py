import os
import pathlib


import markdown_blocks
from textnode import TextNode, TextType

import helpers


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    static_path = root.joinpath("static")
    public_path = root.joinpath("public")
    helpers.copy_dir(str(static_path), str(public_path))
    content_path = root.joinpath("content")

    template_path = root.joinpath("template.html")
    dest_path = root.joinpath("public")
    markdown_blocks.generate_pages(
        str(content_path),
        str(template_path),
        str(dest_path),
    )


main()
