from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency,
)
import numpy as np


doc = ''


class Constants(BaseConstants):
    name_in_url = 'Instructions'
    players_per_group = None
    num_rounds = 1

    endowment_in_euro = 15
    multiplier = 15
    endowment_in_points = endowment_in_euro * multiplier

    decisions = 21
    gain_tables = 20
    loss_tables = 20
    blocks = 2
    tables_per_block = gain_tables + loss_tables
    tables = tables_per_block * blocks


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
