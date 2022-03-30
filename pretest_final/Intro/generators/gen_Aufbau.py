from html_generator import HtmlGenerator as html

# INITS
title = 'Aufbau'
filename = '../templates/Intro/Aufbau.html'
code = ''


# DYNAMIC
fix_payoff = '{{Constants.fix_payoff}}'
extra_payoff_lower_limit = '{{Constants.extra_payoff_lower_limit}}'
extra_payoff_upper_limit = '{{Constants.extra_payoff_upper_limit}}'


# STATIC
p1 = "Die Aufwandsentschädigung für Ihre Teilnahme besteht aus zwei Teilen:"
p1 = html.paragraph(p1)

li1_h = "Fixe Auszahlung:"
li1_t = f"Sie erhalten eine garantierte Auszahlung in Höhe von {fix_payoff}."

li2_h = "Variable Auszahlung:"
li2_t = f"Sie können sich zusätzlich einen Betrag zwischen {extra_payoff_lower_limit} und {extra_payoff_upper_limit} dazu verdienen, " \
        "wobei die Verdiensthöhe von Ihren Entscheidungen und einer zufälligen Auslosung abhängt. " \
        "Weitere Informationen erhalten Sie zu einem späteren Zeitpunkt."

ol = f"""
<ol>
    <li style="margin-bottom: 1rem">
        {li1_h}
        <br>
        {li1_t}
    </li>
    <li>
        {li2_h}
        <br>
        {li2_t}
    </li>
</ol>
"""

p2 = "Die Auswertung der Umfrage erfolgt pseudonymisiert. " \
     "Das heißt, Ihre Antworten auf die folgenden Fragen werden vollkommen getrennt von Ihren persönlichen Informationen ausgewertet. " \
     "Bitte antworten Sie daher so präzise wie möglich. "
p2 = html.paragraph(p2)


p3 = "Sie bearbeiten die Umfrage unabhängig von den anderen Teilnehmern, können also in Ihrem eigenen Tempo arbeiten."
p3 = html.paragraph(p3)

p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um mit der Experimentbeschreibung fortzufahren."
p_next = html.paragraph(p_next)


# OUTPUT
code = p1 + ol + p2 + p3 + p_next
html.code(title, code, filename)

