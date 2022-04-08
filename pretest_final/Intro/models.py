from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency,
)
import re
import math
from decimal import Decimal

doc = ''


class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1

    Alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    AlphabetDict = {}
    for n, l in enumerate(Alphabet):
        AlphabetDict.update([(l, n + 10)])


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Anmeldung
    VORNAME = models.StringField(label="Vorname")
    NACHNAME = models.StringField(label="Nachname")
    STRASSE = models.StringField(label="Straße und Hausnummer")
    PLZ = models.IntegerField(label="Postleitzahl")
    STADT = models.StringField(label="Stadt")
    EMAIL = models.StringField(label="E-Mail")
    IBAN = models.StringField(label="IBAN")
    BIC = models.StringField(label="BIC")

    # Fehlermeldung IBAN
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

    # Fehlermeldung BIC
    def BIC_error_message(self, value):
        if re.match('([a-zA-Z]{4}[a-zA-Z]{2}[a-zA-Z0-9]{2}([a-zA-Z0-9]{3})?)', value) is None:
            return "Der von Ihnen eingegebene BIC-Code ist ungültig."

    # Einverständniserklärung
    ACCEPT = models.BooleanField(
        label="Bitte wählen Sie aus, ob Sie in die Einverständniserklärung einwilligen.",
        choices=[
            [True, 'Ja, ich willige ein.'],
            [False, 'Nein, ich willige nicht ein.']
        ],
        widget=widgets.RadioSelect
    )
