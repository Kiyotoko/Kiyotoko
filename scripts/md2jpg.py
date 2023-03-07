import scripts

def md2jpg(inp: str, out: str):
    temp = out.replace('.jpg', '.html')
    scripts.md2html(inp, temp)
    scripts.html2jpg(temp, out)