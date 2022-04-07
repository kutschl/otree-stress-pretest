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


class Einverstaendniserklaerung(Page):
    form_model = 'player'
    form_fields = [
        'ACCEPT'
    ]


class Einverstaendniserklaerung_Anna(Page):
    form_model = 'player'
    form_fields = [
        'consent'
    ]


page_sequence = [
    Willkommen,
    Einverstaendniserklaerung,
    Einverstaendniserklaerung_Anna,
    Anmeldung,
]
