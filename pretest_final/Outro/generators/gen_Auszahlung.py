from generators import HtmlGenerator as html

# INITS
title = 'Vielen Dank für Ihre Teilnahme an der heutigen Studie!'
filename = 'Auszahlung'
url = f'../templates/Outro/{filename}.html'
# -------------------------------------------------------


# CONTENT
endowment = 'participant.vars.endowment'
payoff = 'participant.vars.payoff'
payoff_rd_typ = 'participant.vars.payoff_rd_typ'
payoff_rd_block = 'participant.vars.payoff_rd_block'
payoff_rd_table = 'participant.vars.payoff_rd_table'
payoff_rd_decision = 'participant.vars.payoff_rd_decision'
payoff_player_decision = 'participant.vars.payoff_player_decision'
p_payoff = f"""
Sie erhalten eine <b>Auszahlung in Höhe von {{%{payoff}%}}.</b>
"""
p_payoff = html.paragraph(p_payoff)
# -------------------------------------------------------
p_payoff_details = f"""
Die für Ihre Auszahlung relevante Entscheidung war die folgende: 
"""
p_payoff_details = html.paragraph(p_payoff_details)
# -------------------------------------------------------
li_payoff_details = f"""
<ul style="margin-top: -0.5rem">
     <li style="margin-bottom: 0.25rem">
          Teil: 
          {{%{payoff_rd_block}%}}
     </li>
     <li style="margin-bottom: 0.25rem">
          Tabelle:
          {{% if {payoff_rd_typ} == 'GAIN'%}}
          Gewinnsituation
          {{% endif %}}
          {{% if {payoff_rd_typ} == 'LOSS'%}}
          Verlustsituation
          {{% endif %}}
          {{%{payoff_rd_table}%}}
     </li>
     <li style="margin-bottom: 0.25rem">
          Zeile:
          {{%{payoff_rd_decision}%}}
     </li>
     <li style="margin-bottom: 0.25rem">
          Ihre Entscheidung: 
          
          {{% if {payoff_player_decision} == 1%}}
          Lotterie (Option A)
          {{% endif %}}
          
          {{% if {payoff_player_decision} == 2%}}
              {{% if {payoff_rd_typ} == 'GAIN'%}}
              Sichere Auszahlung (Option B)
              {{% endif %}}
              {{% if {payoff_rd_typ} == 'LOSS'%}}
              Sicherer Verlust (Option B)
              {{% endif %}}
          {{% endif %}}
     </li>
</ul>
"""
# -------------------------------------------------------
mail_info = 'schulzetilling@uni-bonn.de'
mail_info = html.link("mail", mail_info, mail_info)
p_info = f"""
Sie erhalten Ihre Auszahlung innerhalb der nächsten Wochen per Überweisung. 
Bitte kontaktieren Sie {mail_info}, falls Sie weitere Fragen zu dem Experiment oder Ihrer Überweisung haben sollten. 
"""
p_info = html.paragraph(p_info)
# -------------------------------------------------------
p_close = f"""
Vielen Dank für Ihre Teilnahme am Experiment! Sie können das Browserfenster nun schließen. 
"""
p_close = html.paragraph(p_close)
# -------------------------------------------------------


# OUTPUT
code = p_payoff + p_payoff_details + li_payoff_details + p_info + p_close
html.code(title, code, url)

