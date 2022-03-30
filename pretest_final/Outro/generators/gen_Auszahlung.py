from html_generator import HtmlGenerator as html

# INITS
title = 'Vielen Dank für Ihre Teilnahme an der heutigen Studie!'
filename = '../templates/Outro/Auszahlung.html'
code = ''


# DYNAMIC
payoff = '{{player.payoff}}'
fix_payoff = '{{Constants.fix_payoff}}'
extra_payoff = None
extra_payoff_table = None
extra_payoff_decision = None
extra_payoff_option_a = None
extra_payoff_option_b = None
extra_payoff_choice = None

mail = '{{Constants.contact.email}}'


# STATIC
p1 = f"Sie haben in diesem Experiment insgesamt {payoff} verdient:"
p1 = html.paragraph(p1)

li1_h = f"fixer Auszahlungsbetrag:"
li1_t = f"{fix_payoff} als garantierte Auszahlung"

li2_h = f"zusätzlicher Auszahlungsbetrag:"
li2_t = f"{extra_payoff} aus einer zufällig ausgewählten Zeile in einer zufällig ausgewählten Entscheidungstabelle:"

li2li1 = f"Entscheidungstabelle {extra_payoff_table} wurde zufällig ausgewählt"
li2li2 = f"Zeile {extra_payoff_decision} wurde zufällig ausgewählt. Sie konnten sich hier zwischen {extra_payoff_option_a} und {extra_payoff_option_b} entscheiden."
li2li3 = f"Sie haben sich für {extra_payoff_choice} entschieden."

ol = f"""
<ol>
    <li style="margin-bottom: 1rem">
        {li1_h}
        <br>
        {li1_t}
    </li>
    <li style="margin-bottom: 1rem">
        {li2_h}
        <br>
        {li2_t}
        <ul>
            <li style="margin-top: 0.25rem">
                {li2li1}
            </li>
            <li style="margin-top: 0.125rem">
                {li2li2}
            </li>
            <li style="margin-top: 0.125rem">
                {li2li3}
            </li>
        </ul>
    </li>
</ol>
"""


a1 = html.link("mail", mail, mail)

p2 = f"Sie erhalten Ihre Auszahlung innerhalb der nächsten Tage per Überweisung. " \
     f"Bitte kontaktieren Sie {a1}, falls Sie weitere Fragen zu dem Experiment oder Ihrer Überweisung haben sollten."
p2 = html.paragraph(p2)

p3 = f"Vielen Dank für Ihre Teilnahme am Experiment! Sie können das Browserfenster nun schließen."
p3 = html.paragraph(p3)


# OUTPUT
code = p1 + ol + p2 + p3
html.code(title, code, filename)

