
from otree.api import Currency as c, currency_range
from .import models
from ._builtin import Page, WaitPage
from .models import Constants



class RTF_des2(Page):
    form_model = 'player'
    form_fields = ['comm_3_RTF']

class RTF_questions(Page):
    form_model = 'player'
    form_fields = ['switching_point_RTF','comm_4_RTF']
    def vars_for_template(self):
        amount=1
        return dict(
            amount=amount
        )

class HER_questions(Page):
    form_model = 'player'
    form_fields = ['switching_point_HER','comm_3_HER']
    def vars_for_template(self):
        amount=1
        return dict(
            amount=amount
        )



page_sequence = [RTF_des2,RTF_questions,HER_questions,RTF_des2]
