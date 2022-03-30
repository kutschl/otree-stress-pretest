from html_generator import HtmlGenerator as html

# INITS
title = 'Experimentstart'
filename = '../templates/Intro/Experimentstart.html'
code = ''


# DYNAMIC


# STATIC
p1 = "XXX."
p1 = html.paragraph(p1)

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um das Experiment zu starten."
p_next = html.paragraph(p_next)

# OUTPUT
code = p1 + p_next
html.code(title, code, filename)

