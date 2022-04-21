from generators import HtmlGenerator as html

# INITS
title = 'Beispiele und Verständnisfragen'
filename = 'Verstaendnis'
url = f'../templates/Comprehension/{filename}.html'
# --------------------------------------------
javascript_tabs = open('gen_Verstaendnis_tabs.js').read()
javascript_tabs = html.script(javascript_tabs)
# --------------------------------------------
javascript_autofill = open('gen_ExampleTable_autofill.js').read()
javascript_autofill = html.script(javascript_autofill)
# --------------------------------------------
css_tabs = open('gen_Verstaendnis_tabs.css').read()
css_tabs = html.style(css_tabs)
# --------------------------------------------
css_comprehension = open('gen_Verstaendnis_comprehension.css').read()
css_comprehension = html.style(css_comprehension)
# --------------------------------------------
css_table = open('gen_ExampleTable_table.css').read()
css_table = html.style(css_table)
# --------------------------------------------
html_example_gain_table_input = open('gen_ExampleGainTableInput.html').read()
html_example_loss_table_input = open('gen_ExampleLossTableInput.html').read()
# --------------------------------------------
html_example_gain_table_payoff = open('gen_ExampleGainTablePayoff.html').read()
html_example_loss_table_payoff = open('gen_ExampleLossTablePayoff.html').read()
# --------------------------------------------
html_question1_table = open('gen_Question1_Table.html').read()
html_question2_table = open('gen_Question2_Table.html').read()
html_question3_table = open('gen_Question3_Table.html').read()
html_question4_table = open('gen_Question4_Table.html').read()


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
reiter2_eingabe_h = "Ihre Eingabe"
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
reiter2_eingabe_table = html_example_gain_table_input
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
reiter2_auszahlung_h = "Ihre Auszahlung"
reiter2_auszahlung_p1 = """
Hier wird Ihnen erklärt, wie ihre Auszahlung zustande kommt, wenn zufällig eine Gewinnsituation für ihre Auszahlung ausgewählt wird. 
"""
reiter2_auszahlung_p1 = html.paragraph(reiter2_auszahlung_p1)
reiter2_auszahlung_p2 = """
Angenommen, Sie haben folgende Entscheidung getroffen:
"""
reiter2_auszahlung_p2 = html.paragraph(reiter2_auszahlung_p2)
reiter2_auszahlung_table = html_example_gain_table_payoff
reiter2_auszahlung_p3 = """
Der Computer hat nun zufällig Zeile 10 in dieser Tabelle für Ihre Auszahlung ausgewählt. 
Das bedeutet für Sie, dass Sie mit 50% Wahrscheinlichkeit 20 Punkte erhalten und mit 50% Wahrscheinlichkeit 0 Punkte erhalten.
"""
reiter2_auszahlung_p3 = html.paragraph(reiter2_auszahlung_p3)
reiter2_auszahlung = f"""
<h4 class="card-title example-content-h">
    {reiter2_auszahlung_h}
</h4>
{reiter2_auszahlung_p1}
{reiter2_auszahlung_p2}
{reiter2_auszahlung_table}
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
reiter3_eingabe_h = "Ihre Eingabe"
reiter3_eingabe_p1 = """
Hier wird Ihnen erklärt, wie Sie in einer Verlustsituation ihre Entscheidungen eingeben. 
"""
reiter3_eingabe_p1 = html.paragraph(reiter3_eingabe_p1)
reiter3_eingabe_p2 = """
Wenn Sie sich hier für die Lotterie (Option A) entscheiden, besteht eine 5% Chance 50 Punkte zu verlieren und eine 95% Chance 150 Punkte zu verlieren. 
Entscheiden Sie sich hingegen für die sicheren Verlust (Option B), so verlieren Sie mit Sicherheit die der Zeile entsprechenden Punktzahl zwischen 50 und 150.
"""
reiter3_eingabe_p2 = html.paragraph(reiter3_eingabe_p2)
reiter3_eingabe_p3 = """
Angenommen Sie würden lieber die Lotterie haben als sicher 130 Punkte zu verlieren. 
Doch sobald Sie weniger als 130 Punkte verlieren, entscheiden Sie sich für die sicheren Verlust.  
Dann geben Sie Ihre Entscheidung wie folgt in den Computer ein: 
Wählen Sie die Option A für die Zeilen 1-5 und die Option B für die Zeilen 6-21 aus. 
"""
reiter3_eingabe_p3 = html.paragraph(reiter3_eingabe_p3)
reiter3_eingabe_p4 = """
Beachten Sie: Ab der Zeile, in der Sie in Ihrer Entscheidung von einer Option zur anderen wechseln, füllt der Computer automatisch die nachfolgenden Zeilen für Sie aus. 
Sie können diese automatisch ausgefüllten Zeilen jederzeit wieder manuell verändern, indem Sie zur anderen Option wechseln. 
Probieren Sie es aus. 
"""
reiter3_eingabe_p4 = html.paragraph(reiter3_eingabe_p4)
reiter3_eingabe_table = html_example_loss_table_input
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
reiter3_auszahlung_h = "Ihre Auszahlung"
reiter3_auszahlung_p1 = """
Hier wird Ihnen erklärt, wie ihre Auszahlung zustande kommt, wenn zufällig eine Verlustsituation für ihre Auszahlung ausgewählt wird. 
"""
reiter3_auszahlung_p1 = html.paragraph(reiter3_auszahlung_p1)
reiter3_auszahlung_p2 = """
Angenommen, Sie haben folgende Entscheidung getroffen:
"""
reiter3_auszahlung_p2 = html.paragraph(reiter3_auszahlung_p2)
reiter3_auszahlung_table = html_example_loss_table_payoff
reiter3_auszahlung_p3 = """
Der Computer hat nun zufällig Zeile 8 in dieser Tabelle für Ihre Auszahlung ausgewählt. 
Das bedeutet für Sie, dass Sie sicher 115 Punkte verlieren. 
"""
reiter3_auszahlung_p3 = html.paragraph(reiter3_auszahlung_p3)
reiter3_auszahlung = f"""
<h4 class="card-title example-content-h">
    {reiter3_auszahlung_h}
</h4>
{reiter3_auszahlung_p1}
{reiter3_auszahlung_p2}
{html_example_loss_table_payoff}
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


# REITER 3: BSP VERLUST
reiter4_name = "Verständnisfragen"
reiter4_nr = 4
# --------------------------------------------
reiter4_task_p1 = """
Bitte beantworten Sie die folgenden Verständnisfragen. 
Falls Sie sich die Ablaufbeschreibung noch einmal anschauen wollen, können Sie durch Klick auf den Reiter oben zwischen den Seiten hin und her wechseln.
"""
reiter4_task_p1 = html.paragraph(reiter4_task_p1)
reiter4_task_p2 = """
Nach korrekter Beantwortung der Verständnisfragen können Sie mit der weiteren Bearbeitung der Umfrage fortfahren. 
Klicken Sie dazu auf <em>Weiter zur restlichen Umfrage.</em>
"""
reiter4_task_p2 = html.paragraph(reiter4_task_p2)
# --------------------------------------------
reiter4_q1_h = "Frage 1 (Gewinnsituation)"
reiter4_q1_p1 = """
Angenommen Sie haben folgende Entscheidung getroffen.
"""
reiter4_q1_p1 = html.paragraph(reiter4_q1_p1)
reiter4_q1_table = html_question1_table
reiter4_q1_form = "{% formfield player.COMPREHENSION_Q1 %}"
reiter4_q1 = f"""
<div style="margin-top: 1rem; margin-bottom: 3rem">
<h4 class="card-title example-content-h">
{reiter4_q1_h}
</h4>
{reiter4_q1_p1}
{reiter4_q1_table}
{reiter4_q1_form}
</div>
"""
# --------------------------------------------
reiter4_q2_h = "Frage 2 (Gewinnsituation)"
reiter4_q2_p1 = """
Angenommen Sie haben folgende Entscheidung getroffen.
"""
reiter4_q2_p1 = html.paragraph(reiter4_q2_p1)
reiter4_q2_table = html_question2_table
reiter4_q2_form = "{% formfield player.COMPREHENSION_Q2 %}"
reiter4_q2 = f"""
<div style="margin-top: 1rem; margin-bottom: 3rem">
<h4 class="card-title example-content-h">
{reiter4_q2_h}
</h4>
{reiter4_q2_p1}
{reiter4_q2_table}
{reiter4_q2_form}
</div>
"""
# --------------------------------------------
reiter4_q3_h = "Frage 3 (Verlustsituation)"
reiter4_q3_p1 = """
Angenommen Sie haben folgende Entscheidung getroffen.
"""
reiter4_q3_p1 = html.paragraph(reiter4_q3_p1)
reiter4_q3_table = html_question3_table
reiter4_q3_form = "{% formfield player.COMPREHENSION_Q3 %}"
reiter4_q3 = f"""
<div style="margin-top: 1rem; margin-bottom: 3rem">
<h4 class="card-title example-content-h">
{reiter4_q3_h}
</h4>
{reiter4_q3_p1}
{reiter4_q3_table}
{reiter4_q3_form}
</div>
"""
# --------------------------------------------
reiter4_q4_h = "Frage 4 (Verlustsituation)"
reiter4_q4_p1 = """
Angenommen Sie haben folgende Entscheidung getroffen.
"""
reiter4_q4_p1 = html.paragraph(reiter4_q4_p1)
reiter4_q4_table = html_question4_table
reiter4_q4_form = "{% formfield player.COMPREHENSION_Q4 %}"
reiter4_q4 = f"""
<div style="margin-top: 1rem; margin-bottom: 3rem">
<h4 class="card-title example-content-h">
{reiter4_q4_h}
</h4>
{reiter4_q4_p1}
{reiter4_q4_table}
{reiter4_q4_form}
</div>
"""
# --------------------------------------------


reiter4_content = f"""
<div class="card-body">
    {reiter4_task_p1}
    {reiter4_task_p2}
    <hr/>
    {reiter4_q1}
    <hr/>
    {reiter4_q2}
    <hr/>    
    {reiter4_q3}
    <hr/>
    {reiter4_q4}
</div>
"""
reiter4 = f"""
<div class="tab-pane" id="part{reiter4_nr}" role="tabpanel" aria-labelledby="part{reiter4_nr}-tab">
    <div class="card-header bg-transparent mainheader tab-header" >
        <h2 class="card-title font-weight-bold">
            {reiter4_name}
        </h2>
    </div>
    {reiter4_content}
    <button onclick="topFunction(); bootstrapButtonControl('back');" type="button" class="prevtab btn-primary btn back">
        {'Zurück'}
    </button>
    <button class="nexttab btn-primary btn next">{'Weiter zur restlichen Umfrage'}</button>

</div>
"""

# REITER
div_reiter = f"""
<div class="tab-content" id="myTabContent">
    {reiter1}
    {reiter2}
    {reiter3}
    {reiter4}
</div>
"""


# OUTPUT
code = div_tabs + div_reiter + css_tabs + css_comprehension + css_table + javascript_tabs + javascript_autofill
html.code(title, code, url)

