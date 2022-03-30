import numpy as np
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = ""
lotteries = {
    'p': [0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.9, 0.9, 0.9, 0.95, 0.95, 0.95],
    'x1': [20, 40, 50, 150, 10, 20, 50, 20, 40, 50, 10, 20, 40, 50, 50, 150, 20, 40, 50, 10, 20, 50, 20, 40, 50],
    'x2': [0, 10, 20, 50, 0, 10, 0, 0, 10, 20, 0, 10, 10, 0, 20, 0, 0, 10, 20, 0, 10, 0, 0, 10, 20],
    'b_start': [20, 40, 50, 150, 10, 20, 50, 20, 40, 50, 10, 20, 40, 50, 50, 150, 20, 40, 50, 10, 20, 50, 20, 40, 50],
    'b_end': [0, 10, 20, 50, 0, 10, 0, 0, 10, 20, 0, 10, 10, 0, 20, 0, 0, 10, 20, 0, 10, 0, 0, 10, 20],
    'b_step': [1, 1.5, 1.5, 5, 0.5, 0.5, 2.5, 1, 1.5, 1.5, 0.5, 0.5, 1.5, 2.5, 1.5, 7.5, 1, 1.5, 1.5, 0.5, 0.5, 2.5, 1, 1.5, 1.5]
}


def getNumbering(end):
    return np.arange(1, end + 1)


def getChoiceLabels(values):
    keys = getNumbering(len(values))
    return dict(zip(keys, values))


def getA(key):
    return {
        'p1': str("{0:.0%}".format(lotteries['p'][key])),
        'p2': str("{0:.0%}".format(1-lotteries['p'][key])),
        'x1': str("{:.2f}".format(lotteries['x1'][key])) + str(' Punkte'),
        'x2': str("{:.2f}".format(lotteries['x2'][key])) + str(' Punkte')
    }


def getB(key):
    output = []
    for i in np.arange(lotteries['b_start'][key], lotteries['b_end'][key] - lotteries['b_step'][key], (-1)*lotteries['b_step'][key]):
        output.append(str("{:.2f}".format(i)) + str(' Punkte'))
    return output


def getDecision(key: int):
    return {
        'Number': key,
        'Numbering': getNumbering(21).tolist(),
        'A': getA(key - 1),
        'B': getB(key - 1),
        'Choice': [
            [1, 'A'],
            [2, 'B']
        ],
        'ChoiceLabels': getChoiceLabels(getB(key - 1)),
        'Task': None,
        'Widget': widgets.RadioSelectHorizontal
    }


def IntegerField(name, number):
    return models.IntegerField(
        choices=Constants.forms[name]['Choice'],
        label=Constants.forms[name]['ChoiceLabels'][number],
        widget=Constants.forms[name]['Widget']
    )


class Constants(BaseConstants):
    name_in_url = 'GainDomain'
    players_per_group = None
    num_rounds = 1

    decisions_per_round = 21
    tables = len(lotteries['p'])

    forms = {
        'D1': getDecision(16)
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Decision 1
    D1_1 = IntegerField("D1", 1)
    D1_2 = IntegerField("D1", 2)
    D1_3 = IntegerField("D1", 3)
    D1_4 = IntegerField("D1", 4)
    D1_5 = IntegerField("D1", 5)
    D1_6 = IntegerField("D1", 6)
    D1_7 = IntegerField("D1", 7)
    D1_8 = IntegerField("D1", 8)
    D1_9 = IntegerField("D1", 9)
    D1_10 = IntegerField("D1", 10)
    D1_11 = IntegerField("D1", 11)
    D1_12 = IntegerField("D1", 12)
    D1_13 = IntegerField("D1", 13)
    D1_14 = IntegerField("D1", 14)
    D1_15 = IntegerField("D1", 15)
    D1_16 = IntegerField("D1", 16)
    D1_17 = IntegerField("D1", 17)
    D1_18 = IntegerField("D1", 18)
    D1_19 = IntegerField("D1", 19)
    D1_20 = IntegerField("D1", 20)
    D1_21 = IntegerField("D1", 21)

