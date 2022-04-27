from generators import HtmlGenerator as html

# INITS
title = 'Vielen Dank für Ihre Teilnahme an der heutigen Studie!'
filename = 'Auszahlung'
url = f'../templates/Outro/{filename}.html'
# -------------------------------------------------------


# CONTENT
payoff = 'participant.vars.payoff'
payoff_table_type = 'participant.vars.payoff_table_type'
payoff_rd_block = 'participant.vars.payoff_random_block'
payoff_rd_table = 'participant.vars.payoff_random_table'
payoff_rd_decision = 'participant.vars.payoff_random_decision'
payoff_player_option = 'participant.vars.payoff_player_option'
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
          {{% if {payoff_table_type} == 0 %}}
          Gewinnsituation
          {{% endif %}}
          {{% if {payoff_table_type} == 1 %}}
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
          
          {{% if {payoff_player_option} == 0 %}}
          Lotterie (Option A)
          {{% endif %}}
          
          {{% if {payoff_player_option} == 1 %}}
              {{% if {payoff_table_type} == 0 %}}
              Sichere Auszahlung (Option B)
              {{% endif %}}
              {{% if {payoff_table_type} == 1 %}}
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

