from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.DemographischeAngaben, dict(
            ALTER=10,
            JOB=0,
            GENDER=0
        )
