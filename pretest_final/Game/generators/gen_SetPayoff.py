from generators import HtmlGenerator as html
# INITS
title = f'Bitte klicken Sie auf Weiter!'
filename = 'SetPayoff'
url = f'../templates/Game/{filename}.html'


# NEXT BUTTON
p_next = "Das Hauptexperiment ist nun abgeschlossen. Bitte klicken Sie auf <em>Weiter</em>, um fortzufahren."
p_next = html.paragraph(p_next)
button_next = html.next_button()
div_next = f"""
<div class="{'otree-next'}" id="{'otree-next'}">
    {p_next}
    {button_next}
</div>
"""

# OUTPUT
code = div_next
html.code(title, code, url)
