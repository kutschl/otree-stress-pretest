import random

from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.DemographischeAngaben, dict(
            ALTER=random.randint(18, 99),
            JOB=random.randint(0, 2),
            GENDER=random.randint(0, 3)
        )
