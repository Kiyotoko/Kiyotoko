import os
import argparse
import tqdm
from conv import md2html, md2jpg


CONVERTERS = {
    'md2html': (md2html.md2html, lambda f: f.replace('.md', '.html')),
    'md2jpg': (md2jpg.md2jpg, lambda f: f.replace('.md', '.jpg'))
}


def lookup(inp: str, out: str, type: str):
    conv = CONVERTERS.get(type)
    for (dirpath, dirname, filenames) in os.walk(inp):
        for file in tqdm.tqdm(filenames):
            if(file.endswith('.md')):
                conv[0](dirpath + '/' + file, out + '/' + conv[1](file))


def main():
    parser = argparse.ArgumentParser(
        prog = 'ProgramName',
        description = 'What the program does',
        epilog = 'Text at the bottom of help'
    )
    parser.add_argument("input_location")
    parser.add_argument("output_location")
    parser.add_argument("--converter", default="md2html")
    parser.add_argument(
        "-W", "--width",
        default=540,
        type=int
    )
    parser.add_argument(
        "-H", "--height",
        default=380,
        type=int
    )
    args = parser.parse_args()
    lookup(args.input_location, args.output_location, args.converter)


if __name__ == "__main__":
    main()
