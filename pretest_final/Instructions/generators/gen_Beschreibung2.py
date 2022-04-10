from generators import HtmlGenerator as html

# INITS
title = 'Beschreibung der kommenden Entscheidungssituationen (2/2)'
filename = 'Beschreibung2'
url = f'../../Instructions/templates/Instructions/{filename}.html'
code = ''


# CONTENT
tables_per_block = '{% Constants.tables_per_block %}'
blocks = '{% Constants.blocks %}'
tables = '{% Constants.tables %}'
decisions = '{% Constants.decisions %}'

endowment_in_euro = '{% Constants.endowment_in_euro %}'
endowment_in_points = '{% Constants.endowment_in_points %}'
multiplier = '{% Constants.multiplier %}'

p4 = """
Ihre Entscheidungen, die Sie während des Experimentes treffen, bestimmen die Höhe Ihrer endgültigen Auszahlung:
"""
p4 = html.paragraph(p4)

ol1li1 = "Der Computer wählt eine Tabelle mit 50% Wahrscheinlichkeit aus einer Gewinnsituation und mit 50% Wahrscheinlichkeit aus einer Verlustsituation."
ol1li2 = f"In der ausgewählten Tabelle wählt der Computer zufällig eine der {decisions} Zeilen. Die Entscheidung, die Sie dort getroffen haben, wird dann <b>tatsächlich umgesetzt:</b>"
ul2li1 = "Haben Sie in dieser Zeile Option A gewählt, wird Option A umgesetzt."
ul2li2 = "Haben Sie in dieser Zeile Option B gewählt, wird Option B umgesetzt."
ol1li3 = f"Je nach Entscheidungstyp erhalten oder verlieren Sie eine bestimmte Anzahl an Punkten, wobei {multiplier} Punkte einem Betrag von 1 Euro entsprechen. Der entsprechende Euro-Betrag wird danach mit dem Grundbetrag in Höhe von {endowment_in_euro} Euro verrechnet."
ol1 = f"""
<ol>
    <li style="margin-top: 0rem">
        {ol1li1}
    </li>
    <li style="margin-top: 1rem">
        {ol1li2}
        <ul>
            <li style="margin-top: 0.25rem">
                {ul2li1}
            </li>
            <li style="margin-top: 0.25rem">
                {ul2li2}
            </li>
        </ul>
    </li>
    <li style="margin-top: 1rem">
        {ol1li3}
    </li>
</ol>
"""

p5 = """
Es liegt daher in Ihrem Interesse, jede Entscheidung <b>sorgfältig</b> zu treffen.
"""
p5 = html.paragraph(p5)


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
code = p4 + ol1 + p5 + div_next
html.code(title, code, url)

