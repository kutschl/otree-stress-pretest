from html_generator import HtmlGenerator as html

# INITS
title = 'Ihre Einwilligung'
filename = 'Einverstaendniserklaerung'
url = f'../templates/Intro/{filename}.html'
code = ''


# EXTERN FILES
javascript_hideNext = open('gen_Einverstaendniserklaerung_hideNext.js').read()
javascript_hideNext = html.script(javascript_hideNext)
javascript_selectAccept = open('gen_Einverstaendniserklaerung_selectAccept.js').read()
javascript_selectAccept = html.script(javascript_selectAccept)


# TASK
email = 'schulzetilling@uni-bonn.de'
email = html.link('mail', email, email)

p_task1 = """
Um an der Studie teilnehmen zu können, müssen Sie der Verarbeitung Ihrer personenbezogenen Daten zustimmen. 
Lesen Sie sich dafür die unten angezeigte Probandenaufklärung gründlich durch. 
Sie können zustimmen, indem Sie am Ende der Aufklärung die entsprechende Option auswählen. 
Wenn Sie der Verarbeitung Ihrer Daten nicht zustimmen, können Sie leider nicht an dieser Studie teilnehmen.
"""
p_task1 = html.paragraph(p_task1)
p_task2 = f"""
Bei Fragen können sie sich jederzeit (auch anonym) an die folgende E-Mail wenden: 
<br/>
{email}.
"""
p_task2 = html.paragraph(p_task2)


# EINVERSTÄNDNISERKLÄRUNG
h_consent = "Einverständniserklärung in die Erhebung und Verarbeitung von Daten durch die Universität Bonn im Rahmen einer Online-Studie"
h_consent = html.headline(4, h_consent)

p_consent1 = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et 
dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita 
kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur 
sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. 
At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem 
ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt 
ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 
Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. 
Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat 
nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue 
duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy 
nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. 
Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo 
consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore 
eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril 
delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil 
imperdiet doming id quod mazim placerat facer """

div_consent = f"""
<div class="alert border border-dark" style="margin-top: 2rem;">
{h_consent}
<div style="text-align: justify; font-size: 0.875rem;"/>
{p_consent1}
</div>
</div>
"""


# FORM
form_accept = f"""
<div id="id_ACCEPT" required="" style="margin-top: 2rem; margin-bottom: 1rem">
    <div class="form-check">
        <input class="form-check-input" type="radio" id="{'id_ACCEPT-0'}" name="ACCEPT" required="" value="{'True'}">
        <label for="id_ACCEPT-0">{'Ja, ich willige ein.'}</label>
    </div>
    <div class="form-check">
        <input class="form-check-input" type="radio" id="{'id_ACCEPT-1'}" name="ACCEPT" required="" value="{'False'}" data-bs-toggle="modal" data-bs-target="#exampleModal">
        <label for="id_ACCEPT-1">{'Nein, ich willige nicht ein.'}</label>
    </div>
</div>
"""


# MODAL
p1_modal = """
Sie haben der Verarbeitung Ihrer personenbezogenen Daten im Rahmen dieser Studie nicht zugestimmt.
Bitte beachten Sie, dass Sie nur an der Studie teilnehmen können, wenn Sie der Verarbeitung zustimmen.         
"""
p1_modal = html.paragraph(p1_modal)
p2_modal = """
Falls Sie Ihre Auswahl noch einmal ändern wollen, klicken Sie auf "Auswahl ändern".
Falls nicht, können Sie das Browserfenster bzw. den Browsertab jetzt schließen und nehmen somit nicht an der Studie teil.
Ihnen entstehen dadurch keine Nachteile.
"""
p2_modal = html.paragraph(p2_modal)

div_modal = f"""
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel"></h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                {p1_modal}
                {p2_modal}
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal" onclick="{'selectAccept()'}">
                    {'Auswahl ändern'}
                </button>
            </div>
        </div>
    </div>
</div>
"""

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
code = p_task1 + p_task2 + div_consent + form_accept + div_modal + div_next + javascript_hideNext + javascript_selectAccept
html.code(title, code, url)

