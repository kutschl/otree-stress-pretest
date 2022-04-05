from html_generator import HtmlGenerator as html

# INITS
title = 'Persönliche Informationen'
filename = '../templates/Intro/Anmeldung.html'
code = ''


# DYNAMIC
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
f1 = ''
for i in fields:
    label = '{{form.' + i[0] + '.label}}'
    f1 = f1 + html.paragraph(html.label(i[0], label) + html.input(i[1], i[0]))


# STATIC
p1 = """
    Vielen Dank, dass Sie an dieser Umfrage teilnehmen.
    Die Umfrage wird ungefähr eine halbe Stunde Ihrer Zeit in Anspruch nehmen.
    Wenn Sie die Umfrage beendet haben, wird Ihnen eine Aufwandsentschädigung überwiesen.
    Um die Überweisung ausführen zu können, benötigen wir die folgenden Informationen von Ihnen.
    Diese Informationen werden <b> nur für die Abwicklung der Zahlung </b> verwendet
    und vor der Datenauswertung von dem restlichen Datensatz getrennt.
"""
p1 = html.paragraph(p1)

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
p_next = html.paragraph(p_next)

# OUTPUT
code = p1 + f1 + p_next
html.code(title, code, filename)
