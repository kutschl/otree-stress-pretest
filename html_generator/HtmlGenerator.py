def code(title: str, content: str, filename: str):
    # oTree
    br = """\n"""
    o_extends = """{% extends "global/Page.html" %}""" + br
    o_load = """{% load otree %}""" + br
    o_title = """{% block title %}""" + title + """{% endblock %}""" + br
    o_content = """{% block content %}""" + br + br + content + br + br + """{% next_button %}""" + br + br + """{% endblock %}"""
    # File
    f = open(filename, 'w')
    f.write(umlauts(o_extends + o_load + br + o_title + br + o_content))
    f.close()


def paragraph(content) -> str:
    return f"""
<p>
    {content}
</p>
"""


# type = ["mail", "phone"]
def link(type:str, url: str, content: str) -> str:
    if type is str('mail'):
        return f"""<a href="mailto:{url}">{content}</a>"""
    if type is str('phone'):
        return f"""<a href="tel:{url}">{content}</a>"""


def label(id: str, content: str) -> str:
    return f"""<label for="{id}">{content}</label>"""


def input(type: str, id: str) -> str:
    return f"""<input type="{type}" class="form-control" name="{id}" id="{id}"/>"""


def umlauts(string):
    return string\
        .replace("ä", "&auml;") \
        .replace("Ä", "&Auml;") \
        .replace("ö", "&ouml;") \
        .replace("Ö", "&Ouml;") \
        .replace("ü", "&uuml;") \
        .replace("Ü", "&Uuml;") \
        .replace("ß", "&szlig;") \
        .replace("€", "&euro;")

