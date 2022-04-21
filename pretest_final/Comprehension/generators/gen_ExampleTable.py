from lotteries_loader import LotteryLoader as lot
import numpy as np

# --------------------------------------------
data_gain_example = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries_comprehension.xls', 'GAIN_EXAMPLE'
)
data_loss_example = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries_comprehension.xls', 'LOSS_EXAMPLE'
)
# --------------------------------------------
javascript_autofill = open('gen_ExampleTable_autofill.js').read()
# --------------------------------------------
css_table = open('gen_ExampleTable_table.css').read()
# --------------------------------------------


def codeHTML(type, select_a, asc):

    # INITS
    p1 = None
    x1 = None
    x2 = None
    # --------------------------------------------
    if type == 'LOSS':
        p1 = data_loss_example['p'][0]
        x1 = data_loss_example['x1'][0]
        x2 = data_loss_example['x2'][0]
    # --------------------------------------------
    if type == 'GAIN':
        p1 = data_gain_example['p'][0]
        x1 = data_gain_example['x1'][0]
        x2 = data_gain_example['x2'][0]

    # Table B1: Numbering
    dtable_b1_numbering = ''
    for i in np.arange(1, 22, 1):
        dtable_b1_numbering = dtable_b1_numbering + f'<tr class="dtable-b1-tr"><td><span style="padding-right: 0.25rem">{i}</span></td></tr>\n'
    # --------------------------------------------
    dtable_b1 = f"""
    <table class="dtable-b1">
      <tr class="dtable-b1-tr1">
        <td>
          <span></span>
        </td>
      </tr>
      {dtable_b1_numbering}
    </table>
    """

    # Table B2: Option A
    dtable_b2_title = 'Option A: <br/> Lotterie'
    dtable_b2_var = ''
    dtable_b2_p1 = str("{0:.0%}".format(p1))
    dtable_b2_p2 = str("{0:.0%}".format(1-p1))
    dtable_b2_x1 = ''
    dtable_b2_x2 = ''
    # --------------------------------------------
    if type == 'LOSS':
        dtable_b2_var = 'Verlust'
        dtable_b2_x1 = str("{:.2f}".format(x1*-1)) + str(' Punkten')
        dtable_b2_x2 = str("{:.2f}".format(x2*-1)) + str(' Punkten')
    # --------------------------------------------
    if type == 'GAIN':
        dtable_b2_var = 'Auszahlung'
        dtable_b2_x1 = str("{:.2f}".format(x1)) + str(' Punkten')
        dtable_b2_x2 = str("{:.2f}".format(x2)) + str(' Punkten')
    # --------------------------------------------
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
            <p>{dtable_b2_var} von {dtable_b2_x1}</p>
            <p>mit {dtable_b2_p1} Wahrscheinlichkeit</p>
            <p>und {dtable_b2_var} von {dtable_b2_x2}</p>
            <p>mit {dtable_b2_p2} Wahrscheinlichkeit</p>
          </div>
        </td>
      </tr>
    </table>
    """

    # Table B3: Entscheidung
    dtable_b3_rows = ''
    for i in np.arange(0, 21, 1):
        if type == "GAIN":
            dtable_b3_rows = dtable_b3_rows + f'<tr class="dtable-b3-tr"><td>A</td><td><input required class="form-check-input {"gain"}-example-table" value="1" type="radio" id="EXAMPLE_GAIN_{i+1}-0" name="EXAMPLE_GAIN_{i+1}"/></td><td><input required class="form-check-input {"gain"}-example-table" type="radio" value="2" id="EXAMPLE_GAIN_{i+1}-1" name="EXAMPLE_GAIN_{i+1}"/></td><td>B</td></tr>\n'
        if type == "LOSS":
            dtable_b3_rows = dtable_b3_rows + f'<tr class="dtable-b3-tr"><td>A</td><td><input required class="form-check-input {"loss"}-example-table" value="1" type="radio" id="EXAMPLE_LOSS_{i+1}-0" name="EXAMPLE_LOSS_{i+1}"/></td><td><input required class="form-check-input {"loss"}-example-table" type="radio" value="2" id="EXAMPLE_LOSS_{i+1}-1" name="EXAMPLE_LOSS_{i+1}"/></td><td>B</td></tr>\n'
    # --------------------------------------------
    dtable_b3_title = 'Ihre Entscheidung'
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

    # Table B4: Option B
    dtable_b4_title_var = ''
    if type == 'GAIN':
        dtable_b4_title_var = "Sichere Auszahlung"
    if type == 'LOSS':
        dtable_b4_title_var = "Sicherer Verlust"
    dtable_b4_title = f'Option B: <br/> {dtable_b4_title_var}'
    # --------------------------------------------
    b_start = None
    b_step = None
    b_stop = None
    if type == "GAIN":
        b_start = data_gain_example['x1'][0]
        b_step = (-1)*(data_gain_example['x1'][0] - data_gain_example['x2'][0])/20
        b_stop = data_gain_example['x2'][0] + b_step
    if type == "LOSS":
        b_start = data_loss_example['x1'][0]
        b_step = (-1)*(data_loss_example['x1'][0] - data_loss_example['x2'][0])/20
        b_stop = data_loss_example['x2'][0] + b_step
    # --------------------------------------------
    dtable_b4_rows_data = []
    for i in np.arange(b_start, b_stop, b_step):
        if type == 'LOSS':
            i = i*(-1)
        dtable_b4_rows_data.append(str("{:.2f}".format(i)) + str(' Punkte'))
    if asc is True:
        dtable_b4_rows_data.reverse()
    dtable_b4_rows = ''
    for i in np.arange(0, 21, 1):
        dtable_b4_rows = dtable_b4_rows + f'<tr class="dtable-b4-tr"><td><span>{dtable_b4_rows_data[i]}</span></td></tr>\n'
    # --------------------------------------------
    dtable_b4_type = ''
    if type == "GAIN":
        dtable_b4_type = "gain-example-table"
    if type == "LOSS":
        dtable_b4_type = "loss-example-table"

    dtable_b4 = f"""
    <!--Tabelle B4: Option B-->
    <table class="dtable-b4 {dtable_b4_type}" id="ASC" name="{False}">
      <tr class="dtable-b4-tr1">
        <td>
          <span>{dtable_b4_title}</span>
        </td>
      </tr>
      {dtable_b4_rows}
    </table>
    """

    # Table: Body
    dtable_b = f"""
        <div class="dtable-b">
            {dtable_b1}
            {dtable_b2}
            {dtable_b3}
            {dtable_b4}
        </div>
        """

    # Table
    dtable = f"""
        <div class="dtable">
        {dtable_b}
        </div>
        """

    # OUTPUT
    f = ''
    if type == 'GAIN':
        f = open('gen_ExampleGainTable.html', 'w')
    if type == 'LOSS':
        f = open('gen_ExampleLossTable.html', 'w')
    f.write(dtable)
    f.close()



codeHTML('GAIN', 7, False)
codeHTML('LOSS', 10, False)
