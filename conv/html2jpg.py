import imgkit
if __name__ == "__main__":
    from core import STYLESHEETS, OPTIONS
else:
    from conv.core import STYLESHEETS, OPTIONS


def html2jpg(inp: str, out: str, css: list = STYLESHEETS, opt: dict[str, any] = OPTIONS) -> None:
    imgkit.from_file(inp, out, css=css, options=opt)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        prog = 'html2jpg',
        description = 'Converts html to markdown files.',
        epilog = 'Text at the bottom of help'
    )
    parser.add_argument(
        "input_file",
        type=str
    )
    parser.add_argument(
        "output_file",
        type=str
    )
    parser.add_argument(
        "--css",
        default=STYLESHEETS,
        type=list,
        nargs="+"
    )
    parser.add_argument(
        "--encoding",
        default="UTF-8",
        type=str
    )
    parser.add_argument(
        "-W", "--width",
        default=380,
        type=int
    )
    parser.add_argument(
        "-H", "--height",
        default=540,
        type=int
    )
    args = parser.parse_args()
    html2jpg(args.input_file, args.output_file, css=args.css, opt={
        "encoding": args.encoding,
        "width": args.width,
        "height": args.height
    })


if __name__ == "__main__":
    main()