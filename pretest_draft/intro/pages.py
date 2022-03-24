
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import string
import re


class Willkommen(Page):

    form_model = 'player'
    form_fields = ['vorname','nachname','straße','plz','stadt', 'email', 'iban', 'bic']
    def error_message(self, values):


        ###IBAN VALIDIERUNG BEGINNT HIER
        valid_codes = ["AL", "AT", "BE", "BG", "CH", "CH", "CY", "CZ", "DE", "DK",
                      "EE", "ES", "FI", "FR", "GB", "GR", "HR", "HU",
                      "IE", "IS", "IT", "LI", "LT", "LU", "LV", "MC",
                      "MT", "NL", "NO", "PL", "PT", "RO", "SE", "SI",
                      "SK", "SM"]


        len_dict = {"AT": 20, "EE": 20, "LT": 20, "LU": 20, "BE": 16, "BG": 22, "DE": 22, "GB": 22,
                   "IE": 22, "CH": 21, "HR": 21, "LI": 21, "LV": 21, "CY": 28, "HU": 28, "PL": 28,
                   "CZ": 24, "ES": 24, "RO": 24, "SE": 24, "SK": 24, "DK": 18, "FI": 18, "NL": 18,
                   "FR": 27, "GR": 27, "IT": 27, "MC": 27, "SM": 27, "IS": 26, "MT": 31, "NO": 15,
                   "PT": 25, "SI": 19, "AL": 28}


        LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}

        iban = values["iban"]

        IBAN = iban.upper()

        IBAN = IBAN.replace(" ", "")

        c1 = False
        c2 = False
        c3 = False
        c4 = False

        country = IBAN[0:2]

        c1 = country in valid_codes

        if c1:

            c2 = len_dict[country] == len(IBAN)

        if c1 and c2:


            temp = IBAN[:2] + '00' + IBAN[4:]

            number_iban = (temp[4:] + temp[:4]).translate(LETTERS)


            check_digits = '{:0>2}'.format(98 - (int(number_iban) % 97))

            c3 = check_digits == IBAN[2:4]

        if c1 and c2 and c3:

            _number_iban = (IBAN[4:] + IBAN[:4]).translate(LETTERS)

            c4 = int(_number_iban) % 97 == 1

        if not (c1 and c2 and c3 and c4):
            return "Die von Ihnen angegebene IBAN ist nicht gültig. Bitte überprüfen Sie Ihre Eingabe."

        #check no small letters in iban
        for c in values["iban"]:
            if c.islower():
                return "Die von Ihnen angegebene IBAN enthält Kleinbuchstaben."

        ###IBAN VALIDIERUNG ENDET HIER

        #check basic @ structure in email
        if(re.match("[^@]+@[^@]+\.[^@]+", values["email"]) == None):
            return "Die von Ihnen eingegebene E-Mail-Adresse ist ungültig."

        #check no spaces in email address
        if (' ' in values["email"]) == True:
            return "Die von Ihnen eingegebene E-Mail-Adresse enthält Leerzeichen."

        #valide BIC code
        if(re.match('([a-zA-Z]{4}[a-zA-Z]{2}[a-zA-Z0-9]{2}([a-zA-Z0-9]{3})?)', values["bic"]) == None):
            return "Der von Ihnen eingegebene BIC-Code ist ungültig."

class Einleitung(Page):

    form_model = 'player'

class First_questions(Page):

    form_model = 'player'
    form_fields = ['alter','job','gender']

class First(Page):

    form_model = 'player'

page_sequence = [First, Willkommen, Einleitung, First_questions]
