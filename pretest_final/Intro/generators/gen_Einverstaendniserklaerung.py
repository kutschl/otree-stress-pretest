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
css_consent = open('gen_Einverstaendniserklaerung_consent.css').read()
css_consent = html.style(css_consent)


# TASK
email = 'schulzetilling@uni-bonn.de'
email = html.link('mail', email, email)
div_task_p1 = """
Um an der Studie teilnehmen zu können, müssen Sie der Verarbeitung Ihrer personenbezogenen Daten zustimmen. 
Lesen Sie sich dafür die unten angezeigte Probandenaufklärung gründlich durch. 
Sie können zustimmen, indem Sie am Ende der Aufklärung die entsprechende Option auswählen. 
Wenn Sie der Verarbeitung Ihrer Daten nicht zustimmen, können Sie leider nicht an dieser Studie teilnehmen.
"""
div_task_p1 = html.paragraph(div_task_p1)
div_task_p2 = f"""
Bei Fragen können sie sich jederzeit (auch anonym) an die folgende E-Mail wenden: {email}.
"""
div_task_p2 = html.paragraph(div_task_p2)
div_task = f"""
<div class="consent-task">
{div_task_p1}
{div_task_p2}
</div>
"""


# EINVERSTÄNDNISERKLÄRUNG
div_head_h = "Einverständniserklärung in die Erhebung und Verarbeitung von Daten durch die Universität Bonn im Rahmen einer Online-Studie"
div_head_h = html.headline(4, div_head_h)
div_head = f"""
<div class="consent-head">
{div_head_h}
</div>
"""


# 1. Abschnitt
div_body1_email = "schulzetilling@uni-bonn.de"
div_body1_email = html.link('mail', div_body1_email, div_body1_email)
div_body1_link = "https://www.uni-bonn.de"
div_body1_link = html.link('web', div_body1_link, div_body1_link)
div_body1_h = "Wer ist verantwortlich für die Forschungsstudie?"
div_body1_p1 = """
<b>Verantwortlich für die Durchführung der Forschungsstudie und damit für die Verarbeitung Ihrer Daten ist:</b>
"""
div_body1_p1 = html.paragraph(div_body1_p1)
div_body1_p2 = f"""
Anna Schulze Tilling, Bonn Graduate School of Economics/ CRC Transregio 224 EPoS, Universität Bonn, Kaiserstr. 1, 53111 Bonn, E-Mail: {div_body1_email}
"""
div_body1_p2 = html.paragraph(div_body1_p2)
div_body1_p3 = f"""
<b>Verantwortlich im datenschutzrechtlichen Sinne:</b>
"""
div_body1_p3 = html.paragraph(div_body1_p3)
div_body1_p4 = f"""
Rheinische Friedrich-Wilhelms-Universität Bonn, Regina-Pacis-Weg 3, 53113 Bonn, 
E-Mail: kommunikation@uni-bonn.de, Tel: +49 (0)228-73-0, {div_body1_link}
"""
div_body1_p4 = html.paragraph(div_body1_p4)
div_body1 = f"""
<div class="consent-body-section">
    <div class="consent-body-section-h">
        {div_body1_h}
    </div>
    <div class="consent-body-section-p" id="consent-body-section-1">
        {div_body1_p1}
        {div_body1_p2}
        {div_body1_p3}
        {div_body1_p4}
    </div>
</div>
"""


# 2. Abschnitt
div_body2_h = "Welchen Zwecken dient die Studie?"
div_body2_p1 = """
Das Ziel dieser Forschungsstudie ist es, menschliches Verhalten in wirtschaftlich relevanten Zusammenhängen besser zu verstehen. 
Die Wissenschaft ist an möglichst verzerrungsfreiem, natürlichem Verhalten interessiert. 
Wie bei experimentalökonomischen Studien üblich, erfolgt daher vorab keine umfassende Aufklärung über den Forschungshintergrund. 
Sie werden in dieser Studie Entscheidungen an Ihrem Computer treffen. 
Sie erhalten sämtliche relevante Informationen zum weiteren Ablauf und zu den zu treffenden Entscheidungen zu gegebener Zeit.
"""
div_body2_p1 = html.paragraph(div_body2_p1)
div_body2 = f"""
<div class="consent-body-section">
    <div class="consent-body-section-h">
        {div_body2_h}
    </div>
    <div class="consent-body-section-p">
        {div_body2_p1}
    </div>
</div>
"""


# 3. Abschnitt
div_body3_h = "Was geschieht mit meinen Daten?"
div_body3_p1 = """
Alle beteiligten Mitarbeiter und Wissenschaftler arbeiten selbstverständlich nach den Vorschriften der Datenschutz-Grundverordnung, 
dem Bundesdatenschutzgesetz und den einschlägigen Landesdatenschutzgesetzen.
"""
div_body3_p1 = html.paragraph(div_body3_p1)
div_body3_p2 = """
Ihre Daten werden unmittelbar nach der Erhebung in anonymisierter Form gespeichert und anschließend statistisch ausgewertet. 
Die an der Studie beteiligten Forscher*innen sind nicht in der Lage, Rückschlüsse auf Ihre Person zu ziehen. 
Nach der Anonymisierung darf der erzeugte Datensatz zeitlich unbegrenzt gespeichert, verbreitet und öffentlich zugänglich gemacht werden.
"""
div_body3_p2 = html.paragraph(div_body3_p2)
div_body3_p3 = """
Die Daten werden auf einem Server der Universität Bonn gespeichert. 
Die Dauer der Speicherung der personenbezogenen Daten bemisst sich an den Leitlinien zur Sicherung guter wissenschaftlicher Praxis und an gesetzlichen Vorschriften (beispielsweise zur Aufbewahrung von Auszahlungsbelegen) und erfolgt für einen Zeitraum von zehn Jahren. 
Die Aufbewahrungsfrist beginnt mit dem Datum der Bereitstellung der personenbezogenen Daten. 
Nach Ablauf der Frist werden die entsprechenden Daten routinemäßig gelöscht, sofern kein berechtigtes Interesse an der Weiterspeicherung fortbesteht. 
Gebietet die Ausübung von Interventionsrechten die Löschung, werden die entsprechenden Daten unverzüglich gelöscht.
"""
div_body3_p3 = html.paragraph(div_body3_p3)
div_body3_p4 = """
Da diese Studie online durchgeführt wird, erfolgt die Auszahlung für Ihre Teilnahme an dieser Studie per Banküberweisung. 
Dafür benötigen wir Ihren Namen und Ihre Bankverbindungsdaten, welche verwendet werden, um die vereinbarte Summe für die Teilnahme an Sie zu überweisen und um die Auszahlung zu dokumentieren. 
Ihr Name und Ihre Bankverbindungsdaten werden getrennt von allen restlichen Daten gespeichert und ausschließlich verwendet, um Ihnen Ihre Auszahlung zu überweisen. 
Nachdem Ihnen Ihre Auszahlung überwiesen wurde, wird der Datensatz, welcher Ihren Namen und Ihre Bankverbindungsdaten enthält, gelöscht. 
Gespeichert verbleibt lediglich der Buchungsbeleg, der die Auszahlung an Sie dokumentiert und gemäß §147 AO aufbewahrt werden muss.
"""
div_body3_p4 = html.paragraph(div_body3_p4)
div_body3 = f"""
<div class="consent-body-section">
    <div class="consent-body-section-h">
        {div_body3_h}
    </div>
    <div class="consent-body-section-p">
        {div_body3_p1}
        {div_body3_p2}
        {div_body3_p3}
        {div_body3_p4}
    </div>
</div>
"""


# 4. Abschnitt
div_body4_h = "Welche Rechte habe ich?"
div_body4_link = "https://www.datenschutz.uni-bonn.de."
div_body4_link = html.link('web', div_body4_link, div_body4_link)
div_body4_p1 = """
Sie haben das Recht, Auskunft über die zu Ihrer Person gespeicherten Daten zu erhalten (Art. 15 DS-GVO). 
Sollten unrichtige personenbezogene Daten verarbeitet werden, steht Ihnen ein Recht auf Berichtigung zu (Art. 16 DS-GVO). 
Liegen die gesetzlichen Voraussetzungen vor, so können Sie die Löschung oder Einschränkung der Verarbeitung verlangen sowie Widerspruch gegen die Verarbeitung einlegen (Art. 17, 18 und 21 DS-GVO).
"""
div_body4_p1 = html.paragraph(div_body4_p1)
div_body4_p2 = f"""
Sie können ebenfalls Kontakt mit dem Datenschutzbeauftragten der Universität Bonn aufnehmen: 
Dr. Jörg Hartmann, Genscherallee 3, 53113 Bonn, 
E-Mail: joerg.hartmann@uni-bonn.de, 
Tel: + 49 (0)228 -73 – 6758, 
{div_body4_link}
"""
div_body4_p2 = html.paragraph(div_body4_p2)
div_body4_p3 = """
Sie haben das Recht, sich mit einer Beschwerde an die zuständige Aufsichtsbehörde für Datenschutz zu wenden. 
Zuständige Aufsichtsbehörde: Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Postfach 20 04 44, 40102 Düsseldorf
"""
div_body4_p3 = html.paragraph(div_body4_p3)
div_body4_p4 = """
Die hier erklärte Einwilligung können Sie jederzeit ohne Angabe von Gründen und ohne persönlichen Nachteil mit Wirkung für die Zukunft widerrufen. 
Sofern Ihre Daten bereits anonymisiert wurden, können Ihnen diese aber nicht mehr zugeordnet werden.
Wir können Ihre Angaben also nicht aus dem Ergebnis „herausrechnen“.
"""
div_body4_p4 = html.paragraph(div_body4_p4)
div_body4 = f"""
<div class="consent-body-section">
    <div class="consent-body-section-h">
        {div_body4_h}
    </div>
    <div class="consent-body-section-p">
        {div_body4_p1}
        {div_body4_p2}
        {div_body4_p3}
        {div_body4_p4}
    </div>
</div>
"""


# 5. Abschnitt
div_body5_h = "Einwilligungserklärung"
div_body5_p1 = """
Hiermit willige ich in die Verarbeitung meiner personenbezogenen Daten für das Forschungsvorhaben ein. 
Die Einwilligung kann ich jederzeit widerrufen. 
Ich habe die Hinweise zur Verwendung meiner Daten und zu meinen Rechten in der Datenschutzerklärung zur Kenntnis genommen.
"""
div_body5_p1 = html.paragraph(div_body5_p1)
div_body5 = f"""
<div class="consent-body-section">
    <div class="consent-body-section-h">
        {div_body5_h}
    </div>
    <div class="consent-body-section-p">
        {div_body5_p1}
    </div>
</div>
"""


# Consent Body
div_body = f"""
<div class="consent-body border-dark alert">
{div_body1}
{div_body2}
{div_body3}
{div_body4}
{div_body5}
</div>
"""


# FORM
form_accept = f"""
<div id="id_ACCEPT" required="" class="consent-form">
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
Falls Sie Ihre Auswahl noch einmal ändern wollen, klicken Sie auf <em>"Auswahl ändern"</em>.
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
code = div_task + div_head + div_body + form_accept + div_modal + div_next + javascript_hideNext + javascript_selectAccept + css_consent
html.code(title, code, url)

