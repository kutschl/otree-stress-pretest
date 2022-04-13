from generators import HtmlGenerator as html
import numpy as np

# INITS
title = 'Persönliche Informationen'
filename = 'Anmeldung'
url = f'../templates/Intro/{filename}.html'


# CONTENT
p = """
Vielen Dank, dass Sie an dieser Umfrage teilnehmen. 
Wenn Sie die Umfrage beendet haben, wird Ihnen eine Aufwandsentschädigung überwiesen. 
Um die Überweisung ausführen zu können, benötigen wir die folgenden Informationen von Ihnen. 
Diese Informationen werden <b>nur für die Abwicklung</b> der Zahlung verwendet und vor der Datenauswertung von dem restlichen Datensatz getrennt.
"""
p = html.paragraph(p)

fields = [
    ['VORNAME', 'text'],
    ['NACHNAME', 'text'],
    ['STRASSE', 'text'],
    ['PLZ', 'number'],
    ['STADT', 'text'],
    ['EMAIL', 'email'],
    ['IBAN', 'text'],
    ['BIC', 'text']
]

form = ''
for field in fields:
    form = form + f"""
<p>
    {{% form.{field[0]}.label %}}
    <input type="{field[1]}" class="form-control" name="{field[0]}" id="{field[0]}"/>
    {{% formfield_errors '{field[0]}' %}}
</p>
    """


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
code = p + form + div_next
html.code(title, code, url)

