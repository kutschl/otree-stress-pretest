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


class Aufbau(Page):
    pass


class Beschreibung(Page):
    pass


page_sequence = [Willkommen, Anmeldung, Aufbau, Beschreibung]
