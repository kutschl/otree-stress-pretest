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
    name_in_url = 'Comprehension'
    players_per_group = None
    num_rounds = 1


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
    pass