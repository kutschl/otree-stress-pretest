from . import pages
from ._builtin import Bot


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Aufbau,
        yield pages.Beschreibung1,
        yield pages.Beschreibung2
