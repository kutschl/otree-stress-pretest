from generators import HtmlGenerator as html

# INITS
title = 'Beispielaufgaben'
filename = '../templates/Comprehension/Beispielaufgaben.html'
code = ''


# DYNAMIC
tables = '{{Constants.tables}}'
decisions_per_table = '{{Constants.decisions_per_table}}'


# STATIC
p1 = "Die folgenden zwei Beispiele zeigen Ihnen, wie die beiden Entscheidungstypen funktionieren. Sie sehen zunächst eine Gewinnsituation und anschließend eine Verlustsituation, um sich mit den Entscheidungstypen vertraut zu machen."
p1 = html.paragraph(p1)


p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
p_next = html.paragraph(p_next)


# OUTPUT
code = p1 + p_next
html.code(title, code, filename)

