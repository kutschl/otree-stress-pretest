from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import string
import re


class DemographischeAngaben(Page):
    form_model = 'player'
    form_fields = [
        'ALTER',
        'JOB',
        'GENDER'
    ]


class Auszahlung(Page):
    pass


page_sequence = [DemographischeAngaben, Auszahlung]
