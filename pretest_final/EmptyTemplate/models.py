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


class Constants(BaseConstants):
    name_in_url = 'EmptyTemplate'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass