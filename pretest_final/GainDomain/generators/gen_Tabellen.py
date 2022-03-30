from html_generator import HtmlGenerator as html
from lotteries_loader import LotteryLoader as lot
import numpy as np

data = lot.load('C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls',
                'gain')

javascript_autofill = open('gen_Tabelle_autofill.js').read()
css_table = open('gen_Tabelle_table.css').read()

tables = len(data['p'])
decisions_per_table = 21


# CODE: pages.py.Tabelle{i}(Page)
def codePagesTabellePage():
    code = ''
    sequence = ''
    for table in np.arange(1, tables+1, 1):
        sequence = sequence + f'Tabelle{table}, '
        model = "player"
        fields = ''
        for decision in np.arange(1, decisions_per_table+1, 1):
            fields = fields + f"'D{table}_{decision}', "
        form_model = f"form_model = '{model}'"
        form_fields = f"form_fields = [{fields}]"
        page = f"""
        class Tabelle{table}(Page):
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
    for i in np.arange(1, tables + 1, 1):
        code = code + f"'D{i}': getDecision({i}),\n"
    return print(code)
# codeModelsConstantsForms()


# CODE: models.py.Player.IntegerFields
def codeModelsPlayerIntegerFields():
    code = ''
    for table in np.arange(1, tables+1, 1):
        code = code + f'# Decision {table}\n'
        for decision in np.arange(1, decisions_per_table+1, 1):
            code = code + f'D{table}_{decision} = IntegerField("D{table}", {decision})\n'
        code = code + '\n'
    return print(code)
# codeModelsPlayerIntegerFields()


# CODE: template/Tabelle{i}.html/dtable_b3_rows
def codeB3RowsHtml(table):
    code = ''
    for decision in np.arange(1, decisions_per_table+1, 1):
        code = code + f'<tr class="dtable-b3-tr"><td>A</td><td>{{%form.D{table}_{decision}.0%}}</td><td>{{%form.D{table}_{decision}.1%}}</td><td>B</td></tr>\n'
    return code


# CODE: templates/Tabelle{i}.html
def codeTabelleHtml(key):
    # INITS
    title = f'Entscheidungssituation {key}'
    filename = f'../templates/GainDomain/Tabelle{key}.html'
    code = ''

    # DYNAMIC
    dtable_b1_title = ''
    dtable_b2_title = 'Option A: <br/> Risikolotterie'
    dtable_b3_title = 'Ihre Entscheidung'
    dtable_b4_title = 'Option B: <br/> Sichere Auszahlung'
    Number = f'Constants.forms.D{key}.Number'
    Numbering = f'Constants.forms.D{key}.Numbering'
    p1 = f'Constants.forms.D{key}.A.p1'
    p2 = f'Constants.forms.D{key}.A.p2'
    x1 = f'Constants.forms.D{key}.A.x1'
    x2 = f'Constants.forms.D{key}.A.x2'
    B = f'Constants.forms.D{key}.B'


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

    dtable_b3_rows = codeB3RowsHtml(key)


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
    <table class="dtable-b4">
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



    """
<div class="dtable">
  <div class="dtable-h">
    <span>
      Entscheidungssituation: {{Constants.forms.D1.Number}}
    </span>
  </div>
  <div class="dtable-b">

    <!--Tabelle B1: Nummerierung-->
    <table class="dtable-b1">
      <tr class="dtable-b1-tr1">
        <td>
          <span></span>
        </td>
      </tr>
      {{for i in Constants.forms.D1.Numbering}}
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">{{i}}</span>
        </th>
      </tr>
      {{endfor}}
    </table>

    <!--Tabelle B2: Option A-->
    <table class="dtable-b2">
      <tr class="dtable-b2-tr1">
        <td>
          <span>Option A: <br/> Risikolotterie</span>
        </td>
      </tr>
      <tr class="dtable-b2-tr">
        <td>
          <div>
            <p>Auszahlung von {{Constants.forms.D1.A.x1}}</p>
            <p>mit Wahrscheinlichkeit {{Constants.forms.D1.A.p1}}</p>
            <p>und Auszahlung von {{Constants.forms.D1.A.x2}}</p>
            <p>mit Wahrscheinlichkeit {{Constants.forms.D1.A.p2}}</p>
          </div>
        </td>
      </tr>
    </table>

    <!--Tabelle B3: Entscheidung-->
    <table class="dtable-b3">
      <tr class="dtable-b3-tr1">
        <td colspan="4">
          <span>Ihre Entscheidung</span>
        </td>
      </tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_1.0}}</td><td>{{form.D1_1.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_2.0}}</td><td>{{form.D1_2.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_3.0}}</td><td>{{form.D1_3.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_4.0}}</td><td>{{form.D1_4.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_5.0}}</td><td>{{form.D1_5.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_6.0}}</td><td>{{form.D1_6.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_7.0}}</td><td>{{form.D1_7.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_8.0}}</td><td>{{form.D1_8.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_9.0}}</td><td>{{form.D1_9.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_10.0}}</td><td>{{form.D1_10.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_11.0}}</td><td>{{form.D1_11.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_12.0}}</td><td>{{form.D1_12.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_13.0}}</td><td>{{form.D1_13.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_14.0}}</td><td>{{form.D1_14.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_15.0}}</td><td>{{form.D1_15.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_16.0}}</td><td>{{form.D1_16.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_17.0}}</td><td>{{form.D1_17.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_18.0}}</td><td>{{form.D1_18.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_19.0}}</td><td>{{form.D1_19.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_20.0}}</td><td>{{form.D1_20.1}}</td><td>B</td></tr>
      <tr class="dtable-b3-tr"><td>A</td><td>{{form.D1_21.0}}</td><td>{{form.D1_21.1}}</td><td>B</td></tr>    </table>

    <!--Tabelle B4: Option B-->
    <table class="dtable-b4">
      <tr class="dtable-b4-tr1">
        <td>
          <span>Option B: <br/> Sichere Auszahlung</span>
        </td>
      </tr>
      {{for i in Constants.forms.D1.B}}
      <tr class="dtable-b4-tr">
        <td>
          <span>{{i}}</span>
        </td>
      </tr>
      {{endfor}}
    </table>
  </div>


</div>
    """


    style = html.style(css_table)
    script = html.script(javascript_autofill)

    p_next = "Bitte klicken Sie nun auf <em>Weiter</em>, um fortzufahren."
    p_next = html.paragraph(p_next)

    # OUTPUT
    code = style + dtable + script + p_next
    html.code(title, code, filename)


for i in np.arange(1, tables+1, 1):
    codeTabelleHtml(i)
