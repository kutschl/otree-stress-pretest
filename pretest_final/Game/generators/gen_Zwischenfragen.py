from generators import HtmlGenerator as html
import numpy as np
import random as rd

# order = randomizeOrder()
order = [[7, 4, 5, 9], [10, 12, 8, 15], [11, 13, 2, 16], [14, 1, 3, 6]]


def codeModelsZwischenfragenFields():
    code = '# ZWISCHENFRAGEN \n'
    for question in np.arange(1, 16+1, 1):
        code = code + f'ZWISCHENFRAGE{question} = ZwischenfragenField({question}) \n'
    return print(code)
# codeModelsZwischenfragenFields()


def codeModelsZwischenfragenForms():
    code = ''
    for question in np.arange(1, 16+1, 1):
        code = code + f'"ZWISCHENFRAGE{question}": getZwischenfragen({question}), \n'
    return print(code)
# codeModelsZwischenfragenForms()


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


def codeHtml(page: int, order: list):
    # INITS
    title = f'Zwischenfragen ({page}/4)'
    filename = f'Zwischenfragen{page}'
    url = f'../templates/Game/{filename}.html'

    css_Zwischenfragen = open('gen_Zwischenfragen.css').read()
    css_Zwischenfragen = html.style(css_Zwischenfragen)

    # CONTENT
    pointer = 1
    for question in np.arange(0, len(order[page-1]), 1):
        globals()[f'div_form{pointer}'] = f"""        
        <div class="zwischenfrage-form">
            <div class="zwischenfrage-label">
                {{% form.ZWISCHENFRAGE{order[page-1][question]}.label %}}
            </div>
            {{% if Constants.forms_zwischenfragen.ZWISCHENFRAGE{order[page-1][question]}.image %}}
            <img src="{{% static 'images/zwischenfrage{order[page-1][question]}.png' %}}" alt="Zwischenfrage {order[page-1][question]}" class="zwischenfrage-img"/>
            {{% endif%}}
            <div class="zwischenfrage-choices">
                {{% form.ZWISCHENFRAGE{order[page-1][question]} %}}
            </div>
        </div>
        """
        pointer = pointer + 1



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
    code = div_form1 + div_form2 + div_form3 + div_form4 + div_next + css_Zwischenfragen
    html.code(title, code, url)
# for page in np.arange(1, 4+1, 1):
#     codeHtml(page, order)



