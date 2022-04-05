from ._builtin import Page, WaitPage


class DemographischeAngaben(Page):
    form_model = 'player'
    form_fields = [
        'ALTER',
        'JOB',
        'GENDER'
    ]


page_sequence = [DemographischeAngaben]
