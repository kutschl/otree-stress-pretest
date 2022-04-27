from generators import HtmlGenerator as html
from lotteries_loader import LotteryLoader as lot
import numpy as np

# -----------------------------------------------------------------------------------------
data_gain = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'GAIN'
)
data_loss = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'LOSS'
)
# -----------------------------------------------------------------------------------------
javascript_autofill = open('gen_BlockTabelle_autofill.js').read()
javascript_autofill = html.script(javascript_autofill)
javascript_vars = open('gen_BlockTabelle_vars.js').read()
javascript_vars = html.script(javascript_vars)
# -----------------------------------------------------------------------------------------
css_table = open('gen_BlockTabelle_table.css').read()
css_table = html.style(css_table)
# -----------------------------------------------------------------------------------------
gain_tables_per_block = len(data_gain[list(data_gain.keys())[0]])
loss_tables_per_block = len(data_loss[list(data_loss.keys())[0]])
tables_per_block = gain_tables_per_block + loss_tables_per_block
blocks = 2
tables = blocks * tables_per_block
decisions_per_table = 21
# -----------------------------------------------------------------------------------------


def ModelsPy_Vars():
    code = ''
    for block in np.arange(1, blocks+1, 1):
        for table in np.arange(1, tables_per_block+1, 1):
            code = code + f"""
    # BLOCK {block} TABLE {table}
    BLOCK{block}_TABLE{table}_LOTTERY = models.IntegerField()
    BLOCK{block}_TABLE{table}_TYPE = models.IntegerField()
    BLOCK{block}_TABLE{table}_ORDER = models.IntegerField()
    BLOCK{block}_TABLE{table}_SP_OPTION = models.IntegerField()
    BLOCK{block}_TABLE{table}_SP_DECISION = models.IntegerField()
"""
    return code


print(ModelsPy_Vars())


# -----------------------------------------------------------------------------------------


def HtmlTableB3Rows():
    code = ''
    for decision in np.arange(1, decisions_per_table + 1, 1):
        code = code + f"""
        <tr class="dtable-b3-tr">
        <td>A</td>
        <td>
            <input class="form-check-input" type="radio" value="0" id="RADIO_{decision}-0" name="RADIO_{decision}" required>
        </td>
        <td>
            <input class="form-check-input" type="radio" value="1" id="RADIO_{decision}-1" name="RADIO_{decision}" required>
        </td>
        <td>B</td>
        </tr>
        """
    return code


def HtmlTable(b, t):

    # INITS
    title = f"""
    Teil {b}: Tabelle ({t}/40):
    {{% if participant.vars.block{b}.{t-1}.TYPE == 0 %}}
    Gewinnsituation
    {{% endif %}}
    {{% if participant.vars.block{b}.{t-1}.TYPE == 1 %}}
    Verlustsituation
    {{% endif %}}
    """
    filename = f'../templates/Game/Block{b}Table{t}.html'
    # -----------------------------------------------------------------------------------------

    # TASK
    p_task = """
    Bitte wählen Sie für jede Zeile eine der beiden Entscheidungsoptionen aus.
    Sobald Sie überall eine Entscheidung getroffen haben, klicken Sie bitte auf <em>Weiter</em>.
    """
    p_task = html.paragraph(p_task)
    # -----------------------------------------------------------------------------------------

    # TABLE B1
    dtable_b1_title = ''
    dtable_b1 = f"""
    <!--Tabelle B1: Nummerierung-->
    <table class="dtable-b1">
      <tr class="dtable-b1-tr1">
        <td>
          <span>{dtable_b1_title}</span>
        </td>
      </tr>
      {{% for i in participant.vars.block{b}.{t-1}.NUMBERING %}}
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">{{% i %}}</span>
        </th>
      </tr>
      {{% endfor %}}
    </table>
    """
    # -----------------------------------------------------------------------------------------

    # TABLE B2
    dtable_b2_title = 'Option A: <br/> Lotterie'
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
          
            <p>
            {{% if participant.vars.block{b}.{t-1}.TYPE == 0 %}}
            Gewinn
            {{% endif %}}
            {{% if participant.vars.block{b}.{t-1}.TYPE == 1 %}}
            Verlust
            {{% endif %}}
            von 
            {{% participant.vars.block{b}.{t-1}.OPTION_A.x1%}}
            Punkten
            </p>
            
            <p>
            mit 
            {{% participant.vars.block{b}.{t-1}.OPTION_A.p1%}}
            Wahrscheinlichkeit
            </p>
            
            <p>
            {{% if participant.vars.block{b}.{t-1}.TYPE == 0 %}}
            Gewinn
            {{% endif %}}
            {{% if participant.vars.block{b}.{t-1}.TYPE == 1 %}}
            Verlust
            {{% endif %}}
            von 
            {{% participant.vars.block{b}.{t-1}.OPTION_A.x2%}}
            Punkten
            </p>
            
            <p>
            mit 
            {{% participant.vars.block{b}.{t-1}.OPTION_A.p2%}}
            Wahrscheinlichkeit
            </p>
            
          </div>
        </td>
      </tr>
    </table>
    """
    # -----------------------------------------------------------------------------------------

    # TABLE B3
    dtable_b3_title = 'Ihre Entscheidung'
    dtable_b3_rows = HtmlTableB3Rows()
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
    # -----------------------------------------------------------------------------------------

    # TABLE B4
    dtable_b4_title = f"""
    Option B: <br/>
    Sicherer 
    {{% if participant.vars.block{b}.{t-1}.TYPE == 0 %}}
    Gewinn
    {{% endif %}}
    {{% if participant.vars.block{b}.{t-1}.TYPE == 1 %}}
    Verlust
    {{% endif %}}
    """
    dtable_b4 = f"""
    <!--Tabelle B4: Option B-->
    <table class="dtable-b4">
      <tr class="dtable-b4-tr1">
        <td>
          <span>{dtable_b4_title}</span>
        </td>
      </tr>
      {{% for i in participant.vars.block{b}.{t-1}.OPTION_B %}}
      <tr class="dtable-b4-tr">
        <td>
          <span>{{% i %}} Punkte</span>
        </td>
      </tr>
      {{% endfor %}}
    </table>
    """
    # -----------------------------------------------------------------------------------------

    # TABLE
    dtable_b = f"""
    <div class="dtable-b">
        {dtable_b1}
        {dtable_b2}
        {dtable_b3}
        {dtable_b4}
    </div>
    """
    dtable = f"""
    <div class="dtable" id="TYPE{{% participant.vars.block{b}.{t-1}.ORDER %}}_ORDER{{% participant.vars.block{b}.{t-1}.ORDER %}}">
    {dtable_b}
    </div>
    """
    # -----------------------------------------------------------------------------------------

    # VARS
    div_vars = f"""
    <div style="display:none;">
    
        {{% formfield player.BLOCK{b}_TABLE{t}_LOTTERY %}}
        {{% formfield player.BLOCK{b}_TABLE{t}_TYPE %}}
        {{% formfield player.BLOCK{b}_TABLE{t}_ORDER %}}
        {{% formfield player.BLOCK{b}_TABLE{t}_SP_OPTION %}}
        {{% formfield player.BLOCK{b}_TABLE{t}_SP_DECISION %}}         
                    
    </div>
    """

    # -----------------------------------------------------------------------------------------

    # NEXT BUTTON
    button_next = html.next_button()
    div_next = f"""
    <div class="{'otree-next'}" id="{'otree-next'}">
        {button_next}
    </div>
    """
    # -----------------------------------------------------------------------------------------

    # OUTPUT
    code = p_task + dtable + div_vars + css_table + javascript_autofill + javascript_vars + div_next
    html.code(title, code, filename)


for block in np.arange(1, blocks + 1, 1):
    for table in np.arange(1, tables_per_block+1, 1):
        HtmlTable(block, table)


# -----------------------------------------------------------------------------------------

