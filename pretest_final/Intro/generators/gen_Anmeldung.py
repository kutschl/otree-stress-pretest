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

f_vorname = "{% formfield player.VORNAME %}"
f_nachname = "{% formfield player.NACHNAME %}"
f_strasse = "{% formfield player.STRASSE %}"
f_plz = "{% formfield player.PLZ %}"
f_stadt = "{% formfield player.STADT %}"
f_email = "{% formfield player.EMAIL %}"
f_iban = "{% formfield player.IBAN %}"
f_bic = "{% formfield player.BIC %}"
form = f"""
{f_vorname}
{f_nachname}
{f_strasse}
{f_plz}
{f_stadt}
{f_email}
{f_iban}
{f_bic}
"""

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

