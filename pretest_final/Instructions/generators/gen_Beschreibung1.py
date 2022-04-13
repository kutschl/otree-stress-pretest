from generators import HtmlGenerator as html

# INITS
title = 'Beschreibung der kommenden Entscheidungssituationen'
filename = 'Beschreibung1'
url = f'../../Instructions/templates/Instructions/{filename}.html'


# CONTENT
p1 = f"""
In jeder der kommenden Situationen bekommen Sie eine Tabelle mit 21 Zeilen gezeigt. 
In jeder Zeile treffen Sie eine Entscheidung zwischen einer <b>Lotterie (Option A)</b> und einer <b>sicheren Auszahlung (Option B).</b>
"""
p1 = html.paragraph(p1)

p2 = f"""
Insgesamt zeigen wir Ihnen nacheinander 80 Tabellen. 
40 der Tabellen stellen eine <b>Gewinnsituation</b> mit positiven Punktgewinnen dar. 
Die anderen 40 Tabellen stellt eine <b>Verlustsituation</b> mit negativen Punktverlusten dar. 
"""
p2 = html.paragraph(p2)

ul1li1 = f'In den Tabellen, die Gewinnsituationen darstellen, können Sie Punkte zu Ihrem Basiskonto von 225 Punkten <b>dazuverdienen.</b>'
ul1li2 = f'In den Tabellen, die Verlustsituationen darstellen, können Sie einen Teil der 225 Punkte in Ihrem Basiskonto <b>verlieren.</b>'
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
In jeder Entscheidungssituation werden Ihnen sämtliche für Ihre Entscheidung relevanten Informationen angegeben. 
Im ersten sowie im zweiten Teil wird es jeweils 20 Gewinnsituationen und 20 Verlustsituationen geben. 
"""
p3 = html.paragraph(p3)


# NEXT BUTTON
p_next = "Bitte klicken Sie auf <em>Weiter</em>, um mit der Experimentbeschreibung fortzufahren."
p_next = html.paragraph(p_next)
button_next = html.next_button()
div_next = f"""
<div class="{'otree-next'}" id="{'otree-next'}">
    {p_next}
    {button_next}
</div>
"""


# OUTPUT
code = p1 + p2 + ul1 + p3 + div_next
html.code(title, code, url)

