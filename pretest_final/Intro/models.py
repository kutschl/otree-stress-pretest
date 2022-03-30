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
import numpy as np
from decimal import Decimal

doc = ''


def getB(start, end, step):
    output = []
    for i in np.arange(start, end, step):
        output.append(str("{:.2f}".format(i)) + str(' Punkte'))
    return output


class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1

    fix_payoff = Currency(4)
    extra_payoff_lower_limit = Currency(0)
    extra_payoff_upper_limit = Currency(100)

    multiplier = 0.1
    example_points = 10
    example_payoff = Currency(example_points*multiplier)

    tables = 50
    decisions_per_table = 21

    # Kontaktinformationen
    contact = {
        'email': "schulzetilling@uni-bonn.de",
        'phone': "0123456789"
    }

    # IBAN Validator
    Alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    AlphabetDict = {}
    for n, l in enumerate(Alphabet):
        AlphabetDict.update([(l, n + 10)])

    # Beispiel 1: Gewinnsituation
    ExampleGainValues = {
        'A': [0.5, 20, 0],
        'B': getB(20, -0.5, -1)
    }

    ExampleGain = {
        'Title': "Bsp: Gewinnsituation",
        'Numbering': np.arange(1, 22, 1).tolist(),
        'A': {
            'p1': str("{0:.0%}".format(ExampleGainValues['A'][0])),
            'p2': str("{0:.0%}".format(1-ExampleGainValues['A'][0])),
            'x1': str("{:.2f}".format(ExampleGainValues['A'][1])) + str(' Punkte'),
            'x2': str("{:.2f}".format(ExampleGainValues['A'][2])) + str(' Punkte')
        },
        'B': ExampleGainValues['B']
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # ANMELDUNG
    VORNAME = models.StringField(label="Vorname")
    NACHNAME = models.StringField(label="Nachname")
    STRASSE = models.StringField(label="Straße und Hausnummer")
    PLZ = models.IntegerField(label="Postleitzahl")
    STADT = models.StringField(label="Stadt")
    EMAIL = models.StringField(label="E-Mail")
    IBAN = models.StringField(label="IBAN")
    BIC = models.StringField(label="BIC")

    def IBAN_error_message(self, value):
        reordered_iban = list(value)[4:len(value)] + list(value)[0:4]
        numeric_iban = ""
        invalid_chars = 0
        for l in range(len(value)):
            if reordered_iban[l] == " ":
                return "Bitte verwenden Sie keine Leerzeichen."
            if reordered_iban[l] in Constants.Alphabet:
                numeric_iban += str(Constants.AlphabetDict[reordered_iban[l]])
            elif reordered_iban[l] in [str(x) for x in range(10)]:
                numeric_iban += reordered_iban[l]
            else:
                invalid_chars += 1
        if invalid_chars > 0:
            return "Ihre Eingabe enthält ungültige zeichen. Bitte verwenden Sie nur Ziffern und Großbuchstaben."
        elif round(Decimal(numeric_iban) - math.floor(Decimal(numeric_iban) / 97) * 97) != 1:
            return "Die IBAN ist ungültig. Bitte überprüfen Sie Ihre Eingabe."

    def BIC_error_message(self, value):
        if re.match('([a-zA-Z]{4}[a-zA-Z]{2}[a-zA-Z0-9]{2}([a-zA-Z0-9]{3})?)', value) is None:
            return "Der von Ihnen eingegebene BIC-Code ist ungültig."
