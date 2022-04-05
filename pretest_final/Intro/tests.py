from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Willkommen,
        yield pages.Anmeldung, dict(
            VORNAME='Max',
            NACHNAME='Mustermann',
            STRASSE='Strasse 1',
            PLZ='01234',
            STADT='Stadt',
            EMAIL='email@email.at',
            IBAN='DE89370400440532013000',
            BIC='GENODED1HBO'
        ),
        yield pages.Aufbau,
        yield pages.Beschreibung,
        yield pages.Beispielaufgaben,
        yield pages.Gewinnbeispiel,
        yield pages.Verlustbeispiel,
        yield pages.Auszahlung,
        yield pages.Experimentstart
