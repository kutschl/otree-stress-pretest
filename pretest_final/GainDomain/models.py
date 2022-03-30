import numpy as np
import pandas as pd
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ""


def loadLotteries(url: str, name: str):
    f1 = pd.read_excel(url, sheet_name=f'{name}_desc')
    f2 = pd.read_excel(url, sheet_name=f'{name}_asc')
    data = {}

    if f1.columns.tolist() != f2.columns.tolist():
        return None

    else:
        cols = f1.columns.tolist()
        cols.remove('asc')
        for col in cols:
            data[col] = []
            for f1row in np.arange(0, len(f1), 1):
                data[col].append(f1[col].loc[f1row])
            for f2row in np.arange(0, len(f2), 1):
                data[col].append(f2[col].loc[f2row])
        return data


lotteries = loadLotteries('_static/data/lotteries.xls', 'gain')


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
        'D1': getDecision(1),
        'D2': getDecision(2),
        'D3': getDecision(3),
        'D4': getDecision(4),
        'D5': getDecision(5),
        'D6': getDecision(6),
        'D7': getDecision(7),
        'D8': getDecision(8),
        'D9': getDecision(9),
        'D10': getDecision(10),
        'D11': getDecision(11),
        'D12': getDecision(12),
        'D13': getDecision(13),
        'D14': getDecision(14),
        'D15': getDecision(15),
        'D16': getDecision(16),
        'D17': getDecision(17),
        'D18': getDecision(18),
        'D19': getDecision(19),
        'D20': getDecision(20),
        'D21': getDecision(21),
        'D22': getDecision(22),
        'D23': getDecision(23),
        'D24': getDecision(24),
        'D25': getDecision(25),
        'D26': getDecision(26),
        'D27': getDecision(27),
        'D28': getDecision(28),
        'D29': getDecision(29),
        'D30': getDecision(30),
        'D31': getDecision(31),
        'D32': getDecision(32),
        'D33': getDecision(33),
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

    # Decision 2
    D2_1 = IntegerField("D2", 1)
    D2_2 = IntegerField("D2", 2)
    D2_3 = IntegerField("D2", 3)
    D2_4 = IntegerField("D2", 4)
    D2_5 = IntegerField("D2", 5)
    D2_6 = IntegerField("D2", 6)
    D2_7 = IntegerField("D2", 7)
    D2_8 = IntegerField("D2", 8)
    D2_9 = IntegerField("D2", 9)
    D2_10 = IntegerField("D2", 10)
    D2_11 = IntegerField("D2", 11)
    D2_12 = IntegerField("D2", 12)
    D2_13 = IntegerField("D2", 13)
    D2_14 = IntegerField("D2", 14)
    D2_15 = IntegerField("D2", 15)
    D2_16 = IntegerField("D2", 16)
    D2_17 = IntegerField("D2", 17)
    D2_18 = IntegerField("D2", 18)
    D2_19 = IntegerField("D2", 19)
    D2_20 = IntegerField("D2", 20)
    D2_21 = IntegerField("D2", 21)

    # Decision 3
    D3_1 = IntegerField("D3", 1)
    D3_2 = IntegerField("D3", 2)
    D3_3 = IntegerField("D3", 3)
    D3_4 = IntegerField("D3", 4)
    D3_5 = IntegerField("D3", 5)
    D3_6 = IntegerField("D3", 6)
    D3_7 = IntegerField("D3", 7)
    D3_8 = IntegerField("D3", 8)
    D3_9 = IntegerField("D3", 9)
    D3_10 = IntegerField("D3", 10)
    D3_11 = IntegerField("D3", 11)
    D3_12 = IntegerField("D3", 12)
    D3_13 = IntegerField("D3", 13)
    D3_14 = IntegerField("D3", 14)
    D3_15 = IntegerField("D3", 15)
    D3_16 = IntegerField("D3", 16)
    D3_17 = IntegerField("D3", 17)
    D3_18 = IntegerField("D3", 18)
    D3_19 = IntegerField("D3", 19)
    D3_20 = IntegerField("D3", 20)
    D3_21 = IntegerField("D3", 21)

    # Decision 4
    D4_1 = IntegerField("D4", 1)
    D4_2 = IntegerField("D4", 2)
    D4_3 = IntegerField("D4", 3)
    D4_4 = IntegerField("D4", 4)
    D4_5 = IntegerField("D4", 5)
    D4_6 = IntegerField("D4", 6)
    D4_7 = IntegerField("D4", 7)
    D4_8 = IntegerField("D4", 8)
    D4_9 = IntegerField("D4", 9)
    D4_10 = IntegerField("D4", 10)
    D4_11 = IntegerField("D4", 11)
    D4_12 = IntegerField("D4", 12)
    D4_13 = IntegerField("D4", 13)
    D4_14 = IntegerField("D4", 14)
    D4_15 = IntegerField("D4", 15)
    D4_16 = IntegerField("D4", 16)
    D4_17 = IntegerField("D4", 17)
    D4_18 = IntegerField("D4", 18)
    D4_19 = IntegerField("D4", 19)
    D4_20 = IntegerField("D4", 20)
    D4_21 = IntegerField("D4", 21)

    # Decision 5
    D5_1 = IntegerField("D5", 1)
    D5_2 = IntegerField("D5", 2)
    D5_3 = IntegerField("D5", 3)
    D5_4 = IntegerField("D5", 4)
    D5_5 = IntegerField("D5", 5)
    D5_6 = IntegerField("D5", 6)
    D5_7 = IntegerField("D5", 7)
    D5_8 = IntegerField("D5", 8)
    D5_9 = IntegerField("D5", 9)
    D5_10 = IntegerField("D5", 10)
    D5_11 = IntegerField("D5", 11)
    D5_12 = IntegerField("D5", 12)
    D5_13 = IntegerField("D5", 13)
    D5_14 = IntegerField("D5", 14)
    D5_15 = IntegerField("D5", 15)
    D5_16 = IntegerField("D5", 16)
    D5_17 = IntegerField("D5", 17)
    D5_18 = IntegerField("D5", 18)
    D5_19 = IntegerField("D5", 19)
    D5_20 = IntegerField("D5", 20)
    D5_21 = IntegerField("D5", 21)

    # Decision 6
    D6_1 = IntegerField("D6", 1)
    D6_2 = IntegerField("D6", 2)
    D6_3 = IntegerField("D6", 3)
    D6_4 = IntegerField("D6", 4)
    D6_5 = IntegerField("D6", 5)
    D6_6 = IntegerField("D6", 6)
    D6_7 = IntegerField("D6", 7)
    D6_8 = IntegerField("D6", 8)
    D6_9 = IntegerField("D6", 9)
    D6_10 = IntegerField("D6", 10)
    D6_11 = IntegerField("D6", 11)
    D6_12 = IntegerField("D6", 12)
    D6_13 = IntegerField("D6", 13)
    D6_14 = IntegerField("D6", 14)
    D6_15 = IntegerField("D6", 15)
    D6_16 = IntegerField("D6", 16)
    D6_17 = IntegerField("D6", 17)
    D6_18 = IntegerField("D6", 18)
    D6_19 = IntegerField("D6", 19)
    D6_20 = IntegerField("D6", 20)
    D6_21 = IntegerField("D6", 21)

    # Decision 7
    D7_1 = IntegerField("D7", 1)
    D7_2 = IntegerField("D7", 2)
    D7_3 = IntegerField("D7", 3)
    D7_4 = IntegerField("D7", 4)
    D7_5 = IntegerField("D7", 5)
    D7_6 = IntegerField("D7", 6)
    D7_7 = IntegerField("D7", 7)
    D7_8 = IntegerField("D7", 8)
    D7_9 = IntegerField("D7", 9)
    D7_10 = IntegerField("D7", 10)
    D7_11 = IntegerField("D7", 11)
    D7_12 = IntegerField("D7", 12)
    D7_13 = IntegerField("D7", 13)
    D7_14 = IntegerField("D7", 14)
    D7_15 = IntegerField("D7", 15)
    D7_16 = IntegerField("D7", 16)
    D7_17 = IntegerField("D7", 17)
    D7_18 = IntegerField("D7", 18)
    D7_19 = IntegerField("D7", 19)
    D7_20 = IntegerField("D7", 20)
    D7_21 = IntegerField("D7", 21)

    # Decision 8
    D8_1 = IntegerField("D8", 1)
    D8_2 = IntegerField("D8", 2)
    D8_3 = IntegerField("D8", 3)
    D8_4 = IntegerField("D8", 4)
    D8_5 = IntegerField("D8", 5)
    D8_6 = IntegerField("D8", 6)
    D8_7 = IntegerField("D8", 7)
    D8_8 = IntegerField("D8", 8)
    D8_9 = IntegerField("D8", 9)
    D8_10 = IntegerField("D8", 10)
    D8_11 = IntegerField("D8", 11)
    D8_12 = IntegerField("D8", 12)
    D8_13 = IntegerField("D8", 13)
    D8_14 = IntegerField("D8", 14)
    D8_15 = IntegerField("D8", 15)
    D8_16 = IntegerField("D8", 16)
    D8_17 = IntegerField("D8", 17)
    D8_18 = IntegerField("D8", 18)
    D8_19 = IntegerField("D8", 19)
    D8_20 = IntegerField("D8", 20)
    D8_21 = IntegerField("D8", 21)

    # Decision 9
    D9_1 = IntegerField("D9", 1)
    D9_2 = IntegerField("D9", 2)
    D9_3 = IntegerField("D9", 3)
    D9_4 = IntegerField("D9", 4)
    D9_5 = IntegerField("D9", 5)
    D9_6 = IntegerField("D9", 6)
    D9_7 = IntegerField("D9", 7)
    D9_8 = IntegerField("D9", 8)
    D9_9 = IntegerField("D9", 9)
    D9_10 = IntegerField("D9", 10)
    D9_11 = IntegerField("D9", 11)
    D9_12 = IntegerField("D9", 12)
    D9_13 = IntegerField("D9", 13)
    D9_14 = IntegerField("D9", 14)
    D9_15 = IntegerField("D9", 15)
    D9_16 = IntegerField("D9", 16)
    D9_17 = IntegerField("D9", 17)
    D9_18 = IntegerField("D9", 18)
    D9_19 = IntegerField("D9", 19)
    D9_20 = IntegerField("D9", 20)
    D9_21 = IntegerField("D9", 21)

    # Decision 10
    D10_1 = IntegerField("D10", 1)
    D10_2 = IntegerField("D10", 2)
    D10_3 = IntegerField("D10", 3)
    D10_4 = IntegerField("D10", 4)
    D10_5 = IntegerField("D10", 5)
    D10_6 = IntegerField("D10", 6)
    D10_7 = IntegerField("D10", 7)
    D10_8 = IntegerField("D10", 8)
    D10_9 = IntegerField("D10", 9)
    D10_10 = IntegerField("D10", 10)
    D10_11 = IntegerField("D10", 11)
    D10_12 = IntegerField("D10", 12)
    D10_13 = IntegerField("D10", 13)
    D10_14 = IntegerField("D10", 14)
    D10_15 = IntegerField("D10", 15)
    D10_16 = IntegerField("D10", 16)
    D10_17 = IntegerField("D10", 17)
    D10_18 = IntegerField("D10", 18)
    D10_19 = IntegerField("D10", 19)
    D10_20 = IntegerField("D10", 20)
    D10_21 = IntegerField("D10", 21)

    # Decision 11
    D11_1 = IntegerField("D11", 1)
    D11_2 = IntegerField("D11", 2)
    D11_3 = IntegerField("D11", 3)
    D11_4 = IntegerField("D11", 4)
    D11_5 = IntegerField("D11", 5)
    D11_6 = IntegerField("D11", 6)
    D11_7 = IntegerField("D11", 7)
    D11_8 = IntegerField("D11", 8)
    D11_9 = IntegerField("D11", 9)
    D11_10 = IntegerField("D11", 10)
    D11_11 = IntegerField("D11", 11)
    D11_12 = IntegerField("D11", 12)
    D11_13 = IntegerField("D11", 13)
    D11_14 = IntegerField("D11", 14)
    D11_15 = IntegerField("D11", 15)
    D11_16 = IntegerField("D11", 16)
    D11_17 = IntegerField("D11", 17)
    D11_18 = IntegerField("D11", 18)
    D11_19 = IntegerField("D11", 19)
    D11_20 = IntegerField("D11", 20)
    D11_21 = IntegerField("D11", 21)

    # Decision 12
    D12_1 = IntegerField("D12", 1)
    D12_2 = IntegerField("D12", 2)
    D12_3 = IntegerField("D12", 3)
    D12_4 = IntegerField("D12", 4)
    D12_5 = IntegerField("D12", 5)
    D12_6 = IntegerField("D12", 6)
    D12_7 = IntegerField("D12", 7)
    D12_8 = IntegerField("D12", 8)
    D12_9 = IntegerField("D12", 9)
    D12_10 = IntegerField("D12", 10)
    D12_11 = IntegerField("D12", 11)
    D12_12 = IntegerField("D12", 12)
    D12_13 = IntegerField("D12", 13)
    D12_14 = IntegerField("D12", 14)
    D12_15 = IntegerField("D12", 15)
    D12_16 = IntegerField("D12", 16)
    D12_17 = IntegerField("D12", 17)
    D12_18 = IntegerField("D12", 18)
    D12_19 = IntegerField("D12", 19)
    D12_20 = IntegerField("D12", 20)
    D12_21 = IntegerField("D12", 21)

    # Decision 13
    D13_1 = IntegerField("D13", 1)
    D13_2 = IntegerField("D13", 2)
    D13_3 = IntegerField("D13", 3)
    D13_4 = IntegerField("D13", 4)
    D13_5 = IntegerField("D13", 5)
    D13_6 = IntegerField("D13", 6)
    D13_7 = IntegerField("D13", 7)
    D13_8 = IntegerField("D13", 8)
    D13_9 = IntegerField("D13", 9)
    D13_10 = IntegerField("D13", 10)
    D13_11 = IntegerField("D13", 11)
    D13_12 = IntegerField("D13", 12)
    D13_13 = IntegerField("D13", 13)
    D13_14 = IntegerField("D13", 14)
    D13_15 = IntegerField("D13", 15)
    D13_16 = IntegerField("D13", 16)
    D13_17 = IntegerField("D13", 17)
    D13_18 = IntegerField("D13", 18)
    D13_19 = IntegerField("D13", 19)
    D13_20 = IntegerField("D13", 20)
    D13_21 = IntegerField("D13", 21)

    # Decision 14
    D14_1 = IntegerField("D14", 1)
    D14_2 = IntegerField("D14", 2)
    D14_3 = IntegerField("D14", 3)
    D14_4 = IntegerField("D14", 4)
    D14_5 = IntegerField("D14", 5)
    D14_6 = IntegerField("D14", 6)
    D14_7 = IntegerField("D14", 7)
    D14_8 = IntegerField("D14", 8)
    D14_9 = IntegerField("D14", 9)
    D14_10 = IntegerField("D14", 10)
    D14_11 = IntegerField("D14", 11)
    D14_12 = IntegerField("D14", 12)
    D14_13 = IntegerField("D14", 13)
    D14_14 = IntegerField("D14", 14)
    D14_15 = IntegerField("D14", 15)
    D14_16 = IntegerField("D14", 16)
    D14_17 = IntegerField("D14", 17)
    D14_18 = IntegerField("D14", 18)
    D14_19 = IntegerField("D14", 19)
    D14_20 = IntegerField("D14", 20)
    D14_21 = IntegerField("D14", 21)

    # Decision 15
    D15_1 = IntegerField("D15", 1)
    D15_2 = IntegerField("D15", 2)
    D15_3 = IntegerField("D15", 3)
    D15_4 = IntegerField("D15", 4)
    D15_5 = IntegerField("D15", 5)
    D15_6 = IntegerField("D15", 6)
    D15_7 = IntegerField("D15", 7)
    D15_8 = IntegerField("D15", 8)
    D15_9 = IntegerField("D15", 9)
    D15_10 = IntegerField("D15", 10)
    D15_11 = IntegerField("D15", 11)
    D15_12 = IntegerField("D15", 12)
    D15_13 = IntegerField("D15", 13)
    D15_14 = IntegerField("D15", 14)
    D15_15 = IntegerField("D15", 15)
    D15_16 = IntegerField("D15", 16)
    D15_17 = IntegerField("D15", 17)
    D15_18 = IntegerField("D15", 18)
    D15_19 = IntegerField("D15", 19)
    D15_20 = IntegerField("D15", 20)
    D15_21 = IntegerField("D15", 21)

    # Decision 16
    D16_1 = IntegerField("D16", 1)
    D16_2 = IntegerField("D16", 2)
    D16_3 = IntegerField("D16", 3)
    D16_4 = IntegerField("D16", 4)
    D16_5 = IntegerField("D16", 5)
    D16_6 = IntegerField("D16", 6)
    D16_7 = IntegerField("D16", 7)
    D16_8 = IntegerField("D16", 8)
    D16_9 = IntegerField("D16", 9)
    D16_10 = IntegerField("D16", 10)
    D16_11 = IntegerField("D16", 11)
    D16_12 = IntegerField("D16", 12)
    D16_13 = IntegerField("D16", 13)
    D16_14 = IntegerField("D16", 14)
    D16_15 = IntegerField("D16", 15)
    D16_16 = IntegerField("D16", 16)
    D16_17 = IntegerField("D16", 17)
    D16_18 = IntegerField("D16", 18)
    D16_19 = IntegerField("D16", 19)
    D16_20 = IntegerField("D16", 20)
    D16_21 = IntegerField("D16", 21)

    # Decision 17
    D17_1 = IntegerField("D17", 1)
    D17_2 = IntegerField("D17", 2)
    D17_3 = IntegerField("D17", 3)
    D17_4 = IntegerField("D17", 4)
    D17_5 = IntegerField("D17", 5)
    D17_6 = IntegerField("D17", 6)
    D17_7 = IntegerField("D17", 7)
    D17_8 = IntegerField("D17", 8)
    D17_9 = IntegerField("D17", 9)
    D17_10 = IntegerField("D17", 10)
    D17_11 = IntegerField("D17", 11)
    D17_12 = IntegerField("D17", 12)
    D17_13 = IntegerField("D17", 13)
    D17_14 = IntegerField("D17", 14)
    D17_15 = IntegerField("D17", 15)
    D17_16 = IntegerField("D17", 16)
    D17_17 = IntegerField("D17", 17)
    D17_18 = IntegerField("D17", 18)
    D17_19 = IntegerField("D17", 19)
    D17_20 = IntegerField("D17", 20)
    D17_21 = IntegerField("D17", 21)

    # Decision 18
    D18_1 = IntegerField("D18", 1)
    D18_2 = IntegerField("D18", 2)
    D18_3 = IntegerField("D18", 3)
    D18_4 = IntegerField("D18", 4)
    D18_5 = IntegerField("D18", 5)
    D18_6 = IntegerField("D18", 6)
    D18_7 = IntegerField("D18", 7)
    D18_8 = IntegerField("D18", 8)
    D18_9 = IntegerField("D18", 9)
    D18_10 = IntegerField("D18", 10)
    D18_11 = IntegerField("D18", 11)
    D18_12 = IntegerField("D18", 12)
    D18_13 = IntegerField("D18", 13)
    D18_14 = IntegerField("D18", 14)
    D18_15 = IntegerField("D18", 15)
    D18_16 = IntegerField("D18", 16)
    D18_17 = IntegerField("D18", 17)
    D18_18 = IntegerField("D18", 18)
    D18_19 = IntegerField("D18", 19)
    D18_20 = IntegerField("D18", 20)
    D18_21 = IntegerField("D18", 21)

    # Decision 19
    D19_1 = IntegerField("D19", 1)
    D19_2 = IntegerField("D19", 2)
    D19_3 = IntegerField("D19", 3)
    D19_4 = IntegerField("D19", 4)
    D19_5 = IntegerField("D19", 5)
    D19_6 = IntegerField("D19", 6)
    D19_7 = IntegerField("D19", 7)
    D19_8 = IntegerField("D19", 8)
    D19_9 = IntegerField("D19", 9)
    D19_10 = IntegerField("D19", 10)
    D19_11 = IntegerField("D19", 11)
    D19_12 = IntegerField("D19", 12)
    D19_13 = IntegerField("D19", 13)
    D19_14 = IntegerField("D19", 14)
    D19_15 = IntegerField("D19", 15)
    D19_16 = IntegerField("D19", 16)
    D19_17 = IntegerField("D19", 17)
    D19_18 = IntegerField("D19", 18)
    D19_19 = IntegerField("D19", 19)
    D19_20 = IntegerField("D19", 20)
    D19_21 = IntegerField("D19", 21)

    # Decision 20
    D20_1 = IntegerField("D20", 1)
    D20_2 = IntegerField("D20", 2)
    D20_3 = IntegerField("D20", 3)
    D20_4 = IntegerField("D20", 4)
    D20_5 = IntegerField("D20", 5)
    D20_6 = IntegerField("D20", 6)
    D20_7 = IntegerField("D20", 7)
    D20_8 = IntegerField("D20", 8)
    D20_9 = IntegerField("D20", 9)
    D20_10 = IntegerField("D20", 10)
    D20_11 = IntegerField("D20", 11)
    D20_12 = IntegerField("D20", 12)
    D20_13 = IntegerField("D20", 13)
    D20_14 = IntegerField("D20", 14)
    D20_15 = IntegerField("D20", 15)
    D20_16 = IntegerField("D20", 16)
    D20_17 = IntegerField("D20", 17)
    D20_18 = IntegerField("D20", 18)
    D20_19 = IntegerField("D20", 19)
    D20_20 = IntegerField("D20", 20)
    D20_21 = IntegerField("D20", 21)

    # Decision 21
    D21_1 = IntegerField("D21", 1)
    D21_2 = IntegerField("D21", 2)
    D21_3 = IntegerField("D21", 3)
    D21_4 = IntegerField("D21", 4)
    D21_5 = IntegerField("D21", 5)
    D21_6 = IntegerField("D21", 6)
    D21_7 = IntegerField("D21", 7)
    D21_8 = IntegerField("D21", 8)
    D21_9 = IntegerField("D21", 9)
    D21_10 = IntegerField("D21", 10)
    D21_11 = IntegerField("D21", 11)
    D21_12 = IntegerField("D21", 12)
    D21_13 = IntegerField("D21", 13)
    D21_14 = IntegerField("D21", 14)
    D21_15 = IntegerField("D21", 15)
    D21_16 = IntegerField("D21", 16)
    D21_17 = IntegerField("D21", 17)
    D21_18 = IntegerField("D21", 18)
    D21_19 = IntegerField("D21", 19)
    D21_20 = IntegerField("D21", 20)
    D21_21 = IntegerField("D21", 21)

    # Decision 22
    D22_1 = IntegerField("D22", 1)
    D22_2 = IntegerField("D22", 2)
    D22_3 = IntegerField("D22", 3)
    D22_4 = IntegerField("D22", 4)
    D22_5 = IntegerField("D22", 5)
    D22_6 = IntegerField("D22", 6)
    D22_7 = IntegerField("D22", 7)
    D22_8 = IntegerField("D22", 8)
    D22_9 = IntegerField("D22", 9)
    D22_10 = IntegerField("D22", 10)
    D22_11 = IntegerField("D22", 11)
    D22_12 = IntegerField("D22", 12)
    D22_13 = IntegerField("D22", 13)
    D22_14 = IntegerField("D22", 14)
    D22_15 = IntegerField("D22", 15)
    D22_16 = IntegerField("D22", 16)
    D22_17 = IntegerField("D22", 17)
    D22_18 = IntegerField("D22", 18)
    D22_19 = IntegerField("D22", 19)
    D22_20 = IntegerField("D22", 20)
    D22_21 = IntegerField("D22", 21)

    # Decision 23
    D23_1 = IntegerField("D23", 1)
    D23_2 = IntegerField("D23", 2)
    D23_3 = IntegerField("D23", 3)
    D23_4 = IntegerField("D23", 4)
    D23_5 = IntegerField("D23", 5)
    D23_6 = IntegerField("D23", 6)
    D23_7 = IntegerField("D23", 7)
    D23_8 = IntegerField("D23", 8)
    D23_9 = IntegerField("D23", 9)
    D23_10 = IntegerField("D23", 10)
    D23_11 = IntegerField("D23", 11)
    D23_12 = IntegerField("D23", 12)
    D23_13 = IntegerField("D23", 13)
    D23_14 = IntegerField("D23", 14)
    D23_15 = IntegerField("D23", 15)
    D23_16 = IntegerField("D23", 16)
    D23_17 = IntegerField("D23", 17)
    D23_18 = IntegerField("D23", 18)
    D23_19 = IntegerField("D23", 19)
    D23_20 = IntegerField("D23", 20)
    D23_21 = IntegerField("D23", 21)

    # Decision 24
    D24_1 = IntegerField("D24", 1)
    D24_2 = IntegerField("D24", 2)
    D24_3 = IntegerField("D24", 3)
    D24_4 = IntegerField("D24", 4)
    D24_5 = IntegerField("D24", 5)
    D24_6 = IntegerField("D24", 6)
    D24_7 = IntegerField("D24", 7)
    D24_8 = IntegerField("D24", 8)
    D24_9 = IntegerField("D24", 9)
    D24_10 = IntegerField("D24", 10)
    D24_11 = IntegerField("D24", 11)
    D24_12 = IntegerField("D24", 12)
    D24_13 = IntegerField("D24", 13)
    D24_14 = IntegerField("D24", 14)
    D24_15 = IntegerField("D24", 15)
    D24_16 = IntegerField("D24", 16)
    D24_17 = IntegerField("D24", 17)
    D24_18 = IntegerField("D24", 18)
    D24_19 = IntegerField("D24", 19)
    D24_20 = IntegerField("D24", 20)
    D24_21 = IntegerField("D24", 21)

    # Decision 25
    D25_1 = IntegerField("D25", 1)
    D25_2 = IntegerField("D25", 2)
    D25_3 = IntegerField("D25", 3)
    D25_4 = IntegerField("D25", 4)
    D25_5 = IntegerField("D25", 5)
    D25_6 = IntegerField("D25", 6)
    D25_7 = IntegerField("D25", 7)
    D25_8 = IntegerField("D25", 8)
    D25_9 = IntegerField("D25", 9)
    D25_10 = IntegerField("D25", 10)
    D25_11 = IntegerField("D25", 11)
    D25_12 = IntegerField("D25", 12)
    D25_13 = IntegerField("D25", 13)
    D25_14 = IntegerField("D25", 14)
    D25_15 = IntegerField("D25", 15)
    D25_16 = IntegerField("D25", 16)
    D25_17 = IntegerField("D25", 17)
    D25_18 = IntegerField("D25", 18)
    D25_19 = IntegerField("D25", 19)
    D25_20 = IntegerField("D25", 20)
    D25_21 = IntegerField("D25", 21)

    # Decision 26
    D26_1 = IntegerField("D26", 1)
    D26_2 = IntegerField("D26", 2)
    D26_3 = IntegerField("D26", 3)
    D26_4 = IntegerField("D26", 4)
    D26_5 = IntegerField("D26", 5)
    D26_6 = IntegerField("D26", 6)
    D26_7 = IntegerField("D26", 7)
    D26_8 = IntegerField("D26", 8)
    D26_9 = IntegerField("D26", 9)
    D26_10 = IntegerField("D26", 10)
    D26_11 = IntegerField("D26", 11)
    D26_12 = IntegerField("D26", 12)
    D26_13 = IntegerField("D26", 13)
    D26_14 = IntegerField("D26", 14)
    D26_15 = IntegerField("D26", 15)
    D26_16 = IntegerField("D26", 16)
    D26_17 = IntegerField("D26", 17)
    D26_18 = IntegerField("D26", 18)
    D26_19 = IntegerField("D26", 19)
    D26_20 = IntegerField("D26", 20)
    D26_21 = IntegerField("D26", 21)

    # Decision 27
    D27_1 = IntegerField("D27", 1)
    D27_2 = IntegerField("D27", 2)
    D27_3 = IntegerField("D27", 3)
    D27_4 = IntegerField("D27", 4)
    D27_5 = IntegerField("D27", 5)
    D27_6 = IntegerField("D27", 6)
    D27_7 = IntegerField("D27", 7)
    D27_8 = IntegerField("D27", 8)
    D27_9 = IntegerField("D27", 9)
    D27_10 = IntegerField("D27", 10)
    D27_11 = IntegerField("D27", 11)
    D27_12 = IntegerField("D27", 12)
    D27_13 = IntegerField("D27", 13)
    D27_14 = IntegerField("D27", 14)
    D27_15 = IntegerField("D27", 15)
    D27_16 = IntegerField("D27", 16)
    D27_17 = IntegerField("D27", 17)
    D27_18 = IntegerField("D27", 18)
    D27_19 = IntegerField("D27", 19)
    D27_20 = IntegerField("D27", 20)
    D27_21 = IntegerField("D27", 21)

    # Decision 28
    D28_1 = IntegerField("D28", 1)
    D28_2 = IntegerField("D28", 2)
    D28_3 = IntegerField("D28", 3)
    D28_4 = IntegerField("D28", 4)
    D28_5 = IntegerField("D28", 5)
    D28_6 = IntegerField("D28", 6)
    D28_7 = IntegerField("D28", 7)
    D28_8 = IntegerField("D28", 8)
    D28_9 = IntegerField("D28", 9)
    D28_10 = IntegerField("D28", 10)
    D28_11 = IntegerField("D28", 11)
    D28_12 = IntegerField("D28", 12)
    D28_13 = IntegerField("D28", 13)
    D28_14 = IntegerField("D28", 14)
    D28_15 = IntegerField("D28", 15)
    D28_16 = IntegerField("D28", 16)
    D28_17 = IntegerField("D28", 17)
    D28_18 = IntegerField("D28", 18)
    D28_19 = IntegerField("D28", 19)
    D28_20 = IntegerField("D28", 20)
    D28_21 = IntegerField("D28", 21)

    # Decision 29
    D29_1 = IntegerField("D29", 1)
    D29_2 = IntegerField("D29", 2)
    D29_3 = IntegerField("D29", 3)
    D29_4 = IntegerField("D29", 4)
    D29_5 = IntegerField("D29", 5)
    D29_6 = IntegerField("D29", 6)
    D29_7 = IntegerField("D29", 7)
    D29_8 = IntegerField("D29", 8)
    D29_9 = IntegerField("D29", 9)
    D29_10 = IntegerField("D29", 10)
    D29_11 = IntegerField("D29", 11)
    D29_12 = IntegerField("D29", 12)
    D29_13 = IntegerField("D29", 13)
    D29_14 = IntegerField("D29", 14)
    D29_15 = IntegerField("D29", 15)
    D29_16 = IntegerField("D29", 16)
    D29_17 = IntegerField("D29", 17)
    D29_18 = IntegerField("D29", 18)
    D29_19 = IntegerField("D29", 19)
    D29_20 = IntegerField("D29", 20)
    D29_21 = IntegerField("D29", 21)

    # Decision 30
    D30_1 = IntegerField("D30", 1)
    D30_2 = IntegerField("D30", 2)
    D30_3 = IntegerField("D30", 3)
    D30_4 = IntegerField("D30", 4)
    D30_5 = IntegerField("D30", 5)
    D30_6 = IntegerField("D30", 6)
    D30_7 = IntegerField("D30", 7)
    D30_8 = IntegerField("D30", 8)
    D30_9 = IntegerField("D30", 9)
    D30_10 = IntegerField("D30", 10)
    D30_11 = IntegerField("D30", 11)
    D30_12 = IntegerField("D30", 12)
    D30_13 = IntegerField("D30", 13)
    D30_14 = IntegerField("D30", 14)
    D30_15 = IntegerField("D30", 15)
    D30_16 = IntegerField("D30", 16)
    D30_17 = IntegerField("D30", 17)
    D30_18 = IntegerField("D30", 18)
    D30_19 = IntegerField("D30", 19)
    D30_20 = IntegerField("D30", 20)
    D30_21 = IntegerField("D30", 21)

    # Decision 31
    D31_1 = IntegerField("D31", 1)
    D31_2 = IntegerField("D31", 2)
    D31_3 = IntegerField("D31", 3)
    D31_4 = IntegerField("D31", 4)
    D31_5 = IntegerField("D31", 5)
    D31_6 = IntegerField("D31", 6)
    D31_7 = IntegerField("D31", 7)
    D31_8 = IntegerField("D31", 8)
    D31_9 = IntegerField("D31", 9)
    D31_10 = IntegerField("D31", 10)
    D31_11 = IntegerField("D31", 11)
    D31_12 = IntegerField("D31", 12)
    D31_13 = IntegerField("D31", 13)
    D31_14 = IntegerField("D31", 14)
    D31_15 = IntegerField("D31", 15)
    D31_16 = IntegerField("D31", 16)
    D31_17 = IntegerField("D31", 17)
    D31_18 = IntegerField("D31", 18)
    D31_19 = IntegerField("D31", 19)
    D31_20 = IntegerField("D31", 20)
    D31_21 = IntegerField("D31", 21)

    # Decision 32
    D32_1 = IntegerField("D32", 1)
    D32_2 = IntegerField("D32", 2)
    D32_3 = IntegerField("D32", 3)
    D32_4 = IntegerField("D32", 4)
    D32_5 = IntegerField("D32", 5)
    D32_6 = IntegerField("D32", 6)
    D32_7 = IntegerField("D32", 7)
    D32_8 = IntegerField("D32", 8)
    D32_9 = IntegerField("D32", 9)
    D32_10 = IntegerField("D32", 10)
    D32_11 = IntegerField("D32", 11)
    D32_12 = IntegerField("D32", 12)
    D32_13 = IntegerField("D32", 13)
    D32_14 = IntegerField("D32", 14)
    D32_15 = IntegerField("D32", 15)
    D32_16 = IntegerField("D32", 16)
    D32_17 = IntegerField("D32", 17)
    D32_18 = IntegerField("D32", 18)
    D32_19 = IntegerField("D32", 19)
    D32_20 = IntegerField("D32", 20)
    D32_21 = IntegerField("D32", 21)

    # Decision 33
    D33_1 = IntegerField("D33", 1)
    D33_2 = IntegerField("D33", 2)
    D33_3 = IntegerField("D33", 3)
    D33_4 = IntegerField("D33", 4)
    D33_5 = IntegerField("D33", 5)
    D33_6 = IntegerField("D33", 6)
    D33_7 = IntegerField("D33", 7)
    D33_8 = IntegerField("D33", 8)
    D33_9 = IntegerField("D33", 9)
    D33_10 = IntegerField("D33", 10)
    D33_11 = IntegerField("D33", 11)
    D33_12 = IntegerField("D33", 12)
    D33_13 = IntegerField("D33", 13)
    D33_14 = IntegerField("D33", 14)
    D33_15 = IntegerField("D33", 15)
    D33_16 = IntegerField("D33", 16)
    D33_17 = IntegerField("D33", 17)
    D33_18 = IntegerField("D33", 18)
    D33_19 = IntegerField("D33", 19)
    D33_20 = IntegerField("D33", 20)
    D33_21 = IntegerField("D33", 21)

