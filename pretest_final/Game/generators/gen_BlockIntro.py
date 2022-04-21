from generators import HtmlGenerator as html
import numpy as np


def codeHtml(block_number: int):
    # INITS
    title = f'Auszahlungsrelevante Entscheidungen: Teil {block_number}'
    filename = f'Block{block_number}Intro'
    url = f'../templates/Game/{filename}.html'


    # CONTENT
    p1 = f"""
    Nun beginnt Teil {block_number} der auszahlungsrelevanten Entscheidungen. 
    Die Entscheidungen, die sie jetzt treffen, sind für ihre Auszahlung relevant. 
    """
    p1 = html.paragraph(p1)


    # NEXT BUTTON
    p_next = "Bitte klicken Sie auf <em>Weiter</em>, um mit den auszahlungsrelevanten Entscheidungssituationen zu starten."
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

