from generators import HtmlGenerator as html
import numpy as np


def codeHtml(block_number: int):
    # INITS
    title = f'Block {block_number}'
    filename = f'Block{block_number}Intro'
    url = f'../templates/Game/{filename}.html'


    # CONTENT
    p1 = """
    "In jeder Entscheidungssituation werden Sie 21 Entscheidungen treffen müssen, dabei müssen Sie sich jeweils zwischen den beiden Optionen entscheiden. 
    Ab der Zeile, in der Sie Ihre Entscheidung von einer Option zur anderen wechseln, füllt der Computer automatisch die nachfolgenden Zeilen für Sie aus. 
    Sie können diese automatische ausgefüllten Zeilen manuell korrigieren, indem Sie wieder zur anderen Option wechseln.“
    """
    p1 = html.paragraph(p1)


    # NEXT BUTTON
    p_next = "Bitte klicken Sie auf <em>Weiter</em>, um mit den Entscheidungssituationen fortzufahren."
    p_next = html.paragraph(p_next)
    button_next = html.next_button()
    div_next = f"""
    <div class="{'otree-next'}" id="{'otree-next'}">
        {p_next}
        {button_next}
    </div>
    """

    # OUTPUT
    code = p1 + div_next
    html.code(title, code, url)


for block in np.arange(1, 2+1):
    codeHtml(block)

