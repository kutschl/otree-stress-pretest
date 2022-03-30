from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency,
    currency_range
)
import re
import math
from decimal import Decimal

doc = ''


class Constants(BaseConstants):
    name_in_url = 'Outro'
    players_per_group = None
    num_rounds = 1

    fix_payoff = Currency(4)

    contact = {
        'email': "schulzetilling@uni-bonn.de",
        'phone': "0123456789"
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # DEMOGRAPHISCHE ANGABEN
    ALTER = models.IntegerField(
        label="Bitte geben Sie Ihr Alter an."
    )

    JOB = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, 'Student/Studentin'],
            [1, 'Berufstätig'],
            [2, 'Keines zutreffend'],
        ],
        label="Was beschreibt Ihre berufliche Situation am Besten?"
    )

    GENDER = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [0, 'Männlich'],
            [1, 'Weiblich'],
            [2, 'Divers'],
            [3, 'Keine Angabe'],
        ],
        label="Mit welchem Geschlecht identifizieren Sie sich?"
    )

    ERWACHSENE = models.IntegerField(
        label="Anzahl der Erwachsenen in Ihrem Haushalt"
    )

    KINDER = models.IntegerField(
        label="Anzahl der Kinder in Ihrem Haushalt"
    )

