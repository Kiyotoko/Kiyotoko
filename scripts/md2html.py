import markdown

def md2html(inp: str, out: str):
    markdown.markdownFromFile(encoding='utf8', extensions=['extra', 'pymdownx.arithmatex'], input=inp, output=out)