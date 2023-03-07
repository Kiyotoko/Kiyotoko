import os
import argparse
import tqdm
import scripts


CONVERTERS = {
    'md2html': (scripts.md2html, lambda f: f.replace('.md', '.html')),
    'md2jpg': (scripts.md2jpg, lambda f: f.replace('.md', '.jpg'))
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
    args = parser.parse_args()

    lookup(args.input_location, args.output_location, args.converter)


if __name__ == "__main__":
    main()
