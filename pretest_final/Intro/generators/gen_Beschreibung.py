from html_generator import HtmlGenerator as html

# INITS
title = 'Beschreibung der kommenden Situationen'
filename = '../templates/Intro/Beschreibung.html'
code = ''


# DYNAMIC
tables = '{{Constants.tables}}'
decisions_per_table = '{{Constants.decisions_per_table}}'


# STATIC
p1 = f"Sie sehen gleich nacheinander {tables} Tabellen mit jeweils {decisions_per_table} Zeilen. " \
     f"In jeder Zeile treffen Sie eine Entscheidung zwischen einer <b>Risikolotterie (Option A)</b> und einer <b>sicheren Auszahlung (Option B)</b>. " \
     f"Die Wahrscheinlichkeiten der Risikolotterie sind in den Tabellen angegeben."
p1 = html.paragraph(p1)

p2 = "Die Auszahlungen können positiv (Gewinnsituation) oder negativ (Verlustsituation) sein."
p2 = html.paragraph(p2)

li1 = "Bei positiven Auszahlungen erhalten Sie entweder einen Betrag mit einer gewissen Wahrscheinlichkeit (Option A) oder einen anderen Betrag mit Sicherheit (Option B)."
li2 = "Bei negativen Auszahlungen wird Ihnen entweder ein Betrag mit einer gewissen Wahrscheinlichkeit (Option A) abgezogen oder ein anderer Betrag mit Sicherheit (Option B) abgezogen. "

ul = f"""
<ul>
    <li style="margin-bottom: 1rem">
        {li1}
    </li>
    <li>
        {li2}
    </li>
</ul>
"""

p3 = "In jeder Entscheidungssituation sind Ihnen sämtliche relevanten Informationen angegeben."
p3 = html.paragraph(p3)

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um mit den Beispielaufgaben fortzufahren."
p_next = html.paragraph(p_next)


# OUTPUT
code = p1 + p2 + ul + p3 + p_next
html.code(title, code, filename)

