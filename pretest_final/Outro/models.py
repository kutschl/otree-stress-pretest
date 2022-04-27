from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency
)

doc = ''


class Constants(BaseConstants):
    name_in_url = 'Outro'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def setVariable_PAYOFF(self):
        self.PAYOFF = self.participant.vars['payoff']

    def setVariable_PAYOFF_RANDOM_BLOCK(self):
        self.PAYOFF_RANDOM_BLOCK = self.participant.vars['payoff_random_block']

    def setVariable_PAYOFF_RANDOM_TABLE(self):
        self.PAYOFF_RANDOM_TABLE = self.participant.vars['payoff_random_table']

    def setVariable_PAYOFF_RANDOM_DECISION(self):
        self.PAYOFF_RANDOM_DECISION = self.participant.vars['payoff_random_decision']

    def setVariable_PAYOFF_PLAYER_OPTION(self):
        self.PAYOFF_PLAYER_OPTION = self.participant.vars['payoff_player_option']

    def setVariable_PAYOFF_TABLE_TYPE(self):
        self.PAYOFF_TABLE_TYPE = self.participant.vars['payoff_table_type']

    def setVariable_PAYOFF_TABLE_ORDER(self):
        self.PAYOFF_TABLE_ORDER = self.participant.vars['payoff_table_order']

    def setVariable_PAYOFF_LOTTERY(self):
        self.PAYOFF_LOTTERY = self.participant.vars['payoff_lottery']

    PAYOFF = models.CurrencyField()
    PAYOFF_RANDOM_BLOCK = models.IntegerField()
    PAYOFF_RANDOM_TABLE = models.IntegerField()
    PAYOFF_RANDOM_DECISION = models.IntegerField()
    PAYOFF_PLAYER_OPTION = models.IntegerField()
    PAYOFF_TABLE_TYPE = models.IntegerField()
    PAYOFF_TABLE_ORDER = models.IntegerField()
    PAYOFF_LOTTERY = models.IntegerField()
