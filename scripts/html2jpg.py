import imgkit

def html2jpg(inp: str, out: str, css: list = ["data/Default.css"]) -> None:
    options = {
        'encoding': "UTF-8",
        'width': 9*50,
        'height': 16*50
    }
    imgkit.from_file(inp, out, css=css, options=options)
