from generators import HtmlGenerator as html

# INITS
title = 'Zwischenteil: Nicht-Auszahlungsrelevante Fragen'
filename = 'ZwischenteilIntro'
url = f'../templates/Game/{filename}.html'


# CONTENT
p1 = """
Sie haben nun die ersten 40 Entscheidungen getroffen, die Ihre Aufwandsentschädigung beeinflussen. 
Es folgen 16 Fragen, die Ihre Aufwandsentschädigung nicht beeinflussen.
"""
p1 = html.paragraph(p1)

p2 = """
Nachdem Sie diese beantwortet haben, können Sie mit dem zweiten Teil mit 40 Entscheidungssituationen fortfahren. 
Die Entscheidungen in diesem Teil sind dann wieder für ihre Auszahlung relevant. 
"""
p2 = html.paragraph(p2)


# NEXT BUTTON
p_next = "Bitte klicken Sie auf <em>Weiter</em>, um mit den Fragen aus dem Zwischenteil zu starten."
p_next = html.paragraph(p_next)
button_next = html.next_button()
div_next = f"""
<div class="{'otree-next'}" id="{'otree-next'}">
    {p_next}
    {button_next}
</div>
"""


# OUTPUT
code = p1 + p2 + div_next
html.code(title, code, url)

