import sys
import pathlib


import markdown_blocks

import helpers


def main():
    if len(sys.argv) != 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    root = pathlib.Path(__file__).resolve().parent.parent
    static_path = root.joinpath("static")
    public_path = root.joinpath("docs")
    helpers.copy_dir(str(static_path), str(public_path))
    content_path = root.joinpath("content")

    template_path = root.joinpath("template.html")
    dest_path = root.joinpath("docs")
    markdown_blocks.generate_pages(
        basepath,
        str(content_path),
        str(template_path),
        str(dest_path),
    )


main()
