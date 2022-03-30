from html_generator import HtmlGenerator as html

# INITS
title = 'Willkommen'
filename = '../templates/Intro/Willkommen.html'
code = ''


# DYNAMIC
email = '{{Constants.contact.email}}'
a_email = html.link('mail', email, email)

phone = '{{Constants.contact.phone}}'
a_phone = html.link('phone', phone, phone)


# STATIC
p1 = """
    Herzlich Willkommen zur Online-Studie des BonnEconLab.
    Bitte beachten Sie, dass Sie an dieser Studie nur einmal teilnehmen dürfen.
    Außerdem dürfen Sie nur teilnehmen, wenn Sie sich in unserer Teilnahmedatenbank für diese Studie angemeldet haben.
"""
p1 = html.paragraph(p1)

p2 = """
    Sie erhalten die Aufwandsentschädigung nur, wenn Sie die komplette Umfrage ausfüllen.
    Sie werden dazu ungefähr 30 Minuten brauchen. Bitte bearbeiten Sie diese Umfrage am Computer.
    Eine Teilnahme mit mobilen Geräten wie Smartphones oder Tablets ist nicht möglich.
"""
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

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
p_next = html.paragraph(p_next)

# OUTPUT
code = p1 + p2 + p3 + ul + p_next
html.code(title, code, filename)

