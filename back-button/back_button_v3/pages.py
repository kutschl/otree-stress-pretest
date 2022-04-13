from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction_Page(Page):
  form_model = 'player'

  form_fields = ['q1', 'q2']

  def error_message(self, value):
     return self.player.set_error_message(value)



page_sequence = [
	Instruction_Page
]
