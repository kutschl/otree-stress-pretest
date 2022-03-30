from html_generator import HtmlGenerator as html

# INITS
title = 'Berechnung der Auszahlung'
filename = '../templates/Intro/Auszahlung.html'
code = ''


# DYNAMIC
tables = '{{Constants.tables}}'
decisions_per_table = '{{Constants.decisions_per_table}}'
fix_payoff = '{{Constants.fix_payoff}}'
example_points = '{{Constants.example_points}}'
example_payoff = '{{Constants.example_payoff}}'


# STATIC
p1 = "Ihre Entscheidungen, die Sie während des Experimentes treffen, bestimmen den variablen Teil ihrer Auszahlung:"
p1 = html.paragraph(p1)

li1 = f"Zunächst wird eine der {tables} Tabellen zufällig vom Computer ausgewählt."
li2 = f"In der ausgewählten Tabelle wird eine der {decisions_per_table} Zeilen zufällig vom Computer ausgewählt. " \
      f"Die Entscheidung, die Sie dort getroffen haben, wird tatsächlich umgesetzt:"

li2li1 = "Haben Sie in dieser Zeile Option A gewählt, wird Option A umgesetzt."
li2li2 = "o	Haben Sie in dieser Zeile Option B gewählt, wird Option B umgesetzt." \

li3 = f"Sie erhalten so eine bestimmte Anzahl an Punkten, wobei {example_points} Punkte einer Auszahlung von {example_payoff} entsprechen. " \
      f"Der entsprechende Euro-Betrag wird zu dem fixen Auszahlungsbetrag in Höhe von {fix_payoff} hinzugefügt."

ol = f"""
<ol>
    <li style="margin-bottom: 1rem">
        {li1}
    </li>
    <li style="margin-bottom: 1rem">
        {li2}
        <ul>
            <li style="margin-top: 0.25rem">
                {li2li1}
            </li>
            <li style="margin-top: 0.125rem">
                {li2li2}
            </li>
        </ul>
    </li>
    <li>
        {li3}
    </li>
</ol>
"""

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
p_next = html.paragraph(p_next)

# OUTPUT
code = p1 + ol + p_next
html.code(title, code, filename)

