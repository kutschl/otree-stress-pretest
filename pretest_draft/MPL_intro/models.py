
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = ""
class Constants(BaseConstants):
    name_in_url = 'Einleitung'
    players_per_group = None

    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    right_side_amount_RTF = models.CurrencyField(initial=15)
    switching_point_RTF = models.CurrencyField()
    comm_2_RTF = models.StringField(label="Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen", blank=True)
    comm_3_RTF = models.StringField(label="Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen", blank=True)
    comm_4_RTF = models.StringField(label="Platz für Kommentare, falls Ihnen die Fragen auf dieser Seite unklar erscheinen", blank=True)

    def left_side_amounts_RTF(self):
        return (c(0),c(5),c(10),c(11),c(12),c(13),c(14),c(15),c(16),c(17),c(18),c(19),c(20),c(25),c(30))

    right_side_amount_HER = models.CurrencyField(initial=15)
    switching_point_HER = models.CurrencyField()
    comm_1_HER = models.StringField(label="Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen", blank=True)
    comm_2_HER = models.StringField(label="Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen", blank=True)
    comm_3_HER = models.StringField(label="Platz für Kommentare, falls Ihnen die Fragen auf dieser Seite unklar erscheinen", blank=True)

    def left_side_amounts_HER(self):
        return (c(0),c(5),c(10),c(11),c(12),c(13),c(14),c(15),c(16),c(17),c(18),c(19),c(20),c(25),c(30))
