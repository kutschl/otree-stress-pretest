def code(title: str, content: str, filename: str):
    # oTree
    br = """\n"""
    o_extends = """{% extends "global/Page.html" %}""" + br
    o_load = """{% load otree %}""" + br
    o_title = """{% block title %}""" + title + """{% endblock %}""" + br
    o_content = """{% block content %}""" + br + br + content + br + br + """{% endblock %}"""
    # File
    f = open(filename, 'w')
    f.write(umlauts(o_extends + o_load + br + o_title + br + o_content))
    f.close()


def next_button() -> str:
    return "{% next_button %}"


def paragraph(content) -> str:
    return f"""
<p>
    {content}
</p>
"""


def script(content) -> str:
    return f"""
<script>
{content}
</script>
"""


def style(content) -> str:
    return f"""
<style>
{content}
</style>
"""


# type = ["mail", "phone"]
def link(type:str, url: str, content: str) -> str:
    if type is str('mail'):
        return f"""<a href="mailto:{url}">{content}</a>"""
    if type is str('phone'):
        return f"""<a href="tel:{url}">{content}</a>"""
    if type is str('web'):
        return f"""<a href="{url}">{content}</a>"""


def headline(type: int, content: str) -> str:
    return f"""<h{type}>{content}</h{type}>"""


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
        .replace("€", "&euro;") \
        .replace("§", "&sect;") \
        .replace("–", "&ndash;") \
        .replace("„", "&bdquo;") \
        .replace("“", "&ldquo;")


