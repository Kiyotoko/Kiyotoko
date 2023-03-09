import imgkit


DEFAULT_CSS = ["data/Default.css"]

DEFAULT_OPTIONS = {
    'encoding': "UTF-8",
    'width': 540,
    'height': 380
}


def html2jpg(inp: str, out: str, css: list = DEFAULT_CSS, options: dict[str, any] = DEFAULT_OPTIONS) -> None:
    imgkit.from_file(inp, out, css=css, options=options)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        prog = 'html2jpg',
        description = 'Converts html to markdown files.',
        epilog = 'Text at the bottom of help'
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--css", default="data/Default.css")
    parser.add_argument("-W","--width", default=540)
    parser.add_argument("-H", "--height", default=380)
    parser.add_argument("--encoding", default="UTF-8")
    args = parser.parse_args()
    html2jpg(args.input_file, args.output_file, args.css, {
        "encoding": args.encoding,
        "width": args.width,
        "height": args.height
    })


if __name__ == "__main__":
    main()