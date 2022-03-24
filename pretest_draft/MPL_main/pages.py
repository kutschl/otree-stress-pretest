
from otree.api import Currency as c, currency_range
from .import models
from ._builtin import Page, WaitPage
from .models import Constants





class RTF_questions(Page):
    form_model = 'player'
    form_fields = ['switching_point_RTF','comm_4_RTF']
    def vars_for_template(self):
        amount=1
        return dict(
            amount=amount
        )
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A']
class HER_questions(Page):
    form_model = 'player'
    form_fields = ['switching_point_HER','comm_3_HER']
    def vars_for_template(self):
        amount=1
        return dict(
            amount=amount
        )
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']


page_sequence = [RTF_questions,HER_questions]
