from html_generator import HtmlGenerator as html

# INITS
title = 'Beschreibung der kommenden Entscheidungssituationen (1/2)'
filename = 'Beschreibung1'
url = f'../../Instructions/templates/Instructions/{filename}.html'
code = ''


# DYNAMIC
tables_per_block = 40
blocks = 2
tables = tables_per_block*blocks
decision_per_table = 21

endowment = 15
multiplier = 15


# STATIC
p1 = f"""
In jeder der kommenden Situationen bekommen Sie eine Tabelle mit {decision_per_table} Zeilen gezeigt. 
In jeder Zeile treffen Sie eine Entscheidung zwischen einer <b>Lotterie (Option A)</b> und einer <b>sicheren Auszahlung (Option B).</b>
"""
p1 = html.paragraph(p1)


p2 = f"""
Insgesamt zeigen wir Ihnen nacheinander {tables} Tabellen. {tables_per_block} der Tabellen stellen eine <b>Gewinnsituation</b> mit positiven Punktgewinnen dar. 
Die anderen {tables_per_block} Tabellen stellt eine <b>Verlustsituation</b> mit negativen Punktverlusten dar.
"""
p2 = html.paragraph(p2)

ul1li1 = f'In den Tabellen, die Gewinnsituationen darstellen, können Sie Punkte zu Ihrem Basiskonto von {endowment*multiplier} Punkten <b>dazuverdienen.</b>'
ul1li2 = f'In den Tabellen, die Verlustsituationen darstellen, können Sie einen Teil der {endowment*multiplier} Punkte in Ihrem Basiskonto <b>verlieren.</b>'


ul1 = f"""
<ul>
    <li style="margin-top: -0.5rem">
        {ul1li1}
    </li>
    <li style="margin-top: 0.25rem">
        {ul1li2}
    </li>
</ul>
"""

p3 = """
In jeder Entscheidungssituation sind Ihnen sämtliche relevanten Informationen angegeben.
"""
p3 = html.paragraph(p3)


p_next = """
Bitte klicken Sie auf <em>Weiter</em>.
"""
p_next = html.paragraph(p_next)


# OUTPUT
code = p1 + p2 + ul1 + p3 + p_next
html.code(title, code, url)

