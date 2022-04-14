from generators import HtmlGenerator as html
from lotteries_loader import LotteryLoader as lot
import numpy as np

data_gain = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'GAIN'
)
data_loss = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'LOSS'
)

javascript_autofill = open('gen_BlockTabelle_autofill.js').read()
css_table = open('gen_BlockTabelle_table.css').read()


gain_tables_per_block = len(data_gain[list(data_gain.keys())[0]])
loss_tables_per_block = len(data_loss[list(data_loss.keys())[0]])
tables_per_block = gain_tables_per_block + loss_tables_per_block
blocks = 2
tables = blocks * tables_per_block
decisions_per_table = 21


def codeModelsTabellenForms():
    code = ''
    for block in np.arange(1, blocks + 1, 1):
        for gain_table in np.arange(1, gain_tables_per_block + 1, 1):
            code = code + f"'B{block}_GAIN{gain_table}': getTable({block}, {gain_table}, 'GAIN'),\n"
        code = code + '\n\n'
        for loss_table in np.arange(1, gain_tables_per_block + 1, 1):
            code = code + f"'B{block}_LOSS{loss_table}': getTable({block}, {loss_table}, 'LOSS'),\n"
        code = code + '\n\n'
    return print(code)
# codeModelsTabellenForms()


def codeModelsTabellenFields():
    code = ''
    for block in np.arange(1, blocks + 1, 1):
        for gain_table in np.arange(1, gain_tables_per_block + 1, 1):
            code = code + f'# BLOCK {block} GEWINN TABELLE {gain_table}\n'
            for decision in np.arange(1, decisions_per_table + 1, 1):
                code = code + f'B{block}_GAIN{gain_table}_D{decision} = TableField("B{block}_GAIN{gain_table}", {decision})\n'
            code = code + '\n'
        for loss_table in np.arange(1, loss_tables_per_block + 1, 1):
            code = code + f'# BLOCK {block} VERLUST TABELLE {loss_table}\n'
            for decision in np.arange(1, decisions_per_table + 1, 1):
                code = code + f'B{block}_LOSS{loss_table}_D{decision} = TableField("B{block}_LOSS{loss_table}", {decision})\n'
            code = code + '\n'
    return print(code)
# codeModelsTabellenFields()


def codeB3RowsHtml(b, t, a):
    code = ''
    for decision in np.arange(1, decisions_per_table + 1, 1):
        code = code + f'<tr class="dtable-b3-tr"><td>A</td><td>{{%form.B{b}_{a}{t}_D{decision}.0%}}</td><td>{{%form.B{b}_{a}{t}_D{decision}.1%}}</td><td>B</td></tr>\n'
    return code


def codeHtml(b, t, a):
    # INITS
    title = ''
    filename = ''
    if a == 'GAIN':
        title = f'Block {b} Gewinnsituation {t}'
        filename = f'../templates/Game/Block{b}GewinnTabelle{t}.html'
    if a == 'LOSS':
        title = f'Block {b} Verlustsituation {t}'
        filename = f'../templates/Game/Block{b}VerlustTabelle{t}.html'
    code = ''

    # DYNAMIC
    dtable_b1_title = ''
    dtable_b2_title = 'Option A: <br/> Risikolotterie'
    dtable_b3_title = 'Ihre Entscheidung'
    dtable_b4_title = 'Option B: <br/> Sichere Auszahlung'
    Number = f'Constants.forms_tabellen.B{b}_{a}{t}.Number'
    Numbering = f'Constants.forms_tabellen.B{b}_{a}{t}.Numbering'
    #todo use Typ and Number maybe?
    Typ = f'Constants.forms_tabellen.B{b}_{a}{t}.Typ'
    p1 = f'Constants.forms_tabellen.B{b}_{a}{t}.A.p1'
    p2 = f'Constants.forms_tabellen.B{b}_{a}{t}.A.p2'
    x1 = f'Constants.forms_tabellen.B{b}_{a}{t}.A.x1'
    x2 = f'Constants.forms_tabellen.B{b}_{a}{t}.A.x2'
    B = f'Constants.forms_tabellen.B{b}_{a}{t}.B'
    ASC = f'Constants.forms_tabellen.B{b}_{a}{t}.ASC'

    # STATIC
    dtable_b1 = f"""
    <!--Tabelle B1: Nummerierung-->
    <table class="dtable-b1">
      <tr class="dtable-b1-tr1">
        <td>
          <span>{dtable_b1_title}</span>
        </td>
      </tr>
      {{% for i in {Numbering}%}}
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">{{% i %}}</span>
        </th>
      </tr>
      {{% endfor %}}
    </table>
    """

    dtable_b2 = f"""
    <!--Tabelle B2: Option A-->
    <table class="dtable-b2">
      <tr class="dtable-b2-tr1">
        <td>
          <span>{dtable_b2_title}</span>
        </td>
      </tr>
      <tr class="dtable-b2-tr">
        <td>
          <div>
            <p>Auszahlung von {{%{x1}%}}</p>
            <p>mit Wahrscheinlichkeit {{%{p1}%}}</p>
            <p>und Auszahlung von {{%{x2}%}}</p>
            <p>mit Wahrscheinlichkeit {{%{p2}%}}</p>
          </div>
        </td>
      </tr>
    </table>
    """

    dtable_b3_rows = codeB3RowsHtml(b, t, a)

    dtable_b3 = f"""
    <!--Tabelle B3: Entscheidung-->
    <table class="dtable-b3">
      <tr class="dtable-b3-tr1">
        <td colspan="4">
          <span>{dtable_b3_title}</span>
        </td>
      </tr>
      {dtable_b3_rows}
    </table>
    """

    dtable_b4 = f"""
    <!--Tabelle B4: Option B-->
    <table class="dtable-b4" id="ASC" name="{{%{ASC}%}}">
      <tr class="dtable-b4-tr1">
        <td>
          <span>{dtable_b4_title}</span>
        </td>
      </tr>
      {{% for i in {B} %}}
      <tr class="dtable-b4-tr">
        <td>
          <span>{{% i %}}</span>
        </td>
      </tr>
      {{% endfor %}}
    </table>
    """

    dtable_b = f"""
    <div class="dtable-b">
        {dtable_b1}
        {dtable_b2}
        {dtable_b3}
        {dtable_b4}
    </div>
    """

    # dtable_h = f"""
    # <div class="dtable-h">
    #     <span>
    #         Entscheidungssituation: {{% {Number} %}}
    #     </span>
    # </div>
    # """

    dtable = f"""
    <div class="dtable">
    {dtable_b}
    </div>
    """

    style = html.style(css_table)
    script = html.script(javascript_autofill)

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
    code = style + dtable + script + div_next
    html.code(title, code, filename)
for block in np.arange(1, blocks + 1, 1):
    for gain_table in np.arange(1, gain_tables_per_block + 1, 1):
        codeHtml(block, gain_table, 'GAIN')
    for loss_table in np.arange(1, loss_tables_per_block + 1, 1):
        codeHtml(block, loss_table, 'LOSS')
