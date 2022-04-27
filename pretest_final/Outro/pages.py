from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Auszahlung(Page):
    def vars_for_template(self):
        self.player.setVariable_PAYOFF()
        self.player.setVariable_PAYOFF_RANDOM_BLOCK()
        self.player.setVariable_PAYOFF_RANDOM_TABLE()
        self.player.setVariable_PAYOFF_RANDOM_DECISION()
        self.player.setVariable_PAYOFF_PLAYER_OPTION()
        self.player.setVariable_PAYOFF_TABLE_TYPE()
        self.player.setVariable_PAYOFF_TABLE_ORDER()
        self.player.setVariable_PAYOFF_LOTTERY()


page_sequence = [Auszahlung]
