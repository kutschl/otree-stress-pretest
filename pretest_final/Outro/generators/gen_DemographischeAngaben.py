from html_generator import HtmlGenerator as html


# INITS
title = 'Demographische Angaben'
filename = '../templates/Outro/DemographischeAngaben.html'
code = ''


# DYNAMIC


# STATIC
p1 = "Bitte beantworten Sie die folgenden Fragen."
p1 = html.paragraph(p1)

f1 = '{% formfield player.GENDER %}'
f1 = html.paragraph(f1)

f2 = '{% formfield player.ALTER %}'
f2 = html.paragraph(f2)

f3 = '{% formfield player.JOB %}'
f3 = html.paragraph(f3)

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
p_next = html.paragraph(p_next)


# OUTPUT
code = p1 + f1 + f2 + f3 + p_next
html.code(title, code, filename)

