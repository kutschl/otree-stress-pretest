from html_generator import HtmlGenerator as html

# INITS
title = 'Demographische Angaben'
filename = 'DemographischeAngaben'
url = f'../templates/AfterGame/{filename}.html'
code = ''


# CONTENT
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
code = p1 + f1 + f2 + f3 + div_next
html.code(title, code, url)

