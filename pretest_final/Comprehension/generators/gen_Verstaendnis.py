from generators import HtmlGenerator as html

# INITS
title = 'Beispiele und Verständnisfragen'
filename = 'Verstaendnis'
url = f'../templates/Comprehension/{filename}.html'
# --------------------------------------------
javascript_tabs = open('gen_Verstaendnis_tabs.js').read()
javascript_tabs = html.script(javascript_tabs)
# --------------------------------------------
javascript_autofill = open('gen_Verstaendnis_autofill.js').read()
javascript_autofill = html.script(javascript_autofill)
# --------------------------------------------
css_tabs = open('gen_Verstaendnis_tabs.css').read()
css_tabs = html.style(css_tabs)
# --------------------------------------------
css_comprehension = open('gen_Verstaendnis_comprehension.css').read()
css_comprehension = html.style(css_comprehension)
# --------------------------------------------
css_table = open('gen_Verstaednis_table.css').read()
css_table = html.style(css_table)


# HEADER
div_tabs_tab1 = "Info"
div_tabs_tab2 = "Beispiel: Gewinnsituation"
div_tabs_tab3 = "Beispiel: Verlustsituation"
div_tabs_tab4 = "Verständnisfragen"
# --------------------------------------------
div_tabs = f"""
<div>
    <ul class="nav nav-tabs   fixed-top navbar-light bg-light justify-content-center" id="myTab" role="tablist">
        <li class="nav-item">
            <a class="tabclick nav-link active show" id="part1-tab" data-toggle="tab" href="#part1" role="tab" aria-controls="part1" onclick="topFunction(); bootstrapTabControl(1);" aria-selected="true">
                {div_tabs_tab1}
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" id="part2-tab" data-toggle="tab" href="#part2" role="tab" aria-controls="part2" onclick="topFunction(); bootstrapTabControl(2);" aria-selected="false">
                {div_tabs_tab2}
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" id="part3-tab" data-toggle="tab" href="#part3" role="tab" aria-controls="part3" onclick="topFunction(); bootstrapTabControl(3);">
                {div_tabs_tab3}
            </a>
        </li>
                    <li class="nav-item">
            <a class="nav-link" id="part4-tab" data-toggle="tab" href="#part4" role="tab" aria-controls="part4" onclick="topFunction(); bootstrapTabControl(4);">
                {div_tabs_tab4}
            </a>
        </li>
    </ul>
</div>
"""


# REITER 1: INFO
reiter1_name = "Info"
reiter1_nr = 1
# --------------------------------------------
reiter1_p1 = """
Es beginnt gleich der erste Teil der Studie. 
Auf dieser Seite finden Sie dazu Erklärungen und Beispiele. 
Auf der folgenden Seite werden Sie Ihr Verständnis dieser Erklärungen überprüfen. 
Durch Klicken auf den Reiter oben können Sie zwischen den Seiten wechseln. 
"""
reiter1_p1 = html.paragraph(reiter1_p1)
reiter1_p2 = """
Nach korrekter Beantwortung der Verständnisfragen können Sie mit der weiteren Bearbeitung der Umfrage fortfahren.
"""
reiter1_p2 = html.paragraph(reiter1_p2)
reiter1_content = f"""
<div class="card-body">
    {reiter1_p1}
    {reiter1_p2}
</div>
"""
reiter1 = f"""
<div class="tab-pane {'show active'}" id="part{reiter1_nr}" role="tabpanel" aria-labelledby="part{reiter1_nr}-tab">
    <div class="card-header bg-transparent mainheader tab-header">
        <h2 class="card-title font-weight-bold">
            {reiter1_name}
        </h2>
    </div>
    {reiter1_content}
    <button onclick="topFunction(); bootstrapButtonControl('next');" type="button" class="nexttab btn-primary btn next">
        {'Weiter'}
    </button>
</div>
"""


# REITER 2: BSP GEWINN
reiter2_name = "Beispiel: Gewinnsituation"
reiter2_nr = 2
# --------------------------------------------
reiter2_eingabe_h = "Eingabe bei Gewinnsituation"
reiter2_eingabe_p1 = """
Hier wird Ihnen erklärt, wie Sie in einer Gewinnsituation ihre Entscheidungen eingeben. 
"""
reiter2_eingabe_p1 = html.paragraph(reiter2_eingabe_p1)
reiter2_eingabe_p2 = """
Wenn Sie sich hier für die Lotterie (Option A) entscheiden, besteht eine 50% Chance 20 Punkte zu gewinnen und eine 50% Chance 0 Punkte zu gewinnen. 
Entscheiden Sie sich hingegen für die sichere Auszahlung (Option B), so erhalten Sie mit Sicherheit die der Zeile entsprechenden Punktzahl zwischen 20 und 0.
"""
reiter2_eingabe_p2 = html.paragraph(reiter2_eingabe_p2)
reiter2_eingabe_p3 = """
Angenommen Sie würden lieber 13 Punkte als sichere Auszahlung haben als die Lotterie. 
Sobald die sichere Auszahlung jedoch kleiner ist als 13, entscheiden Sie sich lieber für die Lotterie. 
Dann geben Sie Ihre Entscheidung wie folgt in den Computer ein: Wählen Sie die Option B für die Zeilen 1-8 und die Option A für die Zeilen 9-21 aus. 
"""
reiter2_eingabe_p3 = html.paragraph(reiter2_eingabe_p3)
reiter2_eingabe_p4 = """
Beachten Sie: Ab der Zeile, in der Sie in Ihrer Entscheidung von einer Option zur anderen wechseln, füllt der Computer automatisch die nachfolgenden Zeilen für Sie aus. 
Sie können diese automatisch ausgefüllten Zeilen jederzeit wieder manuell verändern, indem Sie zur anderen Option wechseln.
Probieren Sie es aus.
"""
reiter2_eingabe_p4 = html.paragraph(reiter2_eingabe_p4)
reiter2_eingabe_table = """
<div class="dtable">
    
    <div class="dtable-b">
        
    <!--Tabelle B1: Nummerierung-->
    <table class="dtable-b1">
      <tbody><tr class="dtable-b1-tr1">
        <td>
          <span></span>
        </td>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">1</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">2</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">3</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">4</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">5</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">6</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">7</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">8</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">9</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">10</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">11</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">12</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">13</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">14</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">15</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">16</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">17</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">18</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">19</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">20</span>
        </th>
      </tr>
      
      <tr class="dtable-b1-tr">
        <th>
          <span style="padding-right: 0.25rem">21</span>
        </th>
      </tr>
      
    </tbody></table>
    
        
    <!--Tabelle B2: Option A-->
    <table class="dtable-b2">
      <tbody><tr class="dtable-b2-tr1">
        <td>
          <span>Option A: <br> Risikolotterie</span>
        </td>
      </tr>
      <tr class="dtable-b2-tr">
        <td>
          <div>
            <p>Auszahlung von 20.00 Punkte</p>
            <p>mit Wahrscheinlichkeit 10%</p>
            <p>und Auszahlung von 10.00 Punkte</p>
            <p>mit Wahrscheinlichkeit 90%</p>
          </div>
        </td>
      </tr>
    </tbody></table>
    
        
    <!--Tabelle B3: Entscheidung-->
    <table class="dtable-b3">
      <tbody><tr class="dtable-b3-tr1">
        <td colspan="4">
          <span>Ihre Entscheidung</span>
        </td>
      </tr>
      <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D1-0" name="B1_GAIN2_D1" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D1-1" name="B1_GAIN2_D1" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D2-0" name="B1_GAIN2_D2" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D2-1" name="B1_GAIN2_D2" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D3-0" name="B1_GAIN2_D3" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D3-1" name="B1_GAIN2_D3" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D4-0" name="B1_GAIN2_D4" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D4-1" name="B1_GAIN2_D4" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D5-0" name="B1_GAIN2_D5" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D5-1" name="B1_GAIN2_D5" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D6-0" name="B1_GAIN2_D6" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D6-1" name="B1_GAIN2_D6" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D7-0" name="B1_GAIN2_D7" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D7-1" name="B1_GAIN2_D7" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D8-0" name="B1_GAIN2_D8" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D8-1" name="B1_GAIN2_D8" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D9-0" name="B1_GAIN2_D9" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D9-1" name="B1_GAIN2_D9" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D10-0" name="B1_GAIN2_D10" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D10-1" name="B1_GAIN2_D10" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D11-0" name="B1_GAIN2_D11" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D11-1" name="B1_GAIN2_D11" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D12-0" name="B1_GAIN2_D12" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D12-1" name="B1_GAIN2_D12" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D13-0" name="B1_GAIN2_D13" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D13-1" name="B1_GAIN2_D13" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D14-0" name="B1_GAIN2_D14" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D14-1" name="B1_GAIN2_D14" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D15-0" name="B1_GAIN2_D15" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D15-1" name="B1_GAIN2_D15" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D16-0" name="B1_GAIN2_D16" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D16-1" name="B1_GAIN2_D16" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D17-0" name="B1_GAIN2_D17" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D17-1" name="B1_GAIN2_D17" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D18-0" name="B1_GAIN2_D18" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D18-1" name="B1_GAIN2_D18" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D19-0" name="B1_GAIN2_D19" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D19-1" name="B1_GAIN2_D19" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D20-0" name="B1_GAIN2_D20" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D20-1" name="B1_GAIN2_D20" required="" value="2"></td><td>B</td></tr>
<tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D21-0" name="B1_GAIN2_D21" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN2_D21-1" name="B1_GAIN2_D21" required="" value="2"></td><td>B</td></tr>

    </tbody></table>
    
        
    <!--Tabelle B4: Option B-->
    <table class="dtable-b4" id="ASC" name="False">
      <tbody><tr class="dtable-b4-tr1">
        <td>
          <span>Option B: <br> Sichere Auszahlung</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>20.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>19.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>19.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>18.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>18.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>17.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>17.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>16.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>16.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>15.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>15.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>14.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>14.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>13.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>13.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>12.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>12.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>11.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>11.00 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>10.50 Punkte</span>
        </td>
      </tr>
      
      <tr class="dtable-b4-tr">
        <td>
          <span>10.00 Punkte</span>
        </td>
      </tr>
      
    </tbody></table>
    
    </div>
    
    </div>
"""
reiter2_eingabe = f"""
<h4 class="card-title example-content-h-first">
    {reiter2_eingabe_h}
</h4>
{reiter2_eingabe_p1}
{reiter2_eingabe_p2}
{reiter2_eingabe_table}
{reiter2_eingabe_p3}
{reiter2_eingabe_p4}
"""
# --------------------------------------------
reiter2_auszahlung_h = "Auszahlung bei Gewinnsituation"
reiter2_auszahlung_p1 = """
Hier wird Ihnen erklärt, wie ihre Auszahlung zustande kommt, wenn zufällig eine Gewinnsituation für ihre Auszahlung ausgewählt wird. 
"""
reiter2_auszahlung_p1 = html.paragraph(reiter2_auszahlung_p1)
reiter2_auszahlung_p2 = """
Angenommen, Sie haben folgende Entscheidung getroffen:
XXX BILD XXX
"""
reiter2_auszahlung_p2 = html.paragraph(reiter2_auszahlung_p2)
reiter2_auszahlung_p3 = """
Der Computer hat nun zufällig Zeile XXX in dieser Tabelle für Ihre Auszahlung ausgewählt. 
Das bedeutet für Sie, dass Sie mit Sicherheit XXX Punkte erhalten. 
"""
reiter2_auszahlung_p3 = html.paragraph(reiter2_auszahlung_p3)
reiter2_auszahlung = f"""
<h4 class="card-title example-content-h">
    {reiter2_auszahlung_h}
</h4>
{reiter2_auszahlung_p1}
{reiter2_auszahlung_p2}
{reiter2_auszahlung_p3}
"""
# --------------------------------------------
reiter2_content = f"""
<div class="card-body">
    {reiter2_eingabe}
    <hr/>
    {reiter2_auszahlung}
</div>
"""
reiter2 = f"""
<div class="tab-pane" id="part{reiter2_nr}" role="tabpanel" aria-labelledby="part{reiter2_nr}-tab">
    <div class="card-header bg-transparent mainheader tab-header" >
        <h2 class="card-title font-weight-bold">
            {reiter2_name}
        </h2>
    </div>
    {reiter2_content}
    <button onclick="topFunction(); bootstrapButtonControl('back');" type="button" class="prevtab btn-primary btn back">
        {'Zurück'}
    </button>
    <button onclick="topFunction(); bootstrapButtonControl('next');" type="button" class="nexttab btn-primary btn next">
        {'Weiter'}
    </button>
</div>
"""


# REITER 3: BSP VERLUST
reiter3_name = "Beispiel: Verlustsituation"
reiter3_nr = 3
# --------------------------------------------
reiter3_eingabe_h = "Eingabe bei Verlustsituation"
reiter3_eingabe_p1 = """
Hier wird Ihnen erklärt, wie Sie in einer Verlustsituation ihre Entscheidungen eingeben. 
"""
reiter3_eingabe_p1 = html.paragraph(reiter3_eingabe_p1)
reiter3_eingabe_p2 = """
Nun eine Verlustsituation. 
Wenn Sie sich hier für die Lotterie (Option A) entscheiden, besteht eine 50% Chance 20 Punkte zu verlieren und eine 50% Chance 0 Punkte zu verlieren. 
Entscheiden Sie sich hingegen für die sichere Auszahlung (Option B), so verlieren Sie mit Sicherheit die der Zeile entsprechenden Punktzahl zwischen 20 und 0.
"""
reiter3_eingabe_p2 = html.paragraph(reiter3_eingabe_p2)
reiter3_eingabe_p3 = """
Angenommen Sie würden lieber die Lotterie haben als sicher 8 Punkte zu verlieren. 
Doch sobald Sie weniger als 8 Punkte verlieren, entscheiden Sie sich für die sichere Auszahlung.  
Dann geben Sie Ihre Entscheidung wie folgt in den Computer ein: 
Wählen Sie die Option A für die Zeilen 1-13 und die Option B für die Zeilen 14-21 aus. 
"""
reiter3_eingabe_p3 = html.paragraph(reiter3_eingabe_p3)
reiter3_eingabe_p4 = """
Beachten Sie: Ab der Zeile, in der Sie in Ihrer Entscheidung von einer Option zur anderen wechseln, füllt der Computer automatisch die nachfolgenden Zeilen für Sie aus. 
Sie können diese automatisch ausgefüllten Zeilen jederzeit wieder manuell verändern, indem Sie zur anderen Option wechseln. 
Probieren Sie es aus. 
"""
reiter3_eingabe_p4 = html.paragraph(reiter3_eingabe_p4)
reiter3_eingabe_table = """
<div class="dtable">

    <div class="dtable-b">

        <!--Tabelle B1: Nummerierung-->
        <table class="dtable-b1">
            <tbody><tr class="dtable-b1-tr1">
                <td>
                    <span></span>
                </td>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">1</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">2</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">3</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">4</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">5</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">6</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">7</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">8</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">9</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">10</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">11</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">12</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">13</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">14</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">15</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">16</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">17</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">18</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">19</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">20</span>
                </th>
            </tr>

            <tr class="dtable-b1-tr">
                <th>
                    <span style="padding-right: 0.25rem">21</span>
                </th>
            </tr>

            </tbody></table>


        <!--Tabelle B2: Option A-->
        <table class="dtable-b2">
            <tbody><tr class="dtable-b2-tr1">
                <td>
                    <span>Option A: <br> Risikolotterie</span>
                </td>
            </tr>
            <tr class="dtable-b2-tr">
                <td>
                    <div>
                        <p>Auszahlung von 10.00 Punkte</p>
                        <p>mit Wahrscheinlichkeit 50%</p>
                        <p>und Auszahlung von 0.00 Punkte</p>
                        <p>mit Wahrscheinlichkeit 50%</p>
                    </div>
                </td>
            </tr>
            </tbody></table>


        <!--Tabelle B3: Entscheidung-->
        <table class="dtable-b3">
            <tbody><tr class="dtable-b3-tr1">
                <td colspan="4">
                    <span>Ihre Entscheidung</span>
                </td>
            </tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D1-0" name="B1_GAIN1_D1" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D1-1" name="B1_GAIN1_D1" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D2-0" name="B1_GAIN1_D2" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D2-1" name="B1_GAIN1_D2" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D3-0" name="B1_GAIN1_D3" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D3-1" name="B1_GAIN1_D3" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D4-0" name="B1_GAIN1_D4" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D4-1" name="B1_GAIN1_D4" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D5-0" name="B1_GAIN1_D5" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D5-1" name="B1_GAIN1_D5" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D6-0" name="B1_GAIN1_D6" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D6-1" name="B1_GAIN1_D6" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D7-0" name="B1_GAIN1_D7" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D7-1" name="B1_GAIN1_D7" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D8-0" name="B1_GAIN1_D8" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D8-1" name="B1_GAIN1_D8" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D9-0" name="B1_GAIN1_D9" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D9-1" name="B1_GAIN1_D9" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D10-0" name="B1_GAIN1_D10" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D10-1" name="B1_GAIN1_D10" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D11-0" name="B1_GAIN1_D11" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D11-1" name="B1_GAIN1_D11" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D12-0" name="B1_GAIN1_D12" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D12-1" name="B1_GAIN1_D12" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D13-0" name="B1_GAIN1_D13" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D13-1" name="B1_GAIN1_D13" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D14-0" name="B1_GAIN1_D14" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D14-1" name="B1_GAIN1_D14" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D15-0" name="B1_GAIN1_D15" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D15-1" name="B1_GAIN1_D15" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D16-0" name="B1_GAIN1_D16" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D16-1" name="B1_GAIN1_D16" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D17-0" name="B1_GAIN1_D17" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D17-1" name="B1_GAIN1_D17" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D18-0" name="B1_GAIN1_D18" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D18-1" name="B1_GAIN1_D18" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D19-0" name="B1_GAIN1_D19" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D19-1" name="B1_GAIN1_D19" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D20-0" name="B1_GAIN1_D20" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D20-1" name="B1_GAIN1_D20" required="" value="2"></td><td>B</td></tr>
            <tr class="dtable-b3-tr"><td>A</td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D21-0" name="B1_GAIN1_D21" required="" value="1"></td><td><input class="form-check-input" type="radio" id="id_B1_GAIN1_D21-1" name="B1_GAIN1_D21" required="" value="2"></td><td>B</td></tr>

            </tbody></table>


        <!--Tabelle B4: Option B-->
        <table class="dtable-b4" id="ASC" name="True">
            <tbody><tr class="dtable-b4-tr1">
                <td>
                    <span>Option B: <br> Sichere Auszahlung</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>0.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>0.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>1.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>1.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>2.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>2.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>3.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>3.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>4.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>4.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>5.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>5.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>6.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>6.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>7.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>7.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>8.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>8.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>9.00 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>9.50 Punkte</span>
                </td>
            </tr>

            <tr class="dtable-b4-tr">
                <td>
                    <span>10.00 Punkte</span>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</div>
"""
reiter3_eingabe = f"""
<h4 class="card-title example-content-h-first">
    {reiter3_eingabe_h}
</h4>
{reiter3_eingabe_p1}
{reiter3_eingabe_p2}
{reiter3_eingabe_table}
{reiter3_eingabe_p3}
{reiter3_eingabe_p4}
"""
# --------------------------------------------
reiter3_auszahlung_h = "Auszahlung bei Verlustsituation"
reiter3_auszahlung_p1 = """
Hier wird Ihnen erklärt, wie ihre Auszahlung zustande kommt, wenn zufällig eine Verlustsituation für ihre Auszahlung ausgewählt wird. 
"""
reiter3_auszahlung_p1 = html.paragraph(reiter3_auszahlung_p1)
reiter3_auszahlung_p2 = """
Angenommen, Sie haben folgende Entscheidung getroffen:
XXX BILD XXX
"""
reiter3_auszahlung_p2 = html.paragraph(reiter3_auszahlung_p2)
reiter3_auszahlung_p3 = """
Der Computer hat nun zufällig Zeile XXX in dieser Tabelle für Ihre Auszahlung ausgewählt. 
Das bedeutet für Sie, dass Sie mit 50% Wahrscheinlichkeit 0 Punkte verlieren und mit 50% Wahrscheinlichkeit 20 Punkte verlieren. 
"""
reiter3_auszahlung_p3 = html.paragraph(reiter3_auszahlung_p3)
reiter3_auszahlung = f"""
<h4 class="card-title example-content-h">
    {reiter3_auszahlung_h}
</h4>
{reiter3_auszahlung_p1}
{reiter3_auszahlung_p2}
{reiter3_auszahlung_p3}
"""
# --------------------------------------------
reiter3_content = f"""
<div class="card-body">
    {reiter3_eingabe}
    <hr/>
    {reiter3_auszahlung}
</div>
"""
reiter3 = f"""
<div class="tab-pane" id="part{reiter3_nr}" role="tabpanel" aria-labelledby="part{reiter3_nr}-tab">
    <div class="card-header bg-transparent mainheader tab-header" >
        <h2 class="card-title font-weight-bold">
            {reiter3_name}
        </h2>
    </div>
    {reiter3_content}
    <button onclick="topFunction(); bootstrapButtonControl('back');" type="button" class="prevtab btn-primary btn back">
        {'Zurück'}
    </button>
    <button onclick="topFunction(); bootstrapButtonControl('next');" type="button" class="nexttab btn-primary btn next">
        {'Weiter'}
    </button>
</div>
"""


# REITER
div_reiter = f"""
<div class="tab-content" id="myTabContent">
    {reiter1}
    {reiter2}
    {reiter3}
</div>
"""


# OUTPUT
code = div_tabs + div_reiter + css_tabs + css_comprehension + css_table + javascript_tabs + javascript_autofill
html.code(title, code, url)

