from html_generator import HtmlGenerator as html

# INITS
title = 'Willkommen'
filename = 'Willkommen'
url = f'../templates/Intro/{filename}.html'
code = ''


# CONTENT
email = "schulzetilling@uni-bonn.de"
a_email = html.link('mail', email, email)
phone = "0176 86963663"
a_phone = html.link('phone', phone, phone)


p1 = """
Herzlich Willkommen zur Online-Studie des BonnEconLab. 
Bitte beachten Sie, dass Sie an dieser Studie <b>nur einmal teilnehmen dürfen.</b> 
Außerdem dürfen Sie nur teilnehmen, wenn Sie sich in unserer Teilnahmedatenbank für diese Studie angemeldet haben.
"""
p1 = html.paragraph(p1)

p2 = """
Sie erhalten die Aufwandsentschädigung nur, <b>wenn Sie die komplette Umfrage ausfüllen.</b> 
Sie werden dazu <b>ungefähr 30 Minuten</b> brauchen. 
Bitte bearbeiten Sie diese Umfrage <b>am Computer.</b> 
Eine Teilnahme mit mobilen Geräten wie Smartphones oder Tablets ist <b>nicht</b> möglich."""
p2 = html.paragraph(p2)

p3 = """
Sollten Sie während des Experiments Fragen haben, können Sie jederzeit die Experimentleiterin kontaktieren:
"""
p3 = html.paragraph(p3)

ul = f"""
<ul>
    <li>
        per Telefonnummer: {a_phone}
    </li>
    <li>
        per E-Mail: {a_email}
    </li>
</ul>
"""


# NOSCRIPT
noscript = """
<noscript>
    <div class="alert alert-danger" role="alert">
        Zur Teilnahme an dieser Studie wird <em>JavaScript</em> benötigt, welches in Ihrem Browser leider deaktiviert ist.
        Bitte aktivieren Sie deshalb JavaScript und laden Sie erneut diese Seite
        oder öffnen Sie Ihren persönlichen Link in einem anderen Browser / auf einem anderen Gerät.
    </div>
</noscript>
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
code = p1 + p2 + p3 + ul + noscript + div_next
html.code(title, code, url)

