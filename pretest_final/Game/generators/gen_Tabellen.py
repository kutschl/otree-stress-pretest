from html_generator import HtmlGenerator as html
from lotteries_loader import LotteryLoader as lot
import numpy as np

data_gain = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'GAIN'
)
data_loss = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'LOSS'
)

javascript_autofill = open('gen_Tabelle_autofill.js').read()
css_table = open('gen_Tabelle_table.css').read()


tables_per_block = len(data_gain[list(data_gain.keys())[0]]) + len(data_loss[list(data_loss.keys())[0]])
blocks = 2
tables = blocks * tables_per_block
decisions_per_table = 21


# CODE: pages.py.Tabelle{i}(Page)
def codePagesTabellePage():
    code = ''
    sequence = ''
    for block in np.arange(1, blocks+1, 1):
        for table in np.arange(1, tables_per_block + 1, 1):
            sequence = sequence + f'Block{block}Tabelle{table}, '
            model = "player"
            fields = ''
            for decision in np.arange(1, decisions_per_table + 1, 1):
                fields = fields + f"'B{block}_T{table}_D{decision}', "
            form_model = f"form_model = '{model}'"
            form_fields = f"form_fields = [{fields}]"
            page = f"""
            class Block{block}Tabelle{table}(Page):
                {form_model}
                {form_fields}
                
            """
            code = code + page
    page_sequence = f'page_sequence = [{sequence}]'
    code = code + page_sequence
    return print(code)
# codePagesTabellePage()


# CODE: models.py.Constants.forms
def codeModelsConstantsForms():
    code = ''
    for block in np.arange(1, blocks + 1, 1):
        for table in np.arange(1, tables_per_block + 1, 1):
            code = code + f"'B{block}_T{table}': getTable({block}, {table}),\n"
        code = code + '\n\n'
    return print(code)
# codeModelsConstantsForms()


# CODE: models.py.Player.IntegerFields
def codeModelsPlayerIntegerFields():
    code = ''
    for block in np.arange(1, blocks + 1, 1):
        for table in np.arange(1, tables_per_block + 1, 1):
            code = code + f'# Block {block} Tabelle {table}\n'
            for decision in np.arange(1, decisions_per_table + 1, 1):
                code = code + f'B{block}_T{table}_D{decision} = IntegerField("B{block}_T{table}", {decision})\n'
            code = code + '\n'
    return print(code)
# codeModelsPlayerIntegerFields()


# CODE: template/Tabelle{i}.html/dtable_b3_rows
def codeB3RowsHtml(block, table):
    code = ''
    for decision in np.arange(1, decisions_per_table + 1, 1):
        code = code + f'<tr class="dtable-b3-tr"><td>A</td><td>{{%form.B{block}_T{table}_D{decision}.0%}}</td><td>{{%form.B{block}_T{table}_D{decision}.1%}}</td><td>B</td></tr>\n'
    return code


# CODE: templates/Tabelle{i}.html
def codeTabelleHtml(b, t):
    # INITS
    title = f'Entscheidungssituation'
    filename = f'../templates/Game/Block{b}Tabelle{t}.html'
    code = ''

    # DYNAMIC
    dtable_b1_title = ''
    dtable_b2_title = 'Option A: <br/> Risikolotterie'
    dtable_b3_title = 'Ihre Entscheidung'
    dtable_b4_title = 'Option B: <br/> Sichere Auszahlung'
    Number = f'Constants.forms.B{b}_T{t}.Number'
    Numbering = f'Constants.forms.B{b}_T{t}.Numbering'
    p1 = f'Constants.forms.B{b}_T{t}.A.p1'
    p2 = f'Constants.forms.B{b}_T{t}.A.p2'
    x1 = f'Constants.forms.B{b}_T{t}.A.x1'
    x2 = f'Constants.forms.B{b}_T{t}.A.x2'
    B = f'Constants.forms.B{b}_T{t}.B'
    ASC = f'Constants.forms.B{b}_T{t}.ASC'

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

    dtable_b3_rows = codeB3RowsHtml(b, t)

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

    dtable_h = f"""
    <div class="dtable-h">
        <span>
            Entscheidungssituation: {{% {Number} %}}
        </span>
    </div>
    """

    dtable = f"""
    <div class="dtable">
    {dtable_h}
    {dtable_b}
    </div>
    """

    style = html.style(css_table)
    script = html.script(javascript_autofill)

    p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
    p_next = html.paragraph(p_next)

    # OUTPUT
    code = style + dtable + script + p_next
    html.code(title, code, filename)
for block in np.arange(1, blocks + 1, 1):
    for table in np.arange(1, tables_per_block + 1, 1):
        codeTabelleHtml(block, table)
