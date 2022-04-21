from generators import HtmlGenerator as html
# INITS
title = f'Ende: Auszahlungsrelevante Entscheidungen'
filename = 'SetPayoff'
url = f'../templates/Game/{filename}.html'


# CONTENT
p1 = """
Sie haben nun alle auszahlungsrelevanten Entscheidungen getroffen. 
Es folgt noch ein Fragebogen. 
"""
p1 = html.paragraph(p1)


# NEXT BUTTON
p_next = "Bitte klicken Sie auf <em>Weiter</em>, um fortzufahren."
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
