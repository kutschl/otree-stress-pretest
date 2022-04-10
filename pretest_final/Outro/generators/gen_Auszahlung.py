from generators import HtmlGenerator as html

# INITS
title = 'Vielen Dank für Ihre Teilnahme an der heutigen Studie!'
filename = '../templates/Outro/Auszahlung.html'
code = ''

# DYNAMIC
endowment = '{{participant.vars.endowment}}'
payoff = '{{participant.vars.payoff}}'
payoff_rd_typ = '{{participant.vars.payoff_rd_typ}}'
payoff_rd_block = '{{participant.vars.payoff_rd_block}}'
payoff_rd_decision = '{{participant.vars.payoff_rd_decision}}'
payoff_player_decision = '{{participant.vars.payoff_player_decision}}'

mail = 'schulzetilling@uni-bonn.de'


# STATIC
p1 = f"Endowment: {endowment}, Payoff: {payoff}, Typ: {payoff_rd_typ}, Block: {payoff_rd_block}, Entscheidung: {payoff_rd_decision}, Ihre Entscheidung: {payoff_player_decision}"
p1 = html.paragraph(p1)

a1 = html.link("mail", mail, mail)

p2 = f"Sie erhalten Ihre Auszahlung innerhalb der nächsten Tage per Überweisung. " \
     f"Bitte kontaktieren Sie {a1}, falls Sie weitere Fragen zu dem Experiment oder Ihrer Überweisung haben sollten."
p2 = html.paragraph(p2)

p3 = f"Vielen Dank für Ihre Teilnahme am Experiment! Sie können das Browserfenster nun schließen."
p3 = html.paragraph(p3)


# OUTPUT
code = p1 + p2 + p3
html.code(title, code, filename)

