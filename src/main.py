import os
import pathlib


from textnode import TextNode, TextType

import helpers


def main():
    root = pathlib.Path(__file__).resolve().parent.parent
    static_path = root.joinpath("static")
    public_path = root.joinpath("public")
    helpers.copy_dir(str(static_path), str(public_path))

main()

