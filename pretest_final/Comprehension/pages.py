from ._builtin import Page


class Verstaendnis(Page):
    form_model = 'player'
    form_fields = [
        'COMPREHENSION_Q1',
        'COMPREHENSION_Q2',
        'COMPREHENSION_Q3',
        'COMPREHENSION_Q4',
    ]
    pass


page_sequence = [
    Verstaendnis
]
