if __name__ == "__main__":
    from md2html import md2html
    from html2jpg import html2jpg
    from core import STYLESHEETS, EXTENSIONS, OPTIONS
else:
    from conv.md2html import md2html
    from conv.html2jpg import html2jpg
    from conv.core import STYLESHEETS, EXTENSIONS, OPTIONS

def md2jpg(inp: str, out: str, ext: list[str] = EXTENSIONS, css: list[str] = STYLESHEETS, opt: dict[str, any] = OPTIONS):
    temp = out.replace('.jpg', '.html')
    print('Transforms: ', inp, ' to ', temp, ' to ', out)
    md2html(inp, temp, css=css, ext=ext)
    html2jpg(temp, out, css=css, opt=opt)


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
    md2jpg(args.input_file, args.output_file, css=args.css, opt={
        "encoding": args.encoding,
        "width": args.width,
        "height": args.height
    })


if __name__ == "__main__":
    main()