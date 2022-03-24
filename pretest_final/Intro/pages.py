from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import string
import re


class Willkommen(Page):
    pass


class Anmeldung(Page):
    form_model = 'player'
    form_fields = [
        'VORNAME',
        'NACHNAME',
        'STRASSE',
        'PLZ',
        'STADT',
        'EMAIL',
        'IBAN',
        'BIC'
    ]

    def error_message(self, values):
        # # BIC-VALIDIERER:
        # if re.match('([a-zA-Z]{4}[a-zA-Z]{2}[a-zA-Z0-9]{2}([a-zA-Z0-9]{3})?)', values["bic"]) is None:
        #     return "Der von Ihnen eingegebene BIC-Code ist ungültig."
        pass


class Aufbau(Page):
    pass


class DemographischeAngaben(Page):
    form_model = 'player'
    form_fields = [
        'ALTER',
        'JOB',
        'GENDER'
    ]


page_sequence = [Willkommen, Anmeldung, Aufbau, DemographischeAngaben]
