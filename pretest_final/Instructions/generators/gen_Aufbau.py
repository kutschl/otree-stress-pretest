from generators import HtmlGenerator as html

# INITS
title = 'Aufbau'
filename = 'Aufbau'
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

p1 = f"""
Zu Beginn des Experimentes erhalten Sie <b>{endowment_in_euro} Euro</b> als Grundbetrag. 
Dies entspricht in diesem Experiment <b>{endowment_in_points} Punkten.</b> 
Ausgehend von den {endowment_in_points} Punkten können Sie Punkte dazuverdienen oder verlieren, 
wobei Ihre endgültige Punktanzahl von Ihren Entscheidungen und einer zufälligen Auslosung abhängt. 
Am Ende des Experiments werden die Punkte in Euro umgerechnet, 
wobei <b>jeweils {multiplier} Punkte einem Euro </b> entsprechen. 
Weitere Informationen erhalten Sie zu einem späteren Zeitpunkt.
"""
p1 = html.paragraph(p1)

p2 = """
Die Auswertung der Umfrage erfolgt pseudonymisiert. 
Das heißt, Ihre Antworten auf die folgenden Fragen werden <b>vollkommen getrennt von Ihren persönlichen Informationen</b> ausgewertet. 
Bitte antworten Sie daher so präzise wie möglich.
"""
p2 = html.paragraph(p2)

p3 = """
Das Experiment besteht aus <b>2 Abschnitten mit jeweils 40 zu treffenden Entscheidungen.</b> 
Diese Entscheidungen beeinflussen Ihre spätere Auszahlung. 
Zwischen diesen beiden Abschnitten, also nach Abschluss der ersten 40 Entscheidungen, werden Ihnen <b>16 weitere Fragen</b> gestellt. 
Diese beeinflussen Ihre Auszahlung nicht. 
Haben Sie diese beantwortet, geht es mit dem zweiten Abschnitt bestehend aus 40 Entscheidungen weiter. 
Diese beeinflussen Ihre Auszahlung dann wieder.
"""
p3 = html.paragraph(p3)

p4 = """
Sie bearbeiten die Umfrage unabhängig von den anderen Teilnehmern, können also <b>in Ihrem eigenen Tempo</b> arbeiten.
"""
p4 = html.paragraph(p4)


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
code = p1 + p2 + p3 + p4 + div_next
html.code(title, code, url)

