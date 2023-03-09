import markdown
if __name__ == "__main__":
    from core import EXTENSIONS, STYLESHEETS, REPOSITORY
else:
    from conv.core import EXTENSIONS, STYLESHEETS, REPOSITORY


def md2html(inp: str, out: str, ext: list[str] = EXTENSIONS, css: list[str] = STYLESHEETS) -> None:
    markdown.markdownFromFile(encoding='utf8', extensions=ext, input=inp, output=out)
    builder = ''
    with open(out, 'r') as file:
        builder = parse_html([parse_css(css[index]) for index in range(len(css))], [file.read()])
    with open(out, 'w') as file:
        file.write(builder)


def parse_css(css: str) -> str:
    return '<link rel="stylesheet" href="'+REPOSITORY+'/'+css+'">'


def parse_html(heads: list = [], bodies: list = []):
    builder = '<html>\n<head>\n'
    for head in heads:
        builder+=head+'\n'
    builder+='</head>\n<body>\n'
    for body in bodies:
        builder+=body+'\n'
    builder+='</body>\n</html>'
    return builder


def main():
    import argparse
    parser = argparse.ArgumentParser(
        prog = 'md2html',
        description = 'Converts markdown to html files.',
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
        "--ext",
        default=EXTENSIONS,
        type=list,
        nargs="+"
    )
    parser.add_argument(
        "--css",
        default=STYLESHEETS,
        type=list,
        nargs="+"
    )
    args = parser.parse_args()
    md2html(args.input_file, args.output_file, args.ext, args.css)


if __name__ == "__main__":
    main()