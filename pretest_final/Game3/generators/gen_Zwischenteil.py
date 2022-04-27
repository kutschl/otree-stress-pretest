from generators import HtmlGenerator as html
import numpy as np
import random as rd

# order = randomizeOrder()
order = [7, 4, 5, 9, 10, 12, 8, 15, 11, 13, 2, 16, 14, 1, 3, 6]


def codeModelsZwischenteilFields():
    code = '# ZWISCHENFRAGEN \n'
    for question in np.arange(1, 16+1, 1):
        code = code + f'ZWISCHENFRAGE{question} = ZwischenfragenField({question}) \n'
    return print(code)
# codeModelsZwischenteilFields()


def codeModelsZwischenteilForms():
    code = ''
    for question in np.arange(1, 16+1, 1):
        code = code + f'"ZWISCHENFRAGE{question}": getZwischenfragen({question}), \n'
    return print(code)
# codeModelsZwischenteilForms()


def randomizeOrder():
    numbers = np.arange(1, 16+1, 1)
    rd.shuffle(numbers)
    output = []
    numbers_pointer = 0
    for page in np.arange(0, 4, 1):
        output.append([])
        output[page] = []
        for question in np.arange(0, 4, 1):
            output[page].append(numbers[numbers_pointer])
            numbers_pointer = numbers_pointer + 1
    return output
# randomizeOrder()


def codeHtml(question: int, order: list):
    # INITS
    title = f'Zwischenteil ({question+1}/16)'
    filename = f'Zwischenteil{question+1}'
    url = f'../templates/Game/{filename}.html'

    css_Zwischenteil = open('gen_Zwischenteil.css').read()
    css_Zwischenteil = html.style(css_Zwischenteil)

    # CONTENT
    div_form = f"""        
        <div class="zwischenteil-form">
            <div class="zwischenteil-label">
                {{% form.ZWISCHENFRAGE{order[question]}.label %}}
            </div>
            {{% if Constants.forms_zwischenfragen.ZWISCHENFRAGE{order[question]}.image %}}
            <img src="{{% static 'images/zwischenfrage{order[question]}.png' %}}" alt="Zwischenteil: Frage {order[question]}" class="zwischenteil-img"/>
            {{% endif%}}
            <div class="zwischenteil-choices">
                {{% form.ZWISCHENFRAGE{order[question]} %}}
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
    code = div_form + div_next + css_Zwischenteil
    html.code(title, code, url)

for question in np.arange(0, 16, 1):
    codeHtml(question, order)



