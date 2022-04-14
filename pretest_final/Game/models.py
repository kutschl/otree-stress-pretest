import numpy as np
import pandas as pd
import random as rd
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ""


def loadLotteries(url: str, sheet: str):
    f = pd.read_excel(url, sheet_name=f'{sheet}')
    d = {
        'type': []
    }
    cols = f.columns.tolist()
    for col in cols:
        d[col] = []
        for row in np.arange(0, len(f), 1):
            d[col].append(f[col].loc[row])
    for row in np.arange(0, len(f), 1):
        d['type'].append(sheet)
    return d


gain_data = loadLotteries('_static/data/lotteries.xls', 'GAIN')
loss_data = loadLotteries('_static/data/lotteries.xls', 'LOSS')


def separateLotteries(d: dict) -> list[dict]:
    d1 = dict(d)
    d2 = dict(d)
    d1['asc'] = []
    d2['asc'] = []
    for i in np.arange(0, len(d[list(d.keys())[0]]), 1):
        randomizer = rd.choice([True, False])
        if randomizer is True:
            d1['asc'].append(randomizer)
            d2['asc'].append(not randomizer)
        if randomizer is False:
            d1['asc'].append(randomizer)
            d2['asc'].append(not randomizer)
    return [d1, d2]


gain_data = separateLotteries(gain_data)
loss_data = separateLotteries(loss_data)


def getOptionA(data: list[dict], block: int, table: int) -> dict:
    return {
        'p1': str("{0:.0%}".format(data[block]['p'][table])),
        'p2': str("{0:.0%}".format(1-data[block]['p'][table])),
        'x1': str("{:.2f}".format(data[block]['x1'][table])) + str(' Punkte'),
        'x2': str("{:.2f}".format(data[block]['x2'][table])) + str(' Punkte')
    }


def getOptionB(data: list[dict], block: int, table: int) -> list:
    li = []
    b_start = data[block]['x1'][table]
    b_step = (-1)*(data[block]['x1'][table] - data[block]['x2'][table])/20
    b_stop = data[block]['x2'][table] + b_step
    for i in np.arange(b_start, b_stop, b_step):
        li.append(str("{:.2f}".format(i)) + str(' Punkte'))
    if data[block]['asc'][table] is True:
        li.reverse()
    return li


def getTable(block: int, table: int, typ: str) -> dict:
    data = None
    if typ is str('GAIN'):
        data = gain_data
    if typ is str('LOSS'):
        data = loss_data
    return {
        'Number': table,
        'Numbering': np.arange(1, 21 + 1).tolist(),
        'A': getOptionA(data, block-1, table-1),
        'B': getOptionB(data, block-1, table-1),
        'Typ': typ,
        'ASC': data[block-1]['asc'][table-1],
        'Choice': [
            [1, 'A'],
            [2, 'B']
        ],
        'Widget': widgets.RadioSelectHorizontal
    }


def getPayoffOptionB(block: int, table: int, decision: int, typ: str):
    data = None
    if typ is str('GAIN'):
        data = gain_data
    if typ is str('LOSS'):
        data = loss_data
    li = []
    b_start = data[block-1]['x1'][table-1]
    b_step = (-1)*(data[block-1]['x1'][table-1] - data[block-1]['x2'][table-1])/20
    b_stop = data[block-1]['x2'][table-1] + b_step
    for i in np.arange(b_start, b_stop, b_step):
        li.append(i)
    if data[block-1]['asc'][table-1] is True:
        li.reverse()
    return li[decision-1]


def getPayoffOptionA(block: int, table: int, typ: str):
    data = None
    if typ is str('GAIN'):
        data = gain_data
    if typ is str('LOSS'):
        data = loss_data
    return {
        'p': data[block-1]['p'][table-1],
        'x1': data[block-1]['x1'][table-1],
        'x2': data[block-1]['x2'][table-1]
    }


def TableField(name, number):
    return models.IntegerField(
        choices=Constants.forms_tabellen[name]['Choice'],
        label=Constants.forms_tabellen[name]['ASC'],
        widget=Constants.forms_tabellen[name]['Widget']
    )


zwischenfragen_data = {
    1: {
        'label': 'Welche der Zahlen ist ein Fünftel eines Viertels von einem Neuntel von 900?',
        'choices': [
            [1, '2'],
            [2, '3'],
            [3, '4'],
            [4, '5'],
            [5, '6'],
            [6, '7']
        ],
        'answer': 4,
        'img': False,
    },
    2: {
        'label': 'Anne ist größer als Bob und Christian ist kleiner als Anne. Welche der folgenden Aussagen ist die genaueste?',
        'choices': [
            [1, 'Christian ist größer als Bob'],
            [2, 'Christian ist kleiner als Bob'],
            [3, 'Christian ist genauso groß wie Bob'],
            [4, 'Es ist nicht möglich, dies anhand der gegebenen Informationen zu beurteilen']
        ],
        'answer': 4,
        'img': False,
    },
    3: {
        'label': 'Joshua ist 12 Jahre alt und seine Schwester ist dreimal so alt wie er. Wenn Joshua 23 Jahre alt ist, wie alt wird dann seine Schwester sein?',
        'choices': [
            [1, '35'],
            [2, '39'],
            [3, '44'],
            [4, '47'],
            [5, '53'],
            [6, '57']
        ],
        'answer': 4,
        'img': False,
    },
    4: {
        'label': 'Wenn der Tag nach morgen zwei Tage vor Donnerstag ist, welcher Tag ist dann heute?',
        'choices': [
            [1, 'Freitag'],
            [2, 'Montag'],
            [3, 'Mittwoch'],
            [4, 'Samstag'],
            [5, 'Dienstag'],
            [6, 'Sonntag']
        ],
        'answer': 6,
        'img': False,
    },
    5: {
        'label': 'Welcher Buchstabe kommt in der folgenden alphanumerischen Folge als nächstes? K N P S U',
        'choices': [
            [1, 'S'],
            [2, 'T'],
            [3, 'U'],
            [4, 'V'],
            [5, 'W'],
            [6, 'X']
        ],
        'answer': 6,
        'img': False,
    },
    6: {
        'label': 'Welcher Buchstabe kommt in der folgenden alphanumerischen Folge als nächstes? V Q M J H',
        'choices': [
            [1, 'E'],
            [2, 'F'],
            [3, 'G'],
            [4, 'H'],
            [5, 'I'],
            [6, 'J']
        ],
        'answer': 3,
        'img': False,
    },
    7: {
        'label': 'Welcher Buchstabe kommt in der folgenden alphanumerischen Folge als nächstes? I J L O S',
        'choices': [
            [1, 'T'],
            [2, 'U'],
            [3, 'V'],
            [4, 'X'],
            [5, 'Y'],
            [6, 'Z']
        ],
        'answer': 4,
        'img': False,
    },
    8: {
        'label': 'Welcher Buchstabe kommt in der folgenden alphanumerischen Folge als nächstes? Q S N P L',
        'choices': [
            [1, 'J'],
            [2, 'H'],
            [3, 'I'],
            [4, 'N'],
            [5, 'M'],
            [6, 'L']
        ],
        'answer': 4,
        'img': False,
    },
    9: {
        'label': 'Welcher Bildausschnitt passt zu dem Muster?',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F']
        ],
        'answer': 5,
        'img': True,
    },
    10: {
        'label': 'Welcher Bildausschnitt passt zu dem Muster?',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F']
        ],
        'answer': 2,
        'img': True,
    },
    11: {
        'label': 'Welcher Bildausschnitt passt zu dem Muster?',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F']
        ],
        'answer': 2,
        'img': True,
    },
    12: {
        'label': 'Welcher Bildausschnitt passt zu dem Muster?',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F']
        ],
        'answer': 4,
        'img': True,
    },
    13: {
        'label': 'Alle unten abgebildeten Würfel haben auf jeder Seite ein anderes Bild. Wählen Sie die Antwortmöglichkeit aus, die eine Drehung des Würfels X darstellt.',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'],
            [7, 'G'],
            [8, 'H']
        ],
        'answer': 3,
        'img': True,
    },
    14: {
        'label': 'Alle unten abgebildeten Würfel haben auf jeder Seite ein anderes Bild. Wählen Sie die Antwortmöglichkeit aus, die eine Drehung des Würfels X darstellt.',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'],
            [7, 'G'],
            [8, 'H']
        ],
        'answer': 2,
        'img': True,
    },
    15: {
        'label': 'Alle unten abgebildeten Würfel haben auf jeder Seite ein anderes Bild. Wählen Sie die Antwortmöglichkeit aus, die eine Drehung des Würfels X darstellt.',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'],
            [7, 'G'],
            [8, 'H']
        ],
        'answer': 6,
        'img': True,
    },
    16: {
        'label': 'Alle unten abgebildeten Würfel haben auf jeder Seite ein anderes Bild. Wählen Sie die Antwortmöglichkeit aus, die eine Drehung des Würfels X darstellt.',
        'choices': [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'],
            [7, 'G'],
            [8, 'H']
        ],
        'answer': 7,
        'img': True,
    },
}


def getZwischenfragen(question: int):
    return {
        'label': zwischenfragen_data[question]['label'],
        'choices': zwischenfragen_data[question]['choices'],
        'image': zwischenfragen_data[question]['img'],
        'answer': zwischenfragen_data[question]['answer']
    }


def ZwischenfragenField(question: int) -> models.IntegerField:
    return models.IntegerField(
        choices=zwischenfragen_data[question]['choices'],
        label=zwischenfragen_data[question]['label'],
        widget=widgets.RadioSelect,
        image=True
    )


class Constants(BaseConstants):
    name_in_url = 'Game'
    players_per_group = None
    num_rounds = 1

    multiplier = 15
    endowment_in_euro = 15
    endowment_in_points = endowment_in_euro * multiplier

    gain_tables_per_block = len(gain_data[0][list(gain_data[0].keys())[0]])
    loss_tables_per_block = len(loss_data[0][list(loss_data[0].keys())[0]])
    tables_per_block = gain_tables_per_block + loss_tables_per_block
    blocks = 2
    tables = blocks * tables_per_block
    decisions_per_table = 21

    forms_tabellen = {
        'B1_GAIN1': getTable(1, 1, 'GAIN'),
        'B1_GAIN2': getTable(1, 2, 'GAIN'),
        'B1_GAIN3': getTable(1, 3, 'GAIN'),
        'B1_GAIN4': getTable(1, 4, 'GAIN'),
        'B1_GAIN5': getTable(1, 5, 'GAIN'),
        'B1_GAIN6': getTable(1, 6, 'GAIN'),
        'B1_GAIN7': getTable(1, 7, 'GAIN'),
        'B1_GAIN8': getTable(1, 8, 'GAIN'),
        'B1_GAIN9': getTable(1, 9, 'GAIN'),
        'B1_GAIN10': getTable(1, 10, 'GAIN'),
        'B1_GAIN11': getTable(1, 11, 'GAIN'),
        'B1_GAIN12': getTable(1, 12, 'GAIN'),
        'B1_GAIN13': getTable(1, 13, 'GAIN'),
        'B1_GAIN14': getTable(1, 14, 'GAIN'),
        'B1_GAIN15': getTable(1, 15, 'GAIN'),
        'B1_GAIN16': getTable(1, 16, 'GAIN'),
        'B1_GAIN17': getTable(1, 17, 'GAIN'),
        'B1_GAIN18': getTable(1, 18, 'GAIN'),
        'B1_GAIN19': getTable(1, 19, 'GAIN'),
        'B1_GAIN20': getTable(1, 20, 'GAIN'),


        'B1_LOSS1': getTable(1, 1, 'LOSS'),
        'B1_LOSS2': getTable(1, 2, 'LOSS'),
        'B1_LOSS3': getTable(1, 3, 'LOSS'),
        'B1_LOSS4': getTable(1, 4, 'LOSS'),
        'B1_LOSS5': getTable(1, 5, 'LOSS'),
        'B1_LOSS6': getTable(1, 6, 'LOSS'),
        'B1_LOSS7': getTable(1, 7, 'LOSS'),
        'B1_LOSS8': getTable(1, 8, 'LOSS'),
        'B1_LOSS9': getTable(1, 9, 'LOSS'),
        'B1_LOSS10': getTable(1, 10, 'LOSS'),
        'B1_LOSS11': getTable(1, 11, 'LOSS'),
        'B1_LOSS12': getTable(1, 12, 'LOSS'),
        'B1_LOSS13': getTable(1, 13, 'LOSS'),
        'B1_LOSS14': getTable(1, 14, 'LOSS'),
        'B1_LOSS15': getTable(1, 15, 'LOSS'),
        'B1_LOSS16': getTable(1, 16, 'LOSS'),
        'B1_LOSS17': getTable(1, 17, 'LOSS'),
        'B1_LOSS18': getTable(1, 18, 'LOSS'),
        'B1_LOSS19': getTable(1, 19, 'LOSS'),
        'B1_LOSS20': getTable(1, 20, 'LOSS'),


        'B2_GAIN1': getTable(2, 1, 'GAIN'),
        'B2_GAIN2': getTable(2, 2, 'GAIN'),
        'B2_GAIN3': getTable(2, 3, 'GAIN'),
        'B2_GAIN4': getTable(2, 4, 'GAIN'),
        'B2_GAIN5': getTable(2, 5, 'GAIN'),
        'B2_GAIN6': getTable(2, 6, 'GAIN'),
        'B2_GAIN7': getTable(2, 7, 'GAIN'),
        'B2_GAIN8': getTable(2, 8, 'GAIN'),
        'B2_GAIN9': getTable(2, 9, 'GAIN'),
        'B2_GAIN10': getTable(2, 10, 'GAIN'),
        'B2_GAIN11': getTable(2, 11, 'GAIN'),
        'B2_GAIN12': getTable(2, 12, 'GAIN'),
        'B2_GAIN13': getTable(2, 13, 'GAIN'),
        'B2_GAIN14': getTable(2, 14, 'GAIN'),
        'B2_GAIN15': getTable(2, 15, 'GAIN'),
        'B2_GAIN16': getTable(2, 16, 'GAIN'),
        'B2_GAIN17': getTable(2, 17, 'GAIN'),
        'B2_GAIN18': getTable(2, 18, 'GAIN'),
        'B2_GAIN19': getTable(2, 19, 'GAIN'),
        'B2_GAIN20': getTable(2, 20, 'GAIN'),


        'B2_LOSS1': getTable(2, 1, 'LOSS'),
        'B2_LOSS2': getTable(2, 2, 'LOSS'),
        'B2_LOSS3': getTable(2, 3, 'LOSS'),
        'B2_LOSS4': getTable(2, 4, 'LOSS'),
        'B2_LOSS5': getTable(2, 5, 'LOSS'),
        'B2_LOSS6': getTable(2, 6, 'LOSS'),
        'B2_LOSS7': getTable(2, 7, 'LOSS'),
        'B2_LOSS8': getTable(2, 8, 'LOSS'),
        'B2_LOSS9': getTable(2, 9, 'LOSS'),
        'B2_LOSS10': getTable(2, 10, 'LOSS'),
        'B2_LOSS11': getTable(2, 11, 'LOSS'),
        'B2_LOSS12': getTable(2, 12, 'LOSS'),
        'B2_LOSS13': getTable(2, 13, 'LOSS'),
        'B2_LOSS14': getTable(2, 14, 'LOSS'),
        'B2_LOSS15': getTable(2, 15, 'LOSS'),
        'B2_LOSS16': getTable(2, 16, 'LOSS'),
        'B2_LOSS17': getTable(2, 17, 'LOSS'),
        'B2_LOSS18': getTable(2, 18, 'LOSS'),
        'B2_LOSS19': getTable(2, 19, 'LOSS'),
        'B2_LOSS20': getTable(2, 20, 'LOSS'),
    }

    forms_zwischenfragen = {
        "ZWISCHENFRAGE1": getZwischenfragen(1),
        "ZWISCHENFRAGE2": getZwischenfragen(2),
        "ZWISCHENFRAGE3": getZwischenfragen(3),
        "ZWISCHENFRAGE4": getZwischenfragen(4),
        "ZWISCHENFRAGE5": getZwischenfragen(5),
        "ZWISCHENFRAGE6": getZwischenfragen(6),
        "ZWISCHENFRAGE7": getZwischenfragen(7),
        "ZWISCHENFRAGE8": getZwischenfragen(8),
        "ZWISCHENFRAGE9": getZwischenfragen(9),
        "ZWISCHENFRAGE10": getZwischenfragen(10),
        "ZWISCHENFRAGE11": getZwischenfragen(11),
        "ZWISCHENFRAGE12": getZwischenfragen(12),
        "ZWISCHENFRAGE13": getZwischenfragen(13),
        "ZWISCHENFRAGE14": getZwischenfragen(14),
        "ZWISCHENFRAGE15": getZwischenfragen(15),
        "ZWISCHENFRAGE16": getZwischenfragen(16),
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # ZWISCHENFRAGEN
    ZWISCHENFRAGE1 = ZwischenfragenField(1)
    ZWISCHENFRAGE2 = ZwischenfragenField(2)
    ZWISCHENFRAGE3 = ZwischenfragenField(3)
    ZWISCHENFRAGE4 = ZwischenfragenField(4)
    ZWISCHENFRAGE5 = ZwischenfragenField(5)
    ZWISCHENFRAGE6 = ZwischenfragenField(6)
    ZWISCHENFRAGE7 = ZwischenfragenField(7)
    ZWISCHENFRAGE8 = ZwischenfragenField(8)
    ZWISCHENFRAGE9 = ZwischenfragenField(9)
    ZWISCHENFRAGE10 = ZwischenfragenField(10)
    ZWISCHENFRAGE11 = ZwischenfragenField(11)
    ZWISCHENFRAGE12 = ZwischenfragenField(12)
    ZWISCHENFRAGE13 = ZwischenfragenField(13)
    ZWISCHENFRAGE14 = ZwischenfragenField(14)
    ZWISCHENFRAGE15 = ZwischenfragenField(15)
    ZWISCHENFRAGE16 = ZwischenfragenField(16)

# AUSZAHLUNGSFUNKTION
    def setPayoff(self):
        # Randomizer
        rd_typ = rd.choice(['GAIN', 'LOSS'])
        rd_block = rd.randint(1, 2)
        rd_table = rd.randint(1, 20)
        rd_decision = rd.randint(1, 21)

        # Player Decision
        player_decision = self.__class__.__dict__[f'B{rd_block}_{rd_typ}{rd_table}_D{rd_decision}']

        # Payoff Info
        self.participant.vars['payoff_rd_typ'] = rd_typ
        self.participant.vars['payoff_rd_block'] = rd_block
        self.participant.vars['payoff_rd_table'] = rd_table
        self.participant.vars['payoff_rd_decision'] = rd_decision
        self.participant.vars['endowment'] = c(Constants.endowment_in_euro)

        # Payoff Calc
        if player_decision == 1:
            # Option A
            urn = []
            for _ in np.arange(0, getPayoffOptionA(rd_block, rd_table, rd_typ)['p'] * 100, 1):
                urn.append(getPayoffOptionA(rd_block, rd_table, rd_typ)['x1'])
            for _ in np.arange(0, (1-getPayoffOptionA(rd_block, rd_table, rd_typ)['p'])*100, 1):
                urn.append(getPayoffOptionA(rd_block, rd_table, rd_typ)['x2'])
            rd.shuffle(urn)
            self.payoff = c(
                Constants.endowment_in_euro + (urn[rd.randint(0, 99)] / Constants.multiplier)
            )
            self.participant.vars['payoff_player_decision'] = 1
            self.participant.vars['payoff'] = self.payoff
        else:
            # Option B
            self.payoff = c(
                Constants.endowment_in_euro + (getPayoffOptionB(rd_block, rd_table, rd_decision, rd_typ) / Constants.multiplier)
            )
            self.participant.vars['payoff_player_decision'] = 2
            self.participant.vars['payoff'] = self.payoff

    # BLOCK 1 GEWINN TABELLE 1
    B1_GAIN1_D1 = TableField("B1_GAIN1", 1)
    B1_GAIN1_D2 = TableField("B1_GAIN1", 2)
    B1_GAIN1_D3 = TableField("B1_GAIN1", 3)
    B1_GAIN1_D4 = TableField("B1_GAIN1", 4)
    B1_GAIN1_D5 = TableField("B1_GAIN1", 5)
    B1_GAIN1_D6 = TableField("B1_GAIN1", 6)
    B1_GAIN1_D7 = TableField("B1_GAIN1", 7)
    B1_GAIN1_D8 = TableField("B1_GAIN1", 8)
    B1_GAIN1_D9 = TableField("B1_GAIN1", 9)
    B1_GAIN1_D10 = TableField("B1_GAIN1", 10)
    B1_GAIN1_D11 = TableField("B1_GAIN1", 11)
    B1_GAIN1_D12 = TableField("B1_GAIN1", 12)
    B1_GAIN1_D13 = TableField("B1_GAIN1", 13)
    B1_GAIN1_D14 = TableField("B1_GAIN1", 14)
    B1_GAIN1_D15 = TableField("B1_GAIN1", 15)
    B1_GAIN1_D16 = TableField("B1_GAIN1", 16)
    B1_GAIN1_D17 = TableField("B1_GAIN1", 17)
    B1_GAIN1_D18 = TableField("B1_GAIN1", 18)
    B1_GAIN1_D19 = TableField("B1_GAIN1", 19)
    B1_GAIN1_D20 = TableField("B1_GAIN1", 20)
    B1_GAIN1_D21 = TableField("B1_GAIN1", 21)

    # BLOCK 1 GEWINN TABELLE 2
    B1_GAIN2_D1 = TableField("B1_GAIN2", 1)
    B1_GAIN2_D2 = TableField("B1_GAIN2", 2)
    B1_GAIN2_D3 = TableField("B1_GAIN2", 3)
    B1_GAIN2_D4 = TableField("B1_GAIN2", 4)
    B1_GAIN2_D5 = TableField("B1_GAIN2", 5)
    B1_GAIN2_D6 = TableField("B1_GAIN2", 6)
    B1_GAIN2_D7 = TableField("B1_GAIN2", 7)
    B1_GAIN2_D8 = TableField("B1_GAIN2", 8)
    B1_GAIN2_D9 = TableField("B1_GAIN2", 9)
    B1_GAIN2_D10 = TableField("B1_GAIN2", 10)
    B1_GAIN2_D11 = TableField("B1_GAIN2", 11)
    B1_GAIN2_D12 = TableField("B1_GAIN2", 12)
    B1_GAIN2_D13 = TableField("B1_GAIN2", 13)
    B1_GAIN2_D14 = TableField("B1_GAIN2", 14)
    B1_GAIN2_D15 = TableField("B1_GAIN2", 15)
    B1_GAIN2_D16 = TableField("B1_GAIN2", 16)
    B1_GAIN2_D17 = TableField("B1_GAIN2", 17)
    B1_GAIN2_D18 = TableField("B1_GAIN2", 18)
    B1_GAIN2_D19 = TableField("B1_GAIN2", 19)
    B1_GAIN2_D20 = TableField("B1_GAIN2", 20)
    B1_GAIN2_D21 = TableField("B1_GAIN2", 21)

    # BLOCK 1 GEWINN TABELLE 3
    B1_GAIN3_D1 = TableField("B1_GAIN3", 1)
    B1_GAIN3_D2 = TableField("B1_GAIN3", 2)
    B1_GAIN3_D3 = TableField("B1_GAIN3", 3)
    B1_GAIN3_D4 = TableField("B1_GAIN3", 4)
    B1_GAIN3_D5 = TableField("B1_GAIN3", 5)
    B1_GAIN3_D6 = TableField("B1_GAIN3", 6)
    B1_GAIN3_D7 = TableField("B1_GAIN3", 7)
    B1_GAIN3_D8 = TableField("B1_GAIN3", 8)
    B1_GAIN3_D9 = TableField("B1_GAIN3", 9)
    B1_GAIN3_D10 = TableField("B1_GAIN3", 10)
    B1_GAIN3_D11 = TableField("B1_GAIN3", 11)
    B1_GAIN3_D12 = TableField("B1_GAIN3", 12)
    B1_GAIN3_D13 = TableField("B1_GAIN3", 13)
    B1_GAIN3_D14 = TableField("B1_GAIN3", 14)
    B1_GAIN3_D15 = TableField("B1_GAIN3", 15)
    B1_GAIN3_D16 = TableField("B1_GAIN3", 16)
    B1_GAIN3_D17 = TableField("B1_GAIN3", 17)
    B1_GAIN3_D18 = TableField("B1_GAIN3", 18)
    B1_GAIN3_D19 = TableField("B1_GAIN3", 19)
    B1_GAIN3_D20 = TableField("B1_GAIN3", 20)
    B1_GAIN3_D21 = TableField("B1_GAIN3", 21)

    # BLOCK 1 GEWINN TABELLE 4
    B1_GAIN4_D1 = TableField("B1_GAIN4", 1)
    B1_GAIN4_D2 = TableField("B1_GAIN4", 2)
    B1_GAIN4_D3 = TableField("B1_GAIN4", 3)
    B1_GAIN4_D4 = TableField("B1_GAIN4", 4)
    B1_GAIN4_D5 = TableField("B1_GAIN4", 5)
    B1_GAIN4_D6 = TableField("B1_GAIN4", 6)
    B1_GAIN4_D7 = TableField("B1_GAIN4", 7)
    B1_GAIN4_D8 = TableField("B1_GAIN4", 8)
    B1_GAIN4_D9 = TableField("B1_GAIN4", 9)
    B1_GAIN4_D10 = TableField("B1_GAIN4", 10)
    B1_GAIN4_D11 = TableField("B1_GAIN4", 11)
    B1_GAIN4_D12 = TableField("B1_GAIN4", 12)
    B1_GAIN4_D13 = TableField("B1_GAIN4", 13)
    B1_GAIN4_D14 = TableField("B1_GAIN4", 14)
    B1_GAIN4_D15 = TableField("B1_GAIN4", 15)
    B1_GAIN4_D16 = TableField("B1_GAIN4", 16)
    B1_GAIN4_D17 = TableField("B1_GAIN4", 17)
    B1_GAIN4_D18 = TableField("B1_GAIN4", 18)
    B1_GAIN4_D19 = TableField("B1_GAIN4", 19)
    B1_GAIN4_D20 = TableField("B1_GAIN4", 20)
    B1_GAIN4_D21 = TableField("B1_GAIN4", 21)

    # BLOCK 1 GEWINN TABELLE 5
    B1_GAIN5_D1 = TableField("B1_GAIN5", 1)
    B1_GAIN5_D2 = TableField("B1_GAIN5", 2)
    B1_GAIN5_D3 = TableField("B1_GAIN5", 3)
    B1_GAIN5_D4 = TableField("B1_GAIN5", 4)
    B1_GAIN5_D5 = TableField("B1_GAIN5", 5)
    B1_GAIN5_D6 = TableField("B1_GAIN5", 6)
    B1_GAIN5_D7 = TableField("B1_GAIN5", 7)
    B1_GAIN5_D8 = TableField("B1_GAIN5", 8)
    B1_GAIN5_D9 = TableField("B1_GAIN5", 9)
    B1_GAIN5_D10 = TableField("B1_GAIN5", 10)
    B1_GAIN5_D11 = TableField("B1_GAIN5", 11)
    B1_GAIN5_D12 = TableField("B1_GAIN5", 12)
    B1_GAIN5_D13 = TableField("B1_GAIN5", 13)
    B1_GAIN5_D14 = TableField("B1_GAIN5", 14)
    B1_GAIN5_D15 = TableField("B1_GAIN5", 15)
    B1_GAIN5_D16 = TableField("B1_GAIN5", 16)
    B1_GAIN5_D17 = TableField("B1_GAIN5", 17)
    B1_GAIN5_D18 = TableField("B1_GAIN5", 18)
    B1_GAIN5_D19 = TableField("B1_GAIN5", 19)
    B1_GAIN5_D20 = TableField("B1_GAIN5", 20)
    B1_GAIN5_D21 = TableField("B1_GAIN5", 21)

    # BLOCK 1 GEWINN TABELLE 6
    B1_GAIN6_D1 = TableField("B1_GAIN6", 1)
    B1_GAIN6_D2 = TableField("B1_GAIN6", 2)
    B1_GAIN6_D3 = TableField("B1_GAIN6", 3)
    B1_GAIN6_D4 = TableField("B1_GAIN6", 4)
    B1_GAIN6_D5 = TableField("B1_GAIN6", 5)
    B1_GAIN6_D6 = TableField("B1_GAIN6", 6)
    B1_GAIN6_D7 = TableField("B1_GAIN6", 7)
    B1_GAIN6_D8 = TableField("B1_GAIN6", 8)
    B1_GAIN6_D9 = TableField("B1_GAIN6", 9)
    B1_GAIN6_D10 = TableField("B1_GAIN6", 10)
    B1_GAIN6_D11 = TableField("B1_GAIN6", 11)
    B1_GAIN6_D12 = TableField("B1_GAIN6", 12)
    B1_GAIN6_D13 = TableField("B1_GAIN6", 13)
    B1_GAIN6_D14 = TableField("B1_GAIN6", 14)
    B1_GAIN6_D15 = TableField("B1_GAIN6", 15)
    B1_GAIN6_D16 = TableField("B1_GAIN6", 16)
    B1_GAIN6_D17 = TableField("B1_GAIN6", 17)
    B1_GAIN6_D18 = TableField("B1_GAIN6", 18)
    B1_GAIN6_D19 = TableField("B1_GAIN6", 19)
    B1_GAIN6_D20 = TableField("B1_GAIN6", 20)
    B1_GAIN6_D21 = TableField("B1_GAIN6", 21)

    # BLOCK 1 GEWINN TABELLE 7
    B1_GAIN7_D1 = TableField("B1_GAIN7", 1)
    B1_GAIN7_D2 = TableField("B1_GAIN7", 2)
    B1_GAIN7_D3 = TableField("B1_GAIN7", 3)
    B1_GAIN7_D4 = TableField("B1_GAIN7", 4)
    B1_GAIN7_D5 = TableField("B1_GAIN7", 5)
    B1_GAIN7_D6 = TableField("B1_GAIN7", 6)
    B1_GAIN7_D7 = TableField("B1_GAIN7", 7)
    B1_GAIN7_D8 = TableField("B1_GAIN7", 8)
    B1_GAIN7_D9 = TableField("B1_GAIN7", 9)
    B1_GAIN7_D10 = TableField("B1_GAIN7", 10)
    B1_GAIN7_D11 = TableField("B1_GAIN7", 11)
    B1_GAIN7_D12 = TableField("B1_GAIN7", 12)
    B1_GAIN7_D13 = TableField("B1_GAIN7", 13)
    B1_GAIN7_D14 = TableField("B1_GAIN7", 14)
    B1_GAIN7_D15 = TableField("B1_GAIN7", 15)
    B1_GAIN7_D16 = TableField("B1_GAIN7", 16)
    B1_GAIN7_D17 = TableField("B1_GAIN7", 17)
    B1_GAIN7_D18 = TableField("B1_GAIN7", 18)
    B1_GAIN7_D19 = TableField("B1_GAIN7", 19)
    B1_GAIN7_D20 = TableField("B1_GAIN7", 20)
    B1_GAIN7_D21 = TableField("B1_GAIN7", 21)

    # BLOCK 1 GEWINN TABELLE 8
    B1_GAIN8_D1 = TableField("B1_GAIN8", 1)
    B1_GAIN8_D2 = TableField("B1_GAIN8", 2)
    B1_GAIN8_D3 = TableField("B1_GAIN8", 3)
    B1_GAIN8_D4 = TableField("B1_GAIN8", 4)
    B1_GAIN8_D5 = TableField("B1_GAIN8", 5)
    B1_GAIN8_D6 = TableField("B1_GAIN8", 6)
    B1_GAIN8_D7 = TableField("B1_GAIN8", 7)
    B1_GAIN8_D8 = TableField("B1_GAIN8", 8)
    B1_GAIN8_D9 = TableField("B1_GAIN8", 9)
    B1_GAIN8_D10 = TableField("B1_GAIN8", 10)
    B1_GAIN8_D11 = TableField("B1_GAIN8", 11)
    B1_GAIN8_D12 = TableField("B1_GAIN8", 12)
    B1_GAIN8_D13 = TableField("B1_GAIN8", 13)
    B1_GAIN8_D14 = TableField("B1_GAIN8", 14)
    B1_GAIN8_D15 = TableField("B1_GAIN8", 15)
    B1_GAIN8_D16 = TableField("B1_GAIN8", 16)
    B1_GAIN8_D17 = TableField("B1_GAIN8", 17)
    B1_GAIN8_D18 = TableField("B1_GAIN8", 18)
    B1_GAIN8_D19 = TableField("B1_GAIN8", 19)
    B1_GAIN8_D20 = TableField("B1_GAIN8", 20)
    B1_GAIN8_D21 = TableField("B1_GAIN8", 21)

    # BLOCK 1 GEWINN TABELLE 9
    B1_GAIN9_D1 = TableField("B1_GAIN9", 1)
    B1_GAIN9_D2 = TableField("B1_GAIN9", 2)
    B1_GAIN9_D3 = TableField("B1_GAIN9", 3)
    B1_GAIN9_D4 = TableField("B1_GAIN9", 4)
    B1_GAIN9_D5 = TableField("B1_GAIN9", 5)
    B1_GAIN9_D6 = TableField("B1_GAIN9", 6)
    B1_GAIN9_D7 = TableField("B1_GAIN9", 7)
    B1_GAIN9_D8 = TableField("B1_GAIN9", 8)
    B1_GAIN9_D9 = TableField("B1_GAIN9", 9)
    B1_GAIN9_D10 = TableField("B1_GAIN9", 10)
    B1_GAIN9_D11 = TableField("B1_GAIN9", 11)
    B1_GAIN9_D12 = TableField("B1_GAIN9", 12)
    B1_GAIN9_D13 = TableField("B1_GAIN9", 13)
    B1_GAIN9_D14 = TableField("B1_GAIN9", 14)
    B1_GAIN9_D15 = TableField("B1_GAIN9", 15)
    B1_GAIN9_D16 = TableField("B1_GAIN9", 16)
    B1_GAIN9_D17 = TableField("B1_GAIN9", 17)
    B1_GAIN9_D18 = TableField("B1_GAIN9", 18)
    B1_GAIN9_D19 = TableField("B1_GAIN9", 19)
    B1_GAIN9_D20 = TableField("B1_GAIN9", 20)
    B1_GAIN9_D21 = TableField("B1_GAIN9", 21)

    # BLOCK 1 GEWINN TABELLE 10
    B1_GAIN10_D1 = TableField("B1_GAIN10", 1)
    B1_GAIN10_D2 = TableField("B1_GAIN10", 2)
    B1_GAIN10_D3 = TableField("B1_GAIN10", 3)
    B1_GAIN10_D4 = TableField("B1_GAIN10", 4)
    B1_GAIN10_D5 = TableField("B1_GAIN10", 5)
    B1_GAIN10_D6 = TableField("B1_GAIN10", 6)
    B1_GAIN10_D7 = TableField("B1_GAIN10", 7)
    B1_GAIN10_D8 = TableField("B1_GAIN10", 8)
    B1_GAIN10_D9 = TableField("B1_GAIN10", 9)
    B1_GAIN10_D10 = TableField("B1_GAIN10", 10)
    B1_GAIN10_D11 = TableField("B1_GAIN10", 11)
    B1_GAIN10_D12 = TableField("B1_GAIN10", 12)
    B1_GAIN10_D13 = TableField("B1_GAIN10", 13)
    B1_GAIN10_D14 = TableField("B1_GAIN10", 14)
    B1_GAIN10_D15 = TableField("B1_GAIN10", 15)
    B1_GAIN10_D16 = TableField("B1_GAIN10", 16)
    B1_GAIN10_D17 = TableField("B1_GAIN10", 17)
    B1_GAIN10_D18 = TableField("B1_GAIN10", 18)
    B1_GAIN10_D19 = TableField("B1_GAIN10", 19)
    B1_GAIN10_D20 = TableField("B1_GAIN10", 20)
    B1_GAIN10_D21 = TableField("B1_GAIN10", 21)

    # BLOCK 1 GEWINN TABELLE 11
    B1_GAIN11_D1 = TableField("B1_GAIN11", 1)
    B1_GAIN11_D2 = TableField("B1_GAIN11", 2)
    B1_GAIN11_D3 = TableField("B1_GAIN11", 3)
    B1_GAIN11_D4 = TableField("B1_GAIN11", 4)
    B1_GAIN11_D5 = TableField("B1_GAIN11", 5)
    B1_GAIN11_D6 = TableField("B1_GAIN11", 6)
    B1_GAIN11_D7 = TableField("B1_GAIN11", 7)
    B1_GAIN11_D8 = TableField("B1_GAIN11", 8)
    B1_GAIN11_D9 = TableField("B1_GAIN11", 9)
    B1_GAIN11_D10 = TableField("B1_GAIN11", 10)
    B1_GAIN11_D11 = TableField("B1_GAIN11", 11)
    B1_GAIN11_D12 = TableField("B1_GAIN11", 12)
    B1_GAIN11_D13 = TableField("B1_GAIN11", 13)
    B1_GAIN11_D14 = TableField("B1_GAIN11", 14)
    B1_GAIN11_D15 = TableField("B1_GAIN11", 15)
    B1_GAIN11_D16 = TableField("B1_GAIN11", 16)
    B1_GAIN11_D17 = TableField("B1_GAIN11", 17)
    B1_GAIN11_D18 = TableField("B1_GAIN11", 18)
    B1_GAIN11_D19 = TableField("B1_GAIN11", 19)
    B1_GAIN11_D20 = TableField("B1_GAIN11", 20)
    B1_GAIN11_D21 = TableField("B1_GAIN11", 21)

    # BLOCK 1 GEWINN TABELLE 12
    B1_GAIN12_D1 = TableField("B1_GAIN12", 1)
    B1_GAIN12_D2 = TableField("B1_GAIN12", 2)
    B1_GAIN12_D3 = TableField("B1_GAIN12", 3)
    B1_GAIN12_D4 = TableField("B1_GAIN12", 4)
    B1_GAIN12_D5 = TableField("B1_GAIN12", 5)
    B1_GAIN12_D6 = TableField("B1_GAIN12", 6)
    B1_GAIN12_D7 = TableField("B1_GAIN12", 7)
    B1_GAIN12_D8 = TableField("B1_GAIN12", 8)
    B1_GAIN12_D9 = TableField("B1_GAIN12", 9)
    B1_GAIN12_D10 = TableField("B1_GAIN12", 10)
    B1_GAIN12_D11 = TableField("B1_GAIN12", 11)
    B1_GAIN12_D12 = TableField("B1_GAIN12", 12)
    B1_GAIN12_D13 = TableField("B1_GAIN12", 13)
    B1_GAIN12_D14 = TableField("B1_GAIN12", 14)
    B1_GAIN12_D15 = TableField("B1_GAIN12", 15)
    B1_GAIN12_D16 = TableField("B1_GAIN12", 16)
    B1_GAIN12_D17 = TableField("B1_GAIN12", 17)
    B1_GAIN12_D18 = TableField("B1_GAIN12", 18)
    B1_GAIN12_D19 = TableField("B1_GAIN12", 19)
    B1_GAIN12_D20 = TableField("B1_GAIN12", 20)
    B1_GAIN12_D21 = TableField("B1_GAIN12", 21)

    # BLOCK 1 GEWINN TABELLE 13
    B1_GAIN13_D1 = TableField("B1_GAIN13", 1)
    B1_GAIN13_D2 = TableField("B1_GAIN13", 2)
    B1_GAIN13_D3 = TableField("B1_GAIN13", 3)
    B1_GAIN13_D4 = TableField("B1_GAIN13", 4)
    B1_GAIN13_D5 = TableField("B1_GAIN13", 5)
    B1_GAIN13_D6 = TableField("B1_GAIN13", 6)
    B1_GAIN13_D7 = TableField("B1_GAIN13", 7)
    B1_GAIN13_D8 = TableField("B1_GAIN13", 8)
    B1_GAIN13_D9 = TableField("B1_GAIN13", 9)
    B1_GAIN13_D10 = TableField("B1_GAIN13", 10)
    B1_GAIN13_D11 = TableField("B1_GAIN13", 11)
    B1_GAIN13_D12 = TableField("B1_GAIN13", 12)
    B1_GAIN13_D13 = TableField("B1_GAIN13", 13)
    B1_GAIN13_D14 = TableField("B1_GAIN13", 14)
    B1_GAIN13_D15 = TableField("B1_GAIN13", 15)
    B1_GAIN13_D16 = TableField("B1_GAIN13", 16)
    B1_GAIN13_D17 = TableField("B1_GAIN13", 17)
    B1_GAIN13_D18 = TableField("B1_GAIN13", 18)
    B1_GAIN13_D19 = TableField("B1_GAIN13", 19)
    B1_GAIN13_D20 = TableField("B1_GAIN13", 20)
    B1_GAIN13_D21 = TableField("B1_GAIN13", 21)

    # BLOCK 1 GEWINN TABELLE 14
    B1_GAIN14_D1 = TableField("B1_GAIN14", 1)
    B1_GAIN14_D2 = TableField("B1_GAIN14", 2)
    B1_GAIN14_D3 = TableField("B1_GAIN14", 3)
    B1_GAIN14_D4 = TableField("B1_GAIN14", 4)
    B1_GAIN14_D5 = TableField("B1_GAIN14", 5)
    B1_GAIN14_D6 = TableField("B1_GAIN14", 6)
    B1_GAIN14_D7 = TableField("B1_GAIN14", 7)
    B1_GAIN14_D8 = TableField("B1_GAIN14", 8)
    B1_GAIN14_D9 = TableField("B1_GAIN14", 9)
    B1_GAIN14_D10 = TableField("B1_GAIN14", 10)
    B1_GAIN14_D11 = TableField("B1_GAIN14", 11)
    B1_GAIN14_D12 = TableField("B1_GAIN14", 12)
    B1_GAIN14_D13 = TableField("B1_GAIN14", 13)
    B1_GAIN14_D14 = TableField("B1_GAIN14", 14)
    B1_GAIN14_D15 = TableField("B1_GAIN14", 15)
    B1_GAIN14_D16 = TableField("B1_GAIN14", 16)
    B1_GAIN14_D17 = TableField("B1_GAIN14", 17)
    B1_GAIN14_D18 = TableField("B1_GAIN14", 18)
    B1_GAIN14_D19 = TableField("B1_GAIN14", 19)
    B1_GAIN14_D20 = TableField("B1_GAIN14", 20)
    B1_GAIN14_D21 = TableField("B1_GAIN14", 21)

    # BLOCK 1 GEWINN TABELLE 15
    B1_GAIN15_D1 = TableField("B1_GAIN15", 1)
    B1_GAIN15_D2 = TableField("B1_GAIN15", 2)
    B1_GAIN15_D3 = TableField("B1_GAIN15", 3)
    B1_GAIN15_D4 = TableField("B1_GAIN15", 4)
    B1_GAIN15_D5 = TableField("B1_GAIN15", 5)
    B1_GAIN15_D6 = TableField("B1_GAIN15", 6)
    B1_GAIN15_D7 = TableField("B1_GAIN15", 7)
    B1_GAIN15_D8 = TableField("B1_GAIN15", 8)
    B1_GAIN15_D9 = TableField("B1_GAIN15", 9)
    B1_GAIN15_D10 = TableField("B1_GAIN15", 10)
    B1_GAIN15_D11 = TableField("B1_GAIN15", 11)
    B1_GAIN15_D12 = TableField("B1_GAIN15", 12)
    B1_GAIN15_D13 = TableField("B1_GAIN15", 13)
    B1_GAIN15_D14 = TableField("B1_GAIN15", 14)
    B1_GAIN15_D15 = TableField("B1_GAIN15", 15)
    B1_GAIN15_D16 = TableField("B1_GAIN15", 16)
    B1_GAIN15_D17 = TableField("B1_GAIN15", 17)
    B1_GAIN15_D18 = TableField("B1_GAIN15", 18)
    B1_GAIN15_D19 = TableField("B1_GAIN15", 19)
    B1_GAIN15_D20 = TableField("B1_GAIN15", 20)
    B1_GAIN15_D21 = TableField("B1_GAIN15", 21)

    # BLOCK 1 GEWINN TABELLE 16
    B1_GAIN16_D1 = TableField("B1_GAIN16", 1)
    B1_GAIN16_D2 = TableField("B1_GAIN16", 2)
    B1_GAIN16_D3 = TableField("B1_GAIN16", 3)
    B1_GAIN16_D4 = TableField("B1_GAIN16", 4)
    B1_GAIN16_D5 = TableField("B1_GAIN16", 5)
    B1_GAIN16_D6 = TableField("B1_GAIN16", 6)
    B1_GAIN16_D7 = TableField("B1_GAIN16", 7)
    B1_GAIN16_D8 = TableField("B1_GAIN16", 8)
    B1_GAIN16_D9 = TableField("B1_GAIN16", 9)
    B1_GAIN16_D10 = TableField("B1_GAIN16", 10)
    B1_GAIN16_D11 = TableField("B1_GAIN16", 11)
    B1_GAIN16_D12 = TableField("B1_GAIN16", 12)
    B1_GAIN16_D13 = TableField("B1_GAIN16", 13)
    B1_GAIN16_D14 = TableField("B1_GAIN16", 14)
    B1_GAIN16_D15 = TableField("B1_GAIN16", 15)
    B1_GAIN16_D16 = TableField("B1_GAIN16", 16)
    B1_GAIN16_D17 = TableField("B1_GAIN16", 17)
    B1_GAIN16_D18 = TableField("B1_GAIN16", 18)
    B1_GAIN16_D19 = TableField("B1_GAIN16", 19)
    B1_GAIN16_D20 = TableField("B1_GAIN16", 20)
    B1_GAIN16_D21 = TableField("B1_GAIN16", 21)

    # BLOCK 1 GEWINN TABELLE 17
    B1_GAIN17_D1 = TableField("B1_GAIN17", 1)
    B1_GAIN17_D2 = TableField("B1_GAIN17", 2)
    B1_GAIN17_D3 = TableField("B1_GAIN17", 3)
    B1_GAIN17_D4 = TableField("B1_GAIN17", 4)
    B1_GAIN17_D5 = TableField("B1_GAIN17", 5)
    B1_GAIN17_D6 = TableField("B1_GAIN17", 6)
    B1_GAIN17_D7 = TableField("B1_GAIN17", 7)
    B1_GAIN17_D8 = TableField("B1_GAIN17", 8)
    B1_GAIN17_D9 = TableField("B1_GAIN17", 9)
    B1_GAIN17_D10 = TableField("B1_GAIN17", 10)
    B1_GAIN17_D11 = TableField("B1_GAIN17", 11)
    B1_GAIN17_D12 = TableField("B1_GAIN17", 12)
    B1_GAIN17_D13 = TableField("B1_GAIN17", 13)
    B1_GAIN17_D14 = TableField("B1_GAIN17", 14)
    B1_GAIN17_D15 = TableField("B1_GAIN17", 15)
    B1_GAIN17_D16 = TableField("B1_GAIN17", 16)
    B1_GAIN17_D17 = TableField("B1_GAIN17", 17)
    B1_GAIN17_D18 = TableField("B1_GAIN17", 18)
    B1_GAIN17_D19 = TableField("B1_GAIN17", 19)
    B1_GAIN17_D20 = TableField("B1_GAIN17", 20)
    B1_GAIN17_D21 = TableField("B1_GAIN17", 21)

    # BLOCK 1 GEWINN TABELLE 18
    B1_GAIN18_D1 = TableField("B1_GAIN18", 1)
    B1_GAIN18_D2 = TableField("B1_GAIN18", 2)
    B1_GAIN18_D3 = TableField("B1_GAIN18", 3)
    B1_GAIN18_D4 = TableField("B1_GAIN18", 4)
    B1_GAIN18_D5 = TableField("B1_GAIN18", 5)
    B1_GAIN18_D6 = TableField("B1_GAIN18", 6)
    B1_GAIN18_D7 = TableField("B1_GAIN18", 7)
    B1_GAIN18_D8 = TableField("B1_GAIN18", 8)
    B1_GAIN18_D9 = TableField("B1_GAIN18", 9)
    B1_GAIN18_D10 = TableField("B1_GAIN18", 10)
    B1_GAIN18_D11 = TableField("B1_GAIN18", 11)
    B1_GAIN18_D12 = TableField("B1_GAIN18", 12)
    B1_GAIN18_D13 = TableField("B1_GAIN18", 13)
    B1_GAIN18_D14 = TableField("B1_GAIN18", 14)
    B1_GAIN18_D15 = TableField("B1_GAIN18", 15)
    B1_GAIN18_D16 = TableField("B1_GAIN18", 16)
    B1_GAIN18_D17 = TableField("B1_GAIN18", 17)
    B1_GAIN18_D18 = TableField("B1_GAIN18", 18)
    B1_GAIN18_D19 = TableField("B1_GAIN18", 19)
    B1_GAIN18_D20 = TableField("B1_GAIN18", 20)
    B1_GAIN18_D21 = TableField("B1_GAIN18", 21)

    # BLOCK 1 GEWINN TABELLE 19
    B1_GAIN19_D1 = TableField("B1_GAIN19", 1)
    B1_GAIN19_D2 = TableField("B1_GAIN19", 2)
    B1_GAIN19_D3 = TableField("B1_GAIN19", 3)
    B1_GAIN19_D4 = TableField("B1_GAIN19", 4)
    B1_GAIN19_D5 = TableField("B1_GAIN19", 5)
    B1_GAIN19_D6 = TableField("B1_GAIN19", 6)
    B1_GAIN19_D7 = TableField("B1_GAIN19", 7)
    B1_GAIN19_D8 = TableField("B1_GAIN19", 8)
    B1_GAIN19_D9 = TableField("B1_GAIN19", 9)
    B1_GAIN19_D10 = TableField("B1_GAIN19", 10)
    B1_GAIN19_D11 = TableField("B1_GAIN19", 11)
    B1_GAIN19_D12 = TableField("B1_GAIN19", 12)
    B1_GAIN19_D13 = TableField("B1_GAIN19", 13)
    B1_GAIN19_D14 = TableField("B1_GAIN19", 14)
    B1_GAIN19_D15 = TableField("B1_GAIN19", 15)
    B1_GAIN19_D16 = TableField("B1_GAIN19", 16)
    B1_GAIN19_D17 = TableField("B1_GAIN19", 17)
    B1_GAIN19_D18 = TableField("B1_GAIN19", 18)
    B1_GAIN19_D19 = TableField("B1_GAIN19", 19)
    B1_GAIN19_D20 = TableField("B1_GAIN19", 20)
    B1_GAIN19_D21 = TableField("B1_GAIN19", 21)

    # BLOCK 1 GEWINN TABELLE 20
    B1_GAIN20_D1 = TableField("B1_GAIN20", 1)
    B1_GAIN20_D2 = TableField("B1_GAIN20", 2)
    B1_GAIN20_D3 = TableField("B1_GAIN20", 3)
    B1_GAIN20_D4 = TableField("B1_GAIN20", 4)
    B1_GAIN20_D5 = TableField("B1_GAIN20", 5)
    B1_GAIN20_D6 = TableField("B1_GAIN20", 6)
    B1_GAIN20_D7 = TableField("B1_GAIN20", 7)
    B1_GAIN20_D8 = TableField("B1_GAIN20", 8)
    B1_GAIN20_D9 = TableField("B1_GAIN20", 9)
    B1_GAIN20_D10 = TableField("B1_GAIN20", 10)
    B1_GAIN20_D11 = TableField("B1_GAIN20", 11)
    B1_GAIN20_D12 = TableField("B1_GAIN20", 12)
    B1_GAIN20_D13 = TableField("B1_GAIN20", 13)
    B1_GAIN20_D14 = TableField("B1_GAIN20", 14)
    B1_GAIN20_D15 = TableField("B1_GAIN20", 15)
    B1_GAIN20_D16 = TableField("B1_GAIN20", 16)
    B1_GAIN20_D17 = TableField("B1_GAIN20", 17)
    B1_GAIN20_D18 = TableField("B1_GAIN20", 18)
    B1_GAIN20_D19 = TableField("B1_GAIN20", 19)
    B1_GAIN20_D20 = TableField("B1_GAIN20", 20)
    B1_GAIN20_D21 = TableField("B1_GAIN20", 21)

    # BLOCK 1 VERLUST TABELLE 1
    B1_LOSS1_D1 = TableField("B1_LOSS1", 1)
    B1_LOSS1_D2 = TableField("B1_LOSS1", 2)
    B1_LOSS1_D3 = TableField("B1_LOSS1", 3)
    B1_LOSS1_D4 = TableField("B1_LOSS1", 4)
    B1_LOSS1_D5 = TableField("B1_LOSS1", 5)
    B1_LOSS1_D6 = TableField("B1_LOSS1", 6)
    B1_LOSS1_D7 = TableField("B1_LOSS1", 7)
    B1_LOSS1_D8 = TableField("B1_LOSS1", 8)
    B1_LOSS1_D9 = TableField("B1_LOSS1", 9)
    B1_LOSS1_D10 = TableField("B1_LOSS1", 10)
    B1_LOSS1_D11 = TableField("B1_LOSS1", 11)
    B1_LOSS1_D12 = TableField("B1_LOSS1", 12)
    B1_LOSS1_D13 = TableField("B1_LOSS1", 13)
    B1_LOSS1_D14 = TableField("B1_LOSS1", 14)
    B1_LOSS1_D15 = TableField("B1_LOSS1", 15)
    B1_LOSS1_D16 = TableField("B1_LOSS1", 16)
    B1_LOSS1_D17 = TableField("B1_LOSS1", 17)
    B1_LOSS1_D18 = TableField("B1_LOSS1", 18)
    B1_LOSS1_D19 = TableField("B1_LOSS1", 19)
    B1_LOSS1_D20 = TableField("B1_LOSS1", 20)
    B1_LOSS1_D21 = TableField("B1_LOSS1", 21)

    # BLOCK 1 VERLUST TABELLE 2
    B1_LOSS2_D1 = TableField("B1_LOSS2", 1)
    B1_LOSS2_D2 = TableField("B1_LOSS2", 2)
    B1_LOSS2_D3 = TableField("B1_LOSS2", 3)
    B1_LOSS2_D4 = TableField("B1_LOSS2", 4)
    B1_LOSS2_D5 = TableField("B1_LOSS2", 5)
    B1_LOSS2_D6 = TableField("B1_LOSS2", 6)
    B1_LOSS2_D7 = TableField("B1_LOSS2", 7)
    B1_LOSS2_D8 = TableField("B1_LOSS2", 8)
    B1_LOSS2_D9 = TableField("B1_LOSS2", 9)
    B1_LOSS2_D10 = TableField("B1_LOSS2", 10)
    B1_LOSS2_D11 = TableField("B1_LOSS2", 11)
    B1_LOSS2_D12 = TableField("B1_LOSS2", 12)
    B1_LOSS2_D13 = TableField("B1_LOSS2", 13)
    B1_LOSS2_D14 = TableField("B1_LOSS2", 14)
    B1_LOSS2_D15 = TableField("B1_LOSS2", 15)
    B1_LOSS2_D16 = TableField("B1_LOSS2", 16)
    B1_LOSS2_D17 = TableField("B1_LOSS2", 17)
    B1_LOSS2_D18 = TableField("B1_LOSS2", 18)
    B1_LOSS2_D19 = TableField("B1_LOSS2", 19)
    B1_LOSS2_D20 = TableField("B1_LOSS2", 20)
    B1_LOSS2_D21 = TableField("B1_LOSS2", 21)

    # BLOCK 1 VERLUST TABELLE 3
    B1_LOSS3_D1 = TableField("B1_LOSS3", 1)
    B1_LOSS3_D2 = TableField("B1_LOSS3", 2)
    B1_LOSS3_D3 = TableField("B1_LOSS3", 3)
    B1_LOSS3_D4 = TableField("B1_LOSS3", 4)
    B1_LOSS3_D5 = TableField("B1_LOSS3", 5)
    B1_LOSS3_D6 = TableField("B1_LOSS3", 6)
    B1_LOSS3_D7 = TableField("B1_LOSS3", 7)
    B1_LOSS3_D8 = TableField("B1_LOSS3", 8)
    B1_LOSS3_D9 = TableField("B1_LOSS3", 9)
    B1_LOSS3_D10 = TableField("B1_LOSS3", 10)
    B1_LOSS3_D11 = TableField("B1_LOSS3", 11)
    B1_LOSS3_D12 = TableField("B1_LOSS3", 12)
    B1_LOSS3_D13 = TableField("B1_LOSS3", 13)
    B1_LOSS3_D14 = TableField("B1_LOSS3", 14)
    B1_LOSS3_D15 = TableField("B1_LOSS3", 15)
    B1_LOSS3_D16 = TableField("B1_LOSS3", 16)
    B1_LOSS3_D17 = TableField("B1_LOSS3", 17)
    B1_LOSS3_D18 = TableField("B1_LOSS3", 18)
    B1_LOSS3_D19 = TableField("B1_LOSS3", 19)
    B1_LOSS3_D20 = TableField("B1_LOSS3", 20)
    B1_LOSS3_D21 = TableField("B1_LOSS3", 21)

    # BLOCK 1 VERLUST TABELLE 4
    B1_LOSS4_D1 = TableField("B1_LOSS4", 1)
    B1_LOSS4_D2 = TableField("B1_LOSS4", 2)
    B1_LOSS4_D3 = TableField("B1_LOSS4", 3)
    B1_LOSS4_D4 = TableField("B1_LOSS4", 4)
    B1_LOSS4_D5 = TableField("B1_LOSS4", 5)
    B1_LOSS4_D6 = TableField("B1_LOSS4", 6)
    B1_LOSS4_D7 = TableField("B1_LOSS4", 7)
    B1_LOSS4_D8 = TableField("B1_LOSS4", 8)
    B1_LOSS4_D9 = TableField("B1_LOSS4", 9)
    B1_LOSS4_D10 = TableField("B1_LOSS4", 10)
    B1_LOSS4_D11 = TableField("B1_LOSS4", 11)
    B1_LOSS4_D12 = TableField("B1_LOSS4", 12)
    B1_LOSS4_D13 = TableField("B1_LOSS4", 13)
    B1_LOSS4_D14 = TableField("B1_LOSS4", 14)
    B1_LOSS4_D15 = TableField("B1_LOSS4", 15)
    B1_LOSS4_D16 = TableField("B1_LOSS4", 16)
    B1_LOSS4_D17 = TableField("B1_LOSS4", 17)
    B1_LOSS4_D18 = TableField("B1_LOSS4", 18)
    B1_LOSS4_D19 = TableField("B1_LOSS4", 19)
    B1_LOSS4_D20 = TableField("B1_LOSS4", 20)
    B1_LOSS4_D21 = TableField("B1_LOSS4", 21)

    # BLOCK 1 VERLUST TABELLE 5
    B1_LOSS5_D1 = TableField("B1_LOSS5", 1)
    B1_LOSS5_D2 = TableField("B1_LOSS5", 2)
    B1_LOSS5_D3 = TableField("B1_LOSS5", 3)
    B1_LOSS5_D4 = TableField("B1_LOSS5", 4)
    B1_LOSS5_D5 = TableField("B1_LOSS5", 5)
    B1_LOSS5_D6 = TableField("B1_LOSS5", 6)
    B1_LOSS5_D7 = TableField("B1_LOSS5", 7)
    B1_LOSS5_D8 = TableField("B1_LOSS5", 8)
    B1_LOSS5_D9 = TableField("B1_LOSS5", 9)
    B1_LOSS5_D10 = TableField("B1_LOSS5", 10)
    B1_LOSS5_D11 = TableField("B1_LOSS5", 11)
    B1_LOSS5_D12 = TableField("B1_LOSS5", 12)
    B1_LOSS5_D13 = TableField("B1_LOSS5", 13)
    B1_LOSS5_D14 = TableField("B1_LOSS5", 14)
    B1_LOSS5_D15 = TableField("B1_LOSS5", 15)
    B1_LOSS5_D16 = TableField("B1_LOSS5", 16)
    B1_LOSS5_D17 = TableField("B1_LOSS5", 17)
    B1_LOSS5_D18 = TableField("B1_LOSS5", 18)
    B1_LOSS5_D19 = TableField("B1_LOSS5", 19)
    B1_LOSS5_D20 = TableField("B1_LOSS5", 20)
    B1_LOSS5_D21 = TableField("B1_LOSS5", 21)

    # BLOCK 1 VERLUST TABELLE 6
    B1_LOSS6_D1 = TableField("B1_LOSS6", 1)
    B1_LOSS6_D2 = TableField("B1_LOSS6", 2)
    B1_LOSS6_D3 = TableField("B1_LOSS6", 3)
    B1_LOSS6_D4 = TableField("B1_LOSS6", 4)
    B1_LOSS6_D5 = TableField("B1_LOSS6", 5)
    B1_LOSS6_D6 = TableField("B1_LOSS6", 6)
    B1_LOSS6_D7 = TableField("B1_LOSS6", 7)
    B1_LOSS6_D8 = TableField("B1_LOSS6", 8)
    B1_LOSS6_D9 = TableField("B1_LOSS6", 9)
    B1_LOSS6_D10 = TableField("B1_LOSS6", 10)
    B1_LOSS6_D11 = TableField("B1_LOSS6", 11)
    B1_LOSS6_D12 = TableField("B1_LOSS6", 12)
    B1_LOSS6_D13 = TableField("B1_LOSS6", 13)
    B1_LOSS6_D14 = TableField("B1_LOSS6", 14)
    B1_LOSS6_D15 = TableField("B1_LOSS6", 15)
    B1_LOSS6_D16 = TableField("B1_LOSS6", 16)
    B1_LOSS6_D17 = TableField("B1_LOSS6", 17)
    B1_LOSS6_D18 = TableField("B1_LOSS6", 18)
    B1_LOSS6_D19 = TableField("B1_LOSS6", 19)
    B1_LOSS6_D20 = TableField("B1_LOSS6", 20)
    B1_LOSS6_D21 = TableField("B1_LOSS6", 21)

    # BLOCK 1 VERLUST TABELLE 7
    B1_LOSS7_D1 = TableField("B1_LOSS7", 1)
    B1_LOSS7_D2 = TableField("B1_LOSS7", 2)
    B1_LOSS7_D3 = TableField("B1_LOSS7", 3)
    B1_LOSS7_D4 = TableField("B1_LOSS7", 4)
    B1_LOSS7_D5 = TableField("B1_LOSS7", 5)
    B1_LOSS7_D6 = TableField("B1_LOSS7", 6)
    B1_LOSS7_D7 = TableField("B1_LOSS7", 7)
    B1_LOSS7_D8 = TableField("B1_LOSS7", 8)
    B1_LOSS7_D9 = TableField("B1_LOSS7", 9)
    B1_LOSS7_D10 = TableField("B1_LOSS7", 10)
    B1_LOSS7_D11 = TableField("B1_LOSS7", 11)
    B1_LOSS7_D12 = TableField("B1_LOSS7", 12)
    B1_LOSS7_D13 = TableField("B1_LOSS7", 13)
    B1_LOSS7_D14 = TableField("B1_LOSS7", 14)
    B1_LOSS7_D15 = TableField("B1_LOSS7", 15)
    B1_LOSS7_D16 = TableField("B1_LOSS7", 16)
    B1_LOSS7_D17 = TableField("B1_LOSS7", 17)
    B1_LOSS7_D18 = TableField("B1_LOSS7", 18)
    B1_LOSS7_D19 = TableField("B1_LOSS7", 19)
    B1_LOSS7_D20 = TableField("B1_LOSS7", 20)
    B1_LOSS7_D21 = TableField("B1_LOSS7", 21)

    # BLOCK 1 VERLUST TABELLE 8
    B1_LOSS8_D1 = TableField("B1_LOSS8", 1)
    B1_LOSS8_D2 = TableField("B1_LOSS8", 2)
    B1_LOSS8_D3 = TableField("B1_LOSS8", 3)
    B1_LOSS8_D4 = TableField("B1_LOSS8", 4)
    B1_LOSS8_D5 = TableField("B1_LOSS8", 5)
    B1_LOSS8_D6 = TableField("B1_LOSS8", 6)
    B1_LOSS8_D7 = TableField("B1_LOSS8", 7)
    B1_LOSS8_D8 = TableField("B1_LOSS8", 8)
    B1_LOSS8_D9 = TableField("B1_LOSS8", 9)
    B1_LOSS8_D10 = TableField("B1_LOSS8", 10)
    B1_LOSS8_D11 = TableField("B1_LOSS8", 11)
    B1_LOSS8_D12 = TableField("B1_LOSS8", 12)
    B1_LOSS8_D13 = TableField("B1_LOSS8", 13)
    B1_LOSS8_D14 = TableField("B1_LOSS8", 14)
    B1_LOSS8_D15 = TableField("B1_LOSS8", 15)
    B1_LOSS8_D16 = TableField("B1_LOSS8", 16)
    B1_LOSS8_D17 = TableField("B1_LOSS8", 17)
    B1_LOSS8_D18 = TableField("B1_LOSS8", 18)
    B1_LOSS8_D19 = TableField("B1_LOSS8", 19)
    B1_LOSS8_D20 = TableField("B1_LOSS8", 20)
    B1_LOSS8_D21 = TableField("B1_LOSS8", 21)

    # BLOCK 1 VERLUST TABELLE 9
    B1_LOSS9_D1 = TableField("B1_LOSS9", 1)
    B1_LOSS9_D2 = TableField("B1_LOSS9", 2)
    B1_LOSS9_D3 = TableField("B1_LOSS9", 3)
    B1_LOSS9_D4 = TableField("B1_LOSS9", 4)
    B1_LOSS9_D5 = TableField("B1_LOSS9", 5)
    B1_LOSS9_D6 = TableField("B1_LOSS9", 6)
    B1_LOSS9_D7 = TableField("B1_LOSS9", 7)
    B1_LOSS9_D8 = TableField("B1_LOSS9", 8)
    B1_LOSS9_D9 = TableField("B1_LOSS9", 9)
    B1_LOSS9_D10 = TableField("B1_LOSS9", 10)
    B1_LOSS9_D11 = TableField("B1_LOSS9", 11)
    B1_LOSS9_D12 = TableField("B1_LOSS9", 12)
    B1_LOSS9_D13 = TableField("B1_LOSS9", 13)
    B1_LOSS9_D14 = TableField("B1_LOSS9", 14)
    B1_LOSS9_D15 = TableField("B1_LOSS9", 15)
    B1_LOSS9_D16 = TableField("B1_LOSS9", 16)
    B1_LOSS9_D17 = TableField("B1_LOSS9", 17)
    B1_LOSS9_D18 = TableField("B1_LOSS9", 18)
    B1_LOSS9_D19 = TableField("B1_LOSS9", 19)
    B1_LOSS9_D20 = TableField("B1_LOSS9", 20)
    B1_LOSS9_D21 = TableField("B1_LOSS9", 21)

    # BLOCK 1 VERLUST TABELLE 10
    B1_LOSS10_D1 = TableField("B1_LOSS10", 1)
    B1_LOSS10_D2 = TableField("B1_LOSS10", 2)
    B1_LOSS10_D3 = TableField("B1_LOSS10", 3)
    B1_LOSS10_D4 = TableField("B1_LOSS10", 4)
    B1_LOSS10_D5 = TableField("B1_LOSS10", 5)
    B1_LOSS10_D6 = TableField("B1_LOSS10", 6)
    B1_LOSS10_D7 = TableField("B1_LOSS10", 7)
    B1_LOSS10_D8 = TableField("B1_LOSS10", 8)
    B1_LOSS10_D9 = TableField("B1_LOSS10", 9)
    B1_LOSS10_D10 = TableField("B1_LOSS10", 10)
    B1_LOSS10_D11 = TableField("B1_LOSS10", 11)
    B1_LOSS10_D12 = TableField("B1_LOSS10", 12)
    B1_LOSS10_D13 = TableField("B1_LOSS10", 13)
    B1_LOSS10_D14 = TableField("B1_LOSS10", 14)
    B1_LOSS10_D15 = TableField("B1_LOSS10", 15)
    B1_LOSS10_D16 = TableField("B1_LOSS10", 16)
    B1_LOSS10_D17 = TableField("B1_LOSS10", 17)
    B1_LOSS10_D18 = TableField("B1_LOSS10", 18)
    B1_LOSS10_D19 = TableField("B1_LOSS10", 19)
    B1_LOSS10_D20 = TableField("B1_LOSS10", 20)
    B1_LOSS10_D21 = TableField("B1_LOSS10", 21)

    # BLOCK 1 VERLUST TABELLE 11
    B1_LOSS11_D1 = TableField("B1_LOSS11", 1)
    B1_LOSS11_D2 = TableField("B1_LOSS11", 2)
    B1_LOSS11_D3 = TableField("B1_LOSS11", 3)
    B1_LOSS11_D4 = TableField("B1_LOSS11", 4)
    B1_LOSS11_D5 = TableField("B1_LOSS11", 5)
    B1_LOSS11_D6 = TableField("B1_LOSS11", 6)
    B1_LOSS11_D7 = TableField("B1_LOSS11", 7)
    B1_LOSS11_D8 = TableField("B1_LOSS11", 8)
    B1_LOSS11_D9 = TableField("B1_LOSS11", 9)
    B1_LOSS11_D10 = TableField("B1_LOSS11", 10)
    B1_LOSS11_D11 = TableField("B1_LOSS11", 11)
    B1_LOSS11_D12 = TableField("B1_LOSS11", 12)
    B1_LOSS11_D13 = TableField("B1_LOSS11", 13)
    B1_LOSS11_D14 = TableField("B1_LOSS11", 14)
    B1_LOSS11_D15 = TableField("B1_LOSS11", 15)
    B1_LOSS11_D16 = TableField("B1_LOSS11", 16)
    B1_LOSS11_D17 = TableField("B1_LOSS11", 17)
    B1_LOSS11_D18 = TableField("B1_LOSS11", 18)
    B1_LOSS11_D19 = TableField("B1_LOSS11", 19)
    B1_LOSS11_D20 = TableField("B1_LOSS11", 20)
    B1_LOSS11_D21 = TableField("B1_LOSS11", 21)

    # BLOCK 1 VERLUST TABELLE 12
    B1_LOSS12_D1 = TableField("B1_LOSS12", 1)
    B1_LOSS12_D2 = TableField("B1_LOSS12", 2)
    B1_LOSS12_D3 = TableField("B1_LOSS12", 3)
    B1_LOSS12_D4 = TableField("B1_LOSS12", 4)
    B1_LOSS12_D5 = TableField("B1_LOSS12", 5)
    B1_LOSS12_D6 = TableField("B1_LOSS12", 6)
    B1_LOSS12_D7 = TableField("B1_LOSS12", 7)
    B1_LOSS12_D8 = TableField("B1_LOSS12", 8)
    B1_LOSS12_D9 = TableField("B1_LOSS12", 9)
    B1_LOSS12_D10 = TableField("B1_LOSS12", 10)
    B1_LOSS12_D11 = TableField("B1_LOSS12", 11)
    B1_LOSS12_D12 = TableField("B1_LOSS12", 12)
    B1_LOSS12_D13 = TableField("B1_LOSS12", 13)
    B1_LOSS12_D14 = TableField("B1_LOSS12", 14)
    B1_LOSS12_D15 = TableField("B1_LOSS12", 15)
    B1_LOSS12_D16 = TableField("B1_LOSS12", 16)
    B1_LOSS12_D17 = TableField("B1_LOSS12", 17)
    B1_LOSS12_D18 = TableField("B1_LOSS12", 18)
    B1_LOSS12_D19 = TableField("B1_LOSS12", 19)
    B1_LOSS12_D20 = TableField("B1_LOSS12", 20)
    B1_LOSS12_D21 = TableField("B1_LOSS12", 21)

    # BLOCK 1 VERLUST TABELLE 13
    B1_LOSS13_D1 = TableField("B1_LOSS13", 1)
    B1_LOSS13_D2 = TableField("B1_LOSS13", 2)
    B1_LOSS13_D3 = TableField("B1_LOSS13", 3)
    B1_LOSS13_D4 = TableField("B1_LOSS13", 4)
    B1_LOSS13_D5 = TableField("B1_LOSS13", 5)
    B1_LOSS13_D6 = TableField("B1_LOSS13", 6)
    B1_LOSS13_D7 = TableField("B1_LOSS13", 7)
    B1_LOSS13_D8 = TableField("B1_LOSS13", 8)
    B1_LOSS13_D9 = TableField("B1_LOSS13", 9)
    B1_LOSS13_D10 = TableField("B1_LOSS13", 10)
    B1_LOSS13_D11 = TableField("B1_LOSS13", 11)
    B1_LOSS13_D12 = TableField("B1_LOSS13", 12)
    B1_LOSS13_D13 = TableField("B1_LOSS13", 13)
    B1_LOSS13_D14 = TableField("B1_LOSS13", 14)
    B1_LOSS13_D15 = TableField("B1_LOSS13", 15)
    B1_LOSS13_D16 = TableField("B1_LOSS13", 16)
    B1_LOSS13_D17 = TableField("B1_LOSS13", 17)
    B1_LOSS13_D18 = TableField("B1_LOSS13", 18)
    B1_LOSS13_D19 = TableField("B1_LOSS13", 19)
    B1_LOSS13_D20 = TableField("B1_LOSS13", 20)
    B1_LOSS13_D21 = TableField("B1_LOSS13", 21)

    # BLOCK 1 VERLUST TABELLE 14
    B1_LOSS14_D1 = TableField("B1_LOSS14", 1)
    B1_LOSS14_D2 = TableField("B1_LOSS14", 2)
    B1_LOSS14_D3 = TableField("B1_LOSS14", 3)
    B1_LOSS14_D4 = TableField("B1_LOSS14", 4)
    B1_LOSS14_D5 = TableField("B1_LOSS14", 5)
    B1_LOSS14_D6 = TableField("B1_LOSS14", 6)
    B1_LOSS14_D7 = TableField("B1_LOSS14", 7)
    B1_LOSS14_D8 = TableField("B1_LOSS14", 8)
    B1_LOSS14_D9 = TableField("B1_LOSS14", 9)
    B1_LOSS14_D10 = TableField("B1_LOSS14", 10)
    B1_LOSS14_D11 = TableField("B1_LOSS14", 11)
    B1_LOSS14_D12 = TableField("B1_LOSS14", 12)
    B1_LOSS14_D13 = TableField("B1_LOSS14", 13)
    B1_LOSS14_D14 = TableField("B1_LOSS14", 14)
    B1_LOSS14_D15 = TableField("B1_LOSS14", 15)
    B1_LOSS14_D16 = TableField("B1_LOSS14", 16)
    B1_LOSS14_D17 = TableField("B1_LOSS14", 17)
    B1_LOSS14_D18 = TableField("B1_LOSS14", 18)
    B1_LOSS14_D19 = TableField("B1_LOSS14", 19)
    B1_LOSS14_D20 = TableField("B1_LOSS14", 20)
    B1_LOSS14_D21 = TableField("B1_LOSS14", 21)

    # BLOCK 1 VERLUST TABELLE 15
    B1_LOSS15_D1 = TableField("B1_LOSS15", 1)
    B1_LOSS15_D2 = TableField("B1_LOSS15", 2)
    B1_LOSS15_D3 = TableField("B1_LOSS15", 3)
    B1_LOSS15_D4 = TableField("B1_LOSS15", 4)
    B1_LOSS15_D5 = TableField("B1_LOSS15", 5)
    B1_LOSS15_D6 = TableField("B1_LOSS15", 6)
    B1_LOSS15_D7 = TableField("B1_LOSS15", 7)
    B1_LOSS15_D8 = TableField("B1_LOSS15", 8)
    B1_LOSS15_D9 = TableField("B1_LOSS15", 9)
    B1_LOSS15_D10 = TableField("B1_LOSS15", 10)
    B1_LOSS15_D11 = TableField("B1_LOSS15", 11)
    B1_LOSS15_D12 = TableField("B1_LOSS15", 12)
    B1_LOSS15_D13 = TableField("B1_LOSS15", 13)
    B1_LOSS15_D14 = TableField("B1_LOSS15", 14)
    B1_LOSS15_D15 = TableField("B1_LOSS15", 15)
    B1_LOSS15_D16 = TableField("B1_LOSS15", 16)
    B1_LOSS15_D17 = TableField("B1_LOSS15", 17)
    B1_LOSS15_D18 = TableField("B1_LOSS15", 18)
    B1_LOSS15_D19 = TableField("B1_LOSS15", 19)
    B1_LOSS15_D20 = TableField("B1_LOSS15", 20)
    B1_LOSS15_D21 = TableField("B1_LOSS15", 21)

    # BLOCK 1 VERLUST TABELLE 16
    B1_LOSS16_D1 = TableField("B1_LOSS16", 1)
    B1_LOSS16_D2 = TableField("B1_LOSS16", 2)
    B1_LOSS16_D3 = TableField("B1_LOSS16", 3)
    B1_LOSS16_D4 = TableField("B1_LOSS16", 4)
    B1_LOSS16_D5 = TableField("B1_LOSS16", 5)
    B1_LOSS16_D6 = TableField("B1_LOSS16", 6)
    B1_LOSS16_D7 = TableField("B1_LOSS16", 7)
    B1_LOSS16_D8 = TableField("B1_LOSS16", 8)
    B1_LOSS16_D9 = TableField("B1_LOSS16", 9)
    B1_LOSS16_D10 = TableField("B1_LOSS16", 10)
    B1_LOSS16_D11 = TableField("B1_LOSS16", 11)
    B1_LOSS16_D12 = TableField("B1_LOSS16", 12)
    B1_LOSS16_D13 = TableField("B1_LOSS16", 13)
    B1_LOSS16_D14 = TableField("B1_LOSS16", 14)
    B1_LOSS16_D15 = TableField("B1_LOSS16", 15)
    B1_LOSS16_D16 = TableField("B1_LOSS16", 16)
    B1_LOSS16_D17 = TableField("B1_LOSS16", 17)
    B1_LOSS16_D18 = TableField("B1_LOSS16", 18)
    B1_LOSS16_D19 = TableField("B1_LOSS16", 19)
    B1_LOSS16_D20 = TableField("B1_LOSS16", 20)
    B1_LOSS16_D21 = TableField("B1_LOSS16", 21)

    # BLOCK 1 VERLUST TABELLE 17
    B1_LOSS17_D1 = TableField("B1_LOSS17", 1)
    B1_LOSS17_D2 = TableField("B1_LOSS17", 2)
    B1_LOSS17_D3 = TableField("B1_LOSS17", 3)
    B1_LOSS17_D4 = TableField("B1_LOSS17", 4)
    B1_LOSS17_D5 = TableField("B1_LOSS17", 5)
    B1_LOSS17_D6 = TableField("B1_LOSS17", 6)
    B1_LOSS17_D7 = TableField("B1_LOSS17", 7)
    B1_LOSS17_D8 = TableField("B1_LOSS17", 8)
    B1_LOSS17_D9 = TableField("B1_LOSS17", 9)
    B1_LOSS17_D10 = TableField("B1_LOSS17", 10)
    B1_LOSS17_D11 = TableField("B1_LOSS17", 11)
    B1_LOSS17_D12 = TableField("B1_LOSS17", 12)
    B1_LOSS17_D13 = TableField("B1_LOSS17", 13)
    B1_LOSS17_D14 = TableField("B1_LOSS17", 14)
    B1_LOSS17_D15 = TableField("B1_LOSS17", 15)
    B1_LOSS17_D16 = TableField("B1_LOSS17", 16)
    B1_LOSS17_D17 = TableField("B1_LOSS17", 17)
    B1_LOSS17_D18 = TableField("B1_LOSS17", 18)
    B1_LOSS17_D19 = TableField("B1_LOSS17", 19)
    B1_LOSS17_D20 = TableField("B1_LOSS17", 20)
    B1_LOSS17_D21 = TableField("B1_LOSS17", 21)

    # BLOCK 1 VERLUST TABELLE 18
    B1_LOSS18_D1 = TableField("B1_LOSS18", 1)
    B1_LOSS18_D2 = TableField("B1_LOSS18", 2)
    B1_LOSS18_D3 = TableField("B1_LOSS18", 3)
    B1_LOSS18_D4 = TableField("B1_LOSS18", 4)
    B1_LOSS18_D5 = TableField("B1_LOSS18", 5)
    B1_LOSS18_D6 = TableField("B1_LOSS18", 6)
    B1_LOSS18_D7 = TableField("B1_LOSS18", 7)
    B1_LOSS18_D8 = TableField("B1_LOSS18", 8)
    B1_LOSS18_D9 = TableField("B1_LOSS18", 9)
    B1_LOSS18_D10 = TableField("B1_LOSS18", 10)
    B1_LOSS18_D11 = TableField("B1_LOSS18", 11)
    B1_LOSS18_D12 = TableField("B1_LOSS18", 12)
    B1_LOSS18_D13 = TableField("B1_LOSS18", 13)
    B1_LOSS18_D14 = TableField("B1_LOSS18", 14)
    B1_LOSS18_D15 = TableField("B1_LOSS18", 15)
    B1_LOSS18_D16 = TableField("B1_LOSS18", 16)
    B1_LOSS18_D17 = TableField("B1_LOSS18", 17)
    B1_LOSS18_D18 = TableField("B1_LOSS18", 18)
    B1_LOSS18_D19 = TableField("B1_LOSS18", 19)
    B1_LOSS18_D20 = TableField("B1_LOSS18", 20)
    B1_LOSS18_D21 = TableField("B1_LOSS18", 21)

    # BLOCK 1 VERLUST TABELLE 19
    B1_LOSS19_D1 = TableField("B1_LOSS19", 1)
    B1_LOSS19_D2 = TableField("B1_LOSS19", 2)
    B1_LOSS19_D3 = TableField("B1_LOSS19", 3)
    B1_LOSS19_D4 = TableField("B1_LOSS19", 4)
    B1_LOSS19_D5 = TableField("B1_LOSS19", 5)
    B1_LOSS19_D6 = TableField("B1_LOSS19", 6)
    B1_LOSS19_D7 = TableField("B1_LOSS19", 7)
    B1_LOSS19_D8 = TableField("B1_LOSS19", 8)
    B1_LOSS19_D9 = TableField("B1_LOSS19", 9)
    B1_LOSS19_D10 = TableField("B1_LOSS19", 10)
    B1_LOSS19_D11 = TableField("B1_LOSS19", 11)
    B1_LOSS19_D12 = TableField("B1_LOSS19", 12)
    B1_LOSS19_D13 = TableField("B1_LOSS19", 13)
    B1_LOSS19_D14 = TableField("B1_LOSS19", 14)
    B1_LOSS19_D15 = TableField("B1_LOSS19", 15)
    B1_LOSS19_D16 = TableField("B1_LOSS19", 16)
    B1_LOSS19_D17 = TableField("B1_LOSS19", 17)
    B1_LOSS19_D18 = TableField("B1_LOSS19", 18)
    B1_LOSS19_D19 = TableField("B1_LOSS19", 19)
    B1_LOSS19_D20 = TableField("B1_LOSS19", 20)
    B1_LOSS19_D21 = TableField("B1_LOSS19", 21)

    # BLOCK 1 VERLUST TABELLE 20
    B1_LOSS20_D1 = TableField("B1_LOSS20", 1)
    B1_LOSS20_D2 = TableField("B1_LOSS20", 2)
    B1_LOSS20_D3 = TableField("B1_LOSS20", 3)
    B1_LOSS20_D4 = TableField("B1_LOSS20", 4)
    B1_LOSS20_D5 = TableField("B1_LOSS20", 5)
    B1_LOSS20_D6 = TableField("B1_LOSS20", 6)
    B1_LOSS20_D7 = TableField("B1_LOSS20", 7)
    B1_LOSS20_D8 = TableField("B1_LOSS20", 8)
    B1_LOSS20_D9 = TableField("B1_LOSS20", 9)
    B1_LOSS20_D10 = TableField("B1_LOSS20", 10)
    B1_LOSS20_D11 = TableField("B1_LOSS20", 11)
    B1_LOSS20_D12 = TableField("B1_LOSS20", 12)
    B1_LOSS20_D13 = TableField("B1_LOSS20", 13)
    B1_LOSS20_D14 = TableField("B1_LOSS20", 14)
    B1_LOSS20_D15 = TableField("B1_LOSS20", 15)
    B1_LOSS20_D16 = TableField("B1_LOSS20", 16)
    B1_LOSS20_D17 = TableField("B1_LOSS20", 17)
    B1_LOSS20_D18 = TableField("B1_LOSS20", 18)
    B1_LOSS20_D19 = TableField("B1_LOSS20", 19)
    B1_LOSS20_D20 = TableField("B1_LOSS20", 20)
    B1_LOSS20_D21 = TableField("B1_LOSS20", 21)

    # BLOCK 2 GEWINN TABELLE 1
    B2_GAIN1_D1 = TableField("B2_GAIN1", 1)
    B2_GAIN1_D2 = TableField("B2_GAIN1", 2)
    B2_GAIN1_D3 = TableField("B2_GAIN1", 3)
    B2_GAIN1_D4 = TableField("B2_GAIN1", 4)
    B2_GAIN1_D5 = TableField("B2_GAIN1", 5)
    B2_GAIN1_D6 = TableField("B2_GAIN1", 6)
    B2_GAIN1_D7 = TableField("B2_GAIN1", 7)
    B2_GAIN1_D8 = TableField("B2_GAIN1", 8)
    B2_GAIN1_D9 = TableField("B2_GAIN1", 9)
    B2_GAIN1_D10 = TableField("B2_GAIN1", 10)
    B2_GAIN1_D11 = TableField("B2_GAIN1", 11)
    B2_GAIN1_D12 = TableField("B2_GAIN1", 12)
    B2_GAIN1_D13 = TableField("B2_GAIN1", 13)
    B2_GAIN1_D14 = TableField("B2_GAIN1", 14)
    B2_GAIN1_D15 = TableField("B2_GAIN1", 15)
    B2_GAIN1_D16 = TableField("B2_GAIN1", 16)
    B2_GAIN1_D17 = TableField("B2_GAIN1", 17)
    B2_GAIN1_D18 = TableField("B2_GAIN1", 18)
    B2_GAIN1_D19 = TableField("B2_GAIN1", 19)
    B2_GAIN1_D20 = TableField("B2_GAIN1", 20)
    B2_GAIN1_D21 = TableField("B2_GAIN1", 21)

    # BLOCK 2 GEWINN TABELLE 2
    B2_GAIN2_D1 = TableField("B2_GAIN2", 1)
    B2_GAIN2_D2 = TableField("B2_GAIN2", 2)
    B2_GAIN2_D3 = TableField("B2_GAIN2", 3)
    B2_GAIN2_D4 = TableField("B2_GAIN2", 4)
    B2_GAIN2_D5 = TableField("B2_GAIN2", 5)
    B2_GAIN2_D6 = TableField("B2_GAIN2", 6)
    B2_GAIN2_D7 = TableField("B2_GAIN2", 7)
    B2_GAIN2_D8 = TableField("B2_GAIN2", 8)
    B2_GAIN2_D9 = TableField("B2_GAIN2", 9)
    B2_GAIN2_D10 = TableField("B2_GAIN2", 10)
    B2_GAIN2_D11 = TableField("B2_GAIN2", 11)
    B2_GAIN2_D12 = TableField("B2_GAIN2", 12)
    B2_GAIN2_D13 = TableField("B2_GAIN2", 13)
    B2_GAIN2_D14 = TableField("B2_GAIN2", 14)
    B2_GAIN2_D15 = TableField("B2_GAIN2", 15)
    B2_GAIN2_D16 = TableField("B2_GAIN2", 16)
    B2_GAIN2_D17 = TableField("B2_GAIN2", 17)
    B2_GAIN2_D18 = TableField("B2_GAIN2", 18)
    B2_GAIN2_D19 = TableField("B2_GAIN2", 19)
    B2_GAIN2_D20 = TableField("B2_GAIN2", 20)
    B2_GAIN2_D21 = TableField("B2_GAIN2", 21)

    # BLOCK 2 GEWINN TABELLE 3
    B2_GAIN3_D1 = TableField("B2_GAIN3", 1)
    B2_GAIN3_D2 = TableField("B2_GAIN3", 2)
    B2_GAIN3_D3 = TableField("B2_GAIN3", 3)
    B2_GAIN3_D4 = TableField("B2_GAIN3", 4)
    B2_GAIN3_D5 = TableField("B2_GAIN3", 5)
    B2_GAIN3_D6 = TableField("B2_GAIN3", 6)
    B2_GAIN3_D7 = TableField("B2_GAIN3", 7)
    B2_GAIN3_D8 = TableField("B2_GAIN3", 8)
    B2_GAIN3_D9 = TableField("B2_GAIN3", 9)
    B2_GAIN3_D10 = TableField("B2_GAIN3", 10)
    B2_GAIN3_D11 = TableField("B2_GAIN3", 11)
    B2_GAIN3_D12 = TableField("B2_GAIN3", 12)
    B2_GAIN3_D13 = TableField("B2_GAIN3", 13)
    B2_GAIN3_D14 = TableField("B2_GAIN3", 14)
    B2_GAIN3_D15 = TableField("B2_GAIN3", 15)
    B2_GAIN3_D16 = TableField("B2_GAIN3", 16)
    B2_GAIN3_D17 = TableField("B2_GAIN3", 17)
    B2_GAIN3_D18 = TableField("B2_GAIN3", 18)
    B2_GAIN3_D19 = TableField("B2_GAIN3", 19)
    B2_GAIN3_D20 = TableField("B2_GAIN3", 20)
    B2_GAIN3_D21 = TableField("B2_GAIN3", 21)

    # BLOCK 2 GEWINN TABELLE 4
    B2_GAIN4_D1 = TableField("B2_GAIN4", 1)
    B2_GAIN4_D2 = TableField("B2_GAIN4", 2)
    B2_GAIN4_D3 = TableField("B2_GAIN4", 3)
    B2_GAIN4_D4 = TableField("B2_GAIN4", 4)
    B2_GAIN4_D5 = TableField("B2_GAIN4", 5)
    B2_GAIN4_D6 = TableField("B2_GAIN4", 6)
    B2_GAIN4_D7 = TableField("B2_GAIN4", 7)
    B2_GAIN4_D8 = TableField("B2_GAIN4", 8)
    B2_GAIN4_D9 = TableField("B2_GAIN4", 9)
    B2_GAIN4_D10 = TableField("B2_GAIN4", 10)
    B2_GAIN4_D11 = TableField("B2_GAIN4", 11)
    B2_GAIN4_D12 = TableField("B2_GAIN4", 12)
    B2_GAIN4_D13 = TableField("B2_GAIN4", 13)
    B2_GAIN4_D14 = TableField("B2_GAIN4", 14)
    B2_GAIN4_D15 = TableField("B2_GAIN4", 15)
    B2_GAIN4_D16 = TableField("B2_GAIN4", 16)
    B2_GAIN4_D17 = TableField("B2_GAIN4", 17)
    B2_GAIN4_D18 = TableField("B2_GAIN4", 18)
    B2_GAIN4_D19 = TableField("B2_GAIN4", 19)
    B2_GAIN4_D20 = TableField("B2_GAIN4", 20)
    B2_GAIN4_D21 = TableField("B2_GAIN4", 21)

    # BLOCK 2 GEWINN TABELLE 5
    B2_GAIN5_D1 = TableField("B2_GAIN5", 1)
    B2_GAIN5_D2 = TableField("B2_GAIN5", 2)
    B2_GAIN5_D3 = TableField("B2_GAIN5", 3)
    B2_GAIN5_D4 = TableField("B2_GAIN5", 4)
    B2_GAIN5_D5 = TableField("B2_GAIN5", 5)
    B2_GAIN5_D6 = TableField("B2_GAIN5", 6)
    B2_GAIN5_D7 = TableField("B2_GAIN5", 7)
    B2_GAIN5_D8 = TableField("B2_GAIN5", 8)
    B2_GAIN5_D9 = TableField("B2_GAIN5", 9)
    B2_GAIN5_D10 = TableField("B2_GAIN5", 10)
    B2_GAIN5_D11 = TableField("B2_GAIN5", 11)
    B2_GAIN5_D12 = TableField("B2_GAIN5", 12)
    B2_GAIN5_D13 = TableField("B2_GAIN5", 13)
    B2_GAIN5_D14 = TableField("B2_GAIN5", 14)
    B2_GAIN5_D15 = TableField("B2_GAIN5", 15)
    B2_GAIN5_D16 = TableField("B2_GAIN5", 16)
    B2_GAIN5_D17 = TableField("B2_GAIN5", 17)
    B2_GAIN5_D18 = TableField("B2_GAIN5", 18)
    B2_GAIN5_D19 = TableField("B2_GAIN5", 19)
    B2_GAIN5_D20 = TableField("B2_GAIN5", 20)
    B2_GAIN5_D21 = TableField("B2_GAIN5", 21)

    # BLOCK 2 GEWINN TABELLE 6
    B2_GAIN6_D1 = TableField("B2_GAIN6", 1)
    B2_GAIN6_D2 = TableField("B2_GAIN6", 2)
    B2_GAIN6_D3 = TableField("B2_GAIN6", 3)
    B2_GAIN6_D4 = TableField("B2_GAIN6", 4)
    B2_GAIN6_D5 = TableField("B2_GAIN6", 5)
    B2_GAIN6_D6 = TableField("B2_GAIN6", 6)
    B2_GAIN6_D7 = TableField("B2_GAIN6", 7)
    B2_GAIN6_D8 = TableField("B2_GAIN6", 8)
    B2_GAIN6_D9 = TableField("B2_GAIN6", 9)
    B2_GAIN6_D10 = TableField("B2_GAIN6", 10)
    B2_GAIN6_D11 = TableField("B2_GAIN6", 11)
    B2_GAIN6_D12 = TableField("B2_GAIN6", 12)
    B2_GAIN6_D13 = TableField("B2_GAIN6", 13)
    B2_GAIN6_D14 = TableField("B2_GAIN6", 14)
    B2_GAIN6_D15 = TableField("B2_GAIN6", 15)
    B2_GAIN6_D16 = TableField("B2_GAIN6", 16)
    B2_GAIN6_D17 = TableField("B2_GAIN6", 17)
    B2_GAIN6_D18 = TableField("B2_GAIN6", 18)
    B2_GAIN6_D19 = TableField("B2_GAIN6", 19)
    B2_GAIN6_D20 = TableField("B2_GAIN6", 20)
    B2_GAIN6_D21 = TableField("B2_GAIN6", 21)

    # BLOCK 2 GEWINN TABELLE 7
    B2_GAIN7_D1 = TableField("B2_GAIN7", 1)
    B2_GAIN7_D2 = TableField("B2_GAIN7", 2)
    B2_GAIN7_D3 = TableField("B2_GAIN7", 3)
    B2_GAIN7_D4 = TableField("B2_GAIN7", 4)
    B2_GAIN7_D5 = TableField("B2_GAIN7", 5)
    B2_GAIN7_D6 = TableField("B2_GAIN7", 6)
    B2_GAIN7_D7 = TableField("B2_GAIN7", 7)
    B2_GAIN7_D8 = TableField("B2_GAIN7", 8)
    B2_GAIN7_D9 = TableField("B2_GAIN7", 9)
    B2_GAIN7_D10 = TableField("B2_GAIN7", 10)
    B2_GAIN7_D11 = TableField("B2_GAIN7", 11)
    B2_GAIN7_D12 = TableField("B2_GAIN7", 12)
    B2_GAIN7_D13 = TableField("B2_GAIN7", 13)
    B2_GAIN7_D14 = TableField("B2_GAIN7", 14)
    B2_GAIN7_D15 = TableField("B2_GAIN7", 15)
    B2_GAIN7_D16 = TableField("B2_GAIN7", 16)
    B2_GAIN7_D17 = TableField("B2_GAIN7", 17)
    B2_GAIN7_D18 = TableField("B2_GAIN7", 18)
    B2_GAIN7_D19 = TableField("B2_GAIN7", 19)
    B2_GAIN7_D20 = TableField("B2_GAIN7", 20)
    B2_GAIN7_D21 = TableField("B2_GAIN7", 21)

    # BLOCK 2 GEWINN TABELLE 8
    B2_GAIN8_D1 = TableField("B2_GAIN8", 1)
    B2_GAIN8_D2 = TableField("B2_GAIN8", 2)
    B2_GAIN8_D3 = TableField("B2_GAIN8", 3)
    B2_GAIN8_D4 = TableField("B2_GAIN8", 4)
    B2_GAIN8_D5 = TableField("B2_GAIN8", 5)
    B2_GAIN8_D6 = TableField("B2_GAIN8", 6)
    B2_GAIN8_D7 = TableField("B2_GAIN8", 7)
    B2_GAIN8_D8 = TableField("B2_GAIN8", 8)
    B2_GAIN8_D9 = TableField("B2_GAIN8", 9)
    B2_GAIN8_D10 = TableField("B2_GAIN8", 10)
    B2_GAIN8_D11 = TableField("B2_GAIN8", 11)
    B2_GAIN8_D12 = TableField("B2_GAIN8", 12)
    B2_GAIN8_D13 = TableField("B2_GAIN8", 13)
    B2_GAIN8_D14 = TableField("B2_GAIN8", 14)
    B2_GAIN8_D15 = TableField("B2_GAIN8", 15)
    B2_GAIN8_D16 = TableField("B2_GAIN8", 16)
    B2_GAIN8_D17 = TableField("B2_GAIN8", 17)
    B2_GAIN8_D18 = TableField("B2_GAIN8", 18)
    B2_GAIN8_D19 = TableField("B2_GAIN8", 19)
    B2_GAIN8_D20 = TableField("B2_GAIN8", 20)
    B2_GAIN8_D21 = TableField("B2_GAIN8", 21)

    # BLOCK 2 GEWINN TABELLE 9
    B2_GAIN9_D1 = TableField("B2_GAIN9", 1)
    B2_GAIN9_D2 = TableField("B2_GAIN9", 2)
    B2_GAIN9_D3 = TableField("B2_GAIN9", 3)
    B2_GAIN9_D4 = TableField("B2_GAIN9", 4)
    B2_GAIN9_D5 = TableField("B2_GAIN9", 5)
    B2_GAIN9_D6 = TableField("B2_GAIN9", 6)
    B2_GAIN9_D7 = TableField("B2_GAIN9", 7)
    B2_GAIN9_D8 = TableField("B2_GAIN9", 8)
    B2_GAIN9_D9 = TableField("B2_GAIN9", 9)
    B2_GAIN9_D10 = TableField("B2_GAIN9", 10)
    B2_GAIN9_D11 = TableField("B2_GAIN9", 11)
    B2_GAIN9_D12 = TableField("B2_GAIN9", 12)
    B2_GAIN9_D13 = TableField("B2_GAIN9", 13)
    B2_GAIN9_D14 = TableField("B2_GAIN9", 14)
    B2_GAIN9_D15 = TableField("B2_GAIN9", 15)
    B2_GAIN9_D16 = TableField("B2_GAIN9", 16)
    B2_GAIN9_D17 = TableField("B2_GAIN9", 17)
    B2_GAIN9_D18 = TableField("B2_GAIN9", 18)
    B2_GAIN9_D19 = TableField("B2_GAIN9", 19)
    B2_GAIN9_D20 = TableField("B2_GAIN9", 20)
    B2_GAIN9_D21 = TableField("B2_GAIN9", 21)

    # BLOCK 2 GEWINN TABELLE 10
    B2_GAIN10_D1 = TableField("B2_GAIN10", 1)
    B2_GAIN10_D2 = TableField("B2_GAIN10", 2)
    B2_GAIN10_D3 = TableField("B2_GAIN10", 3)
    B2_GAIN10_D4 = TableField("B2_GAIN10", 4)
    B2_GAIN10_D5 = TableField("B2_GAIN10", 5)
    B2_GAIN10_D6 = TableField("B2_GAIN10", 6)
    B2_GAIN10_D7 = TableField("B2_GAIN10", 7)
    B2_GAIN10_D8 = TableField("B2_GAIN10", 8)
    B2_GAIN10_D9 = TableField("B2_GAIN10", 9)
    B2_GAIN10_D10 = TableField("B2_GAIN10", 10)
    B2_GAIN10_D11 = TableField("B2_GAIN10", 11)
    B2_GAIN10_D12 = TableField("B2_GAIN10", 12)
    B2_GAIN10_D13 = TableField("B2_GAIN10", 13)
    B2_GAIN10_D14 = TableField("B2_GAIN10", 14)
    B2_GAIN10_D15 = TableField("B2_GAIN10", 15)
    B2_GAIN10_D16 = TableField("B2_GAIN10", 16)
    B2_GAIN10_D17 = TableField("B2_GAIN10", 17)
    B2_GAIN10_D18 = TableField("B2_GAIN10", 18)
    B2_GAIN10_D19 = TableField("B2_GAIN10", 19)
    B2_GAIN10_D20 = TableField("B2_GAIN10", 20)
    B2_GAIN10_D21 = TableField("B2_GAIN10", 21)

    # BLOCK 2 GEWINN TABELLE 11
    B2_GAIN11_D1 = TableField("B2_GAIN11", 1)
    B2_GAIN11_D2 = TableField("B2_GAIN11", 2)
    B2_GAIN11_D3 = TableField("B2_GAIN11", 3)
    B2_GAIN11_D4 = TableField("B2_GAIN11", 4)
    B2_GAIN11_D5 = TableField("B2_GAIN11", 5)
    B2_GAIN11_D6 = TableField("B2_GAIN11", 6)
    B2_GAIN11_D7 = TableField("B2_GAIN11", 7)
    B2_GAIN11_D8 = TableField("B2_GAIN11", 8)
    B2_GAIN11_D9 = TableField("B2_GAIN11", 9)
    B2_GAIN11_D10 = TableField("B2_GAIN11", 10)
    B2_GAIN11_D11 = TableField("B2_GAIN11", 11)
    B2_GAIN11_D12 = TableField("B2_GAIN11", 12)
    B2_GAIN11_D13 = TableField("B2_GAIN11", 13)
    B2_GAIN11_D14 = TableField("B2_GAIN11", 14)
    B2_GAIN11_D15 = TableField("B2_GAIN11", 15)
    B2_GAIN11_D16 = TableField("B2_GAIN11", 16)
    B2_GAIN11_D17 = TableField("B2_GAIN11", 17)
    B2_GAIN11_D18 = TableField("B2_GAIN11", 18)
    B2_GAIN11_D19 = TableField("B2_GAIN11", 19)
    B2_GAIN11_D20 = TableField("B2_GAIN11", 20)
    B2_GAIN11_D21 = TableField("B2_GAIN11", 21)

    # BLOCK 2 GEWINN TABELLE 12
    B2_GAIN12_D1 = TableField("B2_GAIN12", 1)
    B2_GAIN12_D2 = TableField("B2_GAIN12", 2)
    B2_GAIN12_D3 = TableField("B2_GAIN12", 3)
    B2_GAIN12_D4 = TableField("B2_GAIN12", 4)
    B2_GAIN12_D5 = TableField("B2_GAIN12", 5)
    B2_GAIN12_D6 = TableField("B2_GAIN12", 6)
    B2_GAIN12_D7 = TableField("B2_GAIN12", 7)
    B2_GAIN12_D8 = TableField("B2_GAIN12", 8)
    B2_GAIN12_D9 = TableField("B2_GAIN12", 9)
    B2_GAIN12_D10 = TableField("B2_GAIN12", 10)
    B2_GAIN12_D11 = TableField("B2_GAIN12", 11)
    B2_GAIN12_D12 = TableField("B2_GAIN12", 12)
    B2_GAIN12_D13 = TableField("B2_GAIN12", 13)
    B2_GAIN12_D14 = TableField("B2_GAIN12", 14)
    B2_GAIN12_D15 = TableField("B2_GAIN12", 15)
    B2_GAIN12_D16 = TableField("B2_GAIN12", 16)
    B2_GAIN12_D17 = TableField("B2_GAIN12", 17)
    B2_GAIN12_D18 = TableField("B2_GAIN12", 18)
    B2_GAIN12_D19 = TableField("B2_GAIN12", 19)
    B2_GAIN12_D20 = TableField("B2_GAIN12", 20)
    B2_GAIN12_D21 = TableField("B2_GAIN12", 21)

    # BLOCK 2 GEWINN TABELLE 13
    B2_GAIN13_D1 = TableField("B2_GAIN13", 1)
    B2_GAIN13_D2 = TableField("B2_GAIN13", 2)
    B2_GAIN13_D3 = TableField("B2_GAIN13", 3)
    B2_GAIN13_D4 = TableField("B2_GAIN13", 4)
    B2_GAIN13_D5 = TableField("B2_GAIN13", 5)
    B2_GAIN13_D6 = TableField("B2_GAIN13", 6)
    B2_GAIN13_D7 = TableField("B2_GAIN13", 7)
    B2_GAIN13_D8 = TableField("B2_GAIN13", 8)
    B2_GAIN13_D9 = TableField("B2_GAIN13", 9)
    B2_GAIN13_D10 = TableField("B2_GAIN13", 10)
    B2_GAIN13_D11 = TableField("B2_GAIN13", 11)
    B2_GAIN13_D12 = TableField("B2_GAIN13", 12)
    B2_GAIN13_D13 = TableField("B2_GAIN13", 13)
    B2_GAIN13_D14 = TableField("B2_GAIN13", 14)
    B2_GAIN13_D15 = TableField("B2_GAIN13", 15)
    B2_GAIN13_D16 = TableField("B2_GAIN13", 16)
    B2_GAIN13_D17 = TableField("B2_GAIN13", 17)
    B2_GAIN13_D18 = TableField("B2_GAIN13", 18)
    B2_GAIN13_D19 = TableField("B2_GAIN13", 19)
    B2_GAIN13_D20 = TableField("B2_GAIN13", 20)
    B2_GAIN13_D21 = TableField("B2_GAIN13", 21)

    # BLOCK 2 GEWINN TABELLE 14
    B2_GAIN14_D1 = TableField("B2_GAIN14", 1)
    B2_GAIN14_D2 = TableField("B2_GAIN14", 2)
    B2_GAIN14_D3 = TableField("B2_GAIN14", 3)
    B2_GAIN14_D4 = TableField("B2_GAIN14", 4)
    B2_GAIN14_D5 = TableField("B2_GAIN14", 5)
    B2_GAIN14_D6 = TableField("B2_GAIN14", 6)
    B2_GAIN14_D7 = TableField("B2_GAIN14", 7)
    B2_GAIN14_D8 = TableField("B2_GAIN14", 8)
    B2_GAIN14_D9 = TableField("B2_GAIN14", 9)
    B2_GAIN14_D10 = TableField("B2_GAIN14", 10)
    B2_GAIN14_D11 = TableField("B2_GAIN14", 11)
    B2_GAIN14_D12 = TableField("B2_GAIN14", 12)
    B2_GAIN14_D13 = TableField("B2_GAIN14", 13)
    B2_GAIN14_D14 = TableField("B2_GAIN14", 14)
    B2_GAIN14_D15 = TableField("B2_GAIN14", 15)
    B2_GAIN14_D16 = TableField("B2_GAIN14", 16)
    B2_GAIN14_D17 = TableField("B2_GAIN14", 17)
    B2_GAIN14_D18 = TableField("B2_GAIN14", 18)
    B2_GAIN14_D19 = TableField("B2_GAIN14", 19)
    B2_GAIN14_D20 = TableField("B2_GAIN14", 20)
    B2_GAIN14_D21 = TableField("B2_GAIN14", 21)

    # BLOCK 2 GEWINN TABELLE 15
    B2_GAIN15_D1 = TableField("B2_GAIN15", 1)
    B2_GAIN15_D2 = TableField("B2_GAIN15", 2)
    B2_GAIN15_D3 = TableField("B2_GAIN15", 3)
    B2_GAIN15_D4 = TableField("B2_GAIN15", 4)
    B2_GAIN15_D5 = TableField("B2_GAIN15", 5)
    B2_GAIN15_D6 = TableField("B2_GAIN15", 6)
    B2_GAIN15_D7 = TableField("B2_GAIN15", 7)
    B2_GAIN15_D8 = TableField("B2_GAIN15", 8)
    B2_GAIN15_D9 = TableField("B2_GAIN15", 9)
    B2_GAIN15_D10 = TableField("B2_GAIN15", 10)
    B2_GAIN15_D11 = TableField("B2_GAIN15", 11)
    B2_GAIN15_D12 = TableField("B2_GAIN15", 12)
    B2_GAIN15_D13 = TableField("B2_GAIN15", 13)
    B2_GAIN15_D14 = TableField("B2_GAIN15", 14)
    B2_GAIN15_D15 = TableField("B2_GAIN15", 15)
    B2_GAIN15_D16 = TableField("B2_GAIN15", 16)
    B2_GAIN15_D17 = TableField("B2_GAIN15", 17)
    B2_GAIN15_D18 = TableField("B2_GAIN15", 18)
    B2_GAIN15_D19 = TableField("B2_GAIN15", 19)
    B2_GAIN15_D20 = TableField("B2_GAIN15", 20)
    B2_GAIN15_D21 = TableField("B2_GAIN15", 21)

    # BLOCK 2 GEWINN TABELLE 16
    B2_GAIN16_D1 = TableField("B2_GAIN16", 1)
    B2_GAIN16_D2 = TableField("B2_GAIN16", 2)
    B2_GAIN16_D3 = TableField("B2_GAIN16", 3)
    B2_GAIN16_D4 = TableField("B2_GAIN16", 4)
    B2_GAIN16_D5 = TableField("B2_GAIN16", 5)
    B2_GAIN16_D6 = TableField("B2_GAIN16", 6)
    B2_GAIN16_D7 = TableField("B2_GAIN16", 7)
    B2_GAIN16_D8 = TableField("B2_GAIN16", 8)
    B2_GAIN16_D9 = TableField("B2_GAIN16", 9)
    B2_GAIN16_D10 = TableField("B2_GAIN16", 10)
    B2_GAIN16_D11 = TableField("B2_GAIN16", 11)
    B2_GAIN16_D12 = TableField("B2_GAIN16", 12)
    B2_GAIN16_D13 = TableField("B2_GAIN16", 13)
    B2_GAIN16_D14 = TableField("B2_GAIN16", 14)
    B2_GAIN16_D15 = TableField("B2_GAIN16", 15)
    B2_GAIN16_D16 = TableField("B2_GAIN16", 16)
    B2_GAIN16_D17 = TableField("B2_GAIN16", 17)
    B2_GAIN16_D18 = TableField("B2_GAIN16", 18)
    B2_GAIN16_D19 = TableField("B2_GAIN16", 19)
    B2_GAIN16_D20 = TableField("B2_GAIN16", 20)
    B2_GAIN16_D21 = TableField("B2_GAIN16", 21)

    # BLOCK 2 GEWINN TABELLE 17
    B2_GAIN17_D1 = TableField("B2_GAIN17", 1)
    B2_GAIN17_D2 = TableField("B2_GAIN17", 2)
    B2_GAIN17_D3 = TableField("B2_GAIN17", 3)
    B2_GAIN17_D4 = TableField("B2_GAIN17", 4)
    B2_GAIN17_D5 = TableField("B2_GAIN17", 5)
    B2_GAIN17_D6 = TableField("B2_GAIN17", 6)
    B2_GAIN17_D7 = TableField("B2_GAIN17", 7)
    B2_GAIN17_D8 = TableField("B2_GAIN17", 8)
    B2_GAIN17_D9 = TableField("B2_GAIN17", 9)
    B2_GAIN17_D10 = TableField("B2_GAIN17", 10)
    B2_GAIN17_D11 = TableField("B2_GAIN17", 11)
    B2_GAIN17_D12 = TableField("B2_GAIN17", 12)
    B2_GAIN17_D13 = TableField("B2_GAIN17", 13)
    B2_GAIN17_D14 = TableField("B2_GAIN17", 14)
    B2_GAIN17_D15 = TableField("B2_GAIN17", 15)
    B2_GAIN17_D16 = TableField("B2_GAIN17", 16)
    B2_GAIN17_D17 = TableField("B2_GAIN17", 17)
    B2_GAIN17_D18 = TableField("B2_GAIN17", 18)
    B2_GAIN17_D19 = TableField("B2_GAIN17", 19)
    B2_GAIN17_D20 = TableField("B2_GAIN17", 20)
    B2_GAIN17_D21 = TableField("B2_GAIN17", 21)

    # BLOCK 2 GEWINN TABELLE 18
    B2_GAIN18_D1 = TableField("B2_GAIN18", 1)
    B2_GAIN18_D2 = TableField("B2_GAIN18", 2)
    B2_GAIN18_D3 = TableField("B2_GAIN18", 3)
    B2_GAIN18_D4 = TableField("B2_GAIN18", 4)
    B2_GAIN18_D5 = TableField("B2_GAIN18", 5)
    B2_GAIN18_D6 = TableField("B2_GAIN18", 6)
    B2_GAIN18_D7 = TableField("B2_GAIN18", 7)
    B2_GAIN18_D8 = TableField("B2_GAIN18", 8)
    B2_GAIN18_D9 = TableField("B2_GAIN18", 9)
    B2_GAIN18_D10 = TableField("B2_GAIN18", 10)
    B2_GAIN18_D11 = TableField("B2_GAIN18", 11)
    B2_GAIN18_D12 = TableField("B2_GAIN18", 12)
    B2_GAIN18_D13 = TableField("B2_GAIN18", 13)
    B2_GAIN18_D14 = TableField("B2_GAIN18", 14)
    B2_GAIN18_D15 = TableField("B2_GAIN18", 15)
    B2_GAIN18_D16 = TableField("B2_GAIN18", 16)
    B2_GAIN18_D17 = TableField("B2_GAIN18", 17)
    B2_GAIN18_D18 = TableField("B2_GAIN18", 18)
    B2_GAIN18_D19 = TableField("B2_GAIN18", 19)
    B2_GAIN18_D20 = TableField("B2_GAIN18", 20)
    B2_GAIN18_D21 = TableField("B2_GAIN18", 21)

    # BLOCK 2 GEWINN TABELLE 19
    B2_GAIN19_D1 = TableField("B2_GAIN19", 1)
    B2_GAIN19_D2 = TableField("B2_GAIN19", 2)
    B2_GAIN19_D3 = TableField("B2_GAIN19", 3)
    B2_GAIN19_D4 = TableField("B2_GAIN19", 4)
    B2_GAIN19_D5 = TableField("B2_GAIN19", 5)
    B2_GAIN19_D6 = TableField("B2_GAIN19", 6)
    B2_GAIN19_D7 = TableField("B2_GAIN19", 7)
    B2_GAIN19_D8 = TableField("B2_GAIN19", 8)
    B2_GAIN19_D9 = TableField("B2_GAIN19", 9)
    B2_GAIN19_D10 = TableField("B2_GAIN19", 10)
    B2_GAIN19_D11 = TableField("B2_GAIN19", 11)
    B2_GAIN19_D12 = TableField("B2_GAIN19", 12)
    B2_GAIN19_D13 = TableField("B2_GAIN19", 13)
    B2_GAIN19_D14 = TableField("B2_GAIN19", 14)
    B2_GAIN19_D15 = TableField("B2_GAIN19", 15)
    B2_GAIN19_D16 = TableField("B2_GAIN19", 16)
    B2_GAIN19_D17 = TableField("B2_GAIN19", 17)
    B2_GAIN19_D18 = TableField("B2_GAIN19", 18)
    B2_GAIN19_D19 = TableField("B2_GAIN19", 19)
    B2_GAIN19_D20 = TableField("B2_GAIN19", 20)
    B2_GAIN19_D21 = TableField("B2_GAIN19", 21)

    # BLOCK 2 GEWINN TABELLE 20
    B2_GAIN20_D1 = TableField("B2_GAIN20", 1)
    B2_GAIN20_D2 = TableField("B2_GAIN20", 2)
    B2_GAIN20_D3 = TableField("B2_GAIN20", 3)
    B2_GAIN20_D4 = TableField("B2_GAIN20", 4)
    B2_GAIN20_D5 = TableField("B2_GAIN20", 5)
    B2_GAIN20_D6 = TableField("B2_GAIN20", 6)
    B2_GAIN20_D7 = TableField("B2_GAIN20", 7)
    B2_GAIN20_D8 = TableField("B2_GAIN20", 8)
    B2_GAIN20_D9 = TableField("B2_GAIN20", 9)
    B2_GAIN20_D10 = TableField("B2_GAIN20", 10)
    B2_GAIN20_D11 = TableField("B2_GAIN20", 11)
    B2_GAIN20_D12 = TableField("B2_GAIN20", 12)
    B2_GAIN20_D13 = TableField("B2_GAIN20", 13)
    B2_GAIN20_D14 = TableField("B2_GAIN20", 14)
    B2_GAIN20_D15 = TableField("B2_GAIN20", 15)
    B2_GAIN20_D16 = TableField("B2_GAIN20", 16)
    B2_GAIN20_D17 = TableField("B2_GAIN20", 17)
    B2_GAIN20_D18 = TableField("B2_GAIN20", 18)
    B2_GAIN20_D19 = TableField("B2_GAIN20", 19)
    B2_GAIN20_D20 = TableField("B2_GAIN20", 20)
    B2_GAIN20_D21 = TableField("B2_GAIN20", 21)

    # BLOCK 2 VERLUST TABELLE 1
    B2_LOSS1_D1 = TableField("B2_LOSS1", 1)
    B2_LOSS1_D2 = TableField("B2_LOSS1", 2)
    B2_LOSS1_D3 = TableField("B2_LOSS1", 3)
    B2_LOSS1_D4 = TableField("B2_LOSS1", 4)
    B2_LOSS1_D5 = TableField("B2_LOSS1", 5)
    B2_LOSS1_D6 = TableField("B2_LOSS1", 6)
    B2_LOSS1_D7 = TableField("B2_LOSS1", 7)
    B2_LOSS1_D8 = TableField("B2_LOSS1", 8)
    B2_LOSS1_D9 = TableField("B2_LOSS1", 9)
    B2_LOSS1_D10 = TableField("B2_LOSS1", 10)
    B2_LOSS1_D11 = TableField("B2_LOSS1", 11)
    B2_LOSS1_D12 = TableField("B2_LOSS1", 12)
    B2_LOSS1_D13 = TableField("B2_LOSS1", 13)
    B2_LOSS1_D14 = TableField("B2_LOSS1", 14)
    B2_LOSS1_D15 = TableField("B2_LOSS1", 15)
    B2_LOSS1_D16 = TableField("B2_LOSS1", 16)
    B2_LOSS1_D17 = TableField("B2_LOSS1", 17)
    B2_LOSS1_D18 = TableField("B2_LOSS1", 18)
    B2_LOSS1_D19 = TableField("B2_LOSS1", 19)
    B2_LOSS1_D20 = TableField("B2_LOSS1", 20)
    B2_LOSS1_D21 = TableField("B2_LOSS1", 21)

    # BLOCK 2 VERLUST TABELLE 2
    B2_LOSS2_D1 = TableField("B2_LOSS2", 1)
    B2_LOSS2_D2 = TableField("B2_LOSS2", 2)
    B2_LOSS2_D3 = TableField("B2_LOSS2", 3)
    B2_LOSS2_D4 = TableField("B2_LOSS2", 4)
    B2_LOSS2_D5 = TableField("B2_LOSS2", 5)
    B2_LOSS2_D6 = TableField("B2_LOSS2", 6)
    B2_LOSS2_D7 = TableField("B2_LOSS2", 7)
    B2_LOSS2_D8 = TableField("B2_LOSS2", 8)
    B2_LOSS2_D9 = TableField("B2_LOSS2", 9)
    B2_LOSS2_D10 = TableField("B2_LOSS2", 10)
    B2_LOSS2_D11 = TableField("B2_LOSS2", 11)
    B2_LOSS2_D12 = TableField("B2_LOSS2", 12)
    B2_LOSS2_D13 = TableField("B2_LOSS2", 13)
    B2_LOSS2_D14 = TableField("B2_LOSS2", 14)
    B2_LOSS2_D15 = TableField("B2_LOSS2", 15)
    B2_LOSS2_D16 = TableField("B2_LOSS2", 16)
    B2_LOSS2_D17 = TableField("B2_LOSS2", 17)
    B2_LOSS2_D18 = TableField("B2_LOSS2", 18)
    B2_LOSS2_D19 = TableField("B2_LOSS2", 19)
    B2_LOSS2_D20 = TableField("B2_LOSS2", 20)
    B2_LOSS2_D21 = TableField("B2_LOSS2", 21)

    # BLOCK 2 VERLUST TABELLE 3
    B2_LOSS3_D1 = TableField("B2_LOSS3", 1)
    B2_LOSS3_D2 = TableField("B2_LOSS3", 2)
    B2_LOSS3_D3 = TableField("B2_LOSS3", 3)
    B2_LOSS3_D4 = TableField("B2_LOSS3", 4)
    B2_LOSS3_D5 = TableField("B2_LOSS3", 5)
    B2_LOSS3_D6 = TableField("B2_LOSS3", 6)
    B2_LOSS3_D7 = TableField("B2_LOSS3", 7)
    B2_LOSS3_D8 = TableField("B2_LOSS3", 8)
    B2_LOSS3_D9 = TableField("B2_LOSS3", 9)
    B2_LOSS3_D10 = TableField("B2_LOSS3", 10)
    B2_LOSS3_D11 = TableField("B2_LOSS3", 11)
    B2_LOSS3_D12 = TableField("B2_LOSS3", 12)
    B2_LOSS3_D13 = TableField("B2_LOSS3", 13)
    B2_LOSS3_D14 = TableField("B2_LOSS3", 14)
    B2_LOSS3_D15 = TableField("B2_LOSS3", 15)
    B2_LOSS3_D16 = TableField("B2_LOSS3", 16)
    B2_LOSS3_D17 = TableField("B2_LOSS3", 17)
    B2_LOSS3_D18 = TableField("B2_LOSS3", 18)
    B2_LOSS3_D19 = TableField("B2_LOSS3", 19)
    B2_LOSS3_D20 = TableField("B2_LOSS3", 20)
    B2_LOSS3_D21 = TableField("B2_LOSS3", 21)

    # BLOCK 2 VERLUST TABELLE 4
    B2_LOSS4_D1 = TableField("B2_LOSS4", 1)
    B2_LOSS4_D2 = TableField("B2_LOSS4", 2)
    B2_LOSS4_D3 = TableField("B2_LOSS4", 3)
    B2_LOSS4_D4 = TableField("B2_LOSS4", 4)
    B2_LOSS4_D5 = TableField("B2_LOSS4", 5)
    B2_LOSS4_D6 = TableField("B2_LOSS4", 6)
    B2_LOSS4_D7 = TableField("B2_LOSS4", 7)
    B2_LOSS4_D8 = TableField("B2_LOSS4", 8)
    B2_LOSS4_D9 = TableField("B2_LOSS4", 9)
    B2_LOSS4_D10 = TableField("B2_LOSS4", 10)
    B2_LOSS4_D11 = TableField("B2_LOSS4", 11)
    B2_LOSS4_D12 = TableField("B2_LOSS4", 12)
    B2_LOSS4_D13 = TableField("B2_LOSS4", 13)
    B2_LOSS4_D14 = TableField("B2_LOSS4", 14)
    B2_LOSS4_D15 = TableField("B2_LOSS4", 15)
    B2_LOSS4_D16 = TableField("B2_LOSS4", 16)
    B2_LOSS4_D17 = TableField("B2_LOSS4", 17)
    B2_LOSS4_D18 = TableField("B2_LOSS4", 18)
    B2_LOSS4_D19 = TableField("B2_LOSS4", 19)
    B2_LOSS4_D20 = TableField("B2_LOSS4", 20)
    B2_LOSS4_D21 = TableField("B2_LOSS4", 21)

    # BLOCK 2 VERLUST TABELLE 5
    B2_LOSS5_D1 = TableField("B2_LOSS5", 1)
    B2_LOSS5_D2 = TableField("B2_LOSS5", 2)
    B2_LOSS5_D3 = TableField("B2_LOSS5", 3)
    B2_LOSS5_D4 = TableField("B2_LOSS5", 4)
    B2_LOSS5_D5 = TableField("B2_LOSS5", 5)
    B2_LOSS5_D6 = TableField("B2_LOSS5", 6)
    B2_LOSS5_D7 = TableField("B2_LOSS5", 7)
    B2_LOSS5_D8 = TableField("B2_LOSS5", 8)
    B2_LOSS5_D9 = TableField("B2_LOSS5", 9)
    B2_LOSS5_D10 = TableField("B2_LOSS5", 10)
    B2_LOSS5_D11 = TableField("B2_LOSS5", 11)
    B2_LOSS5_D12 = TableField("B2_LOSS5", 12)
    B2_LOSS5_D13 = TableField("B2_LOSS5", 13)
    B2_LOSS5_D14 = TableField("B2_LOSS5", 14)
    B2_LOSS5_D15 = TableField("B2_LOSS5", 15)
    B2_LOSS5_D16 = TableField("B2_LOSS5", 16)
    B2_LOSS5_D17 = TableField("B2_LOSS5", 17)
    B2_LOSS5_D18 = TableField("B2_LOSS5", 18)
    B2_LOSS5_D19 = TableField("B2_LOSS5", 19)
    B2_LOSS5_D20 = TableField("B2_LOSS5", 20)
    B2_LOSS5_D21 = TableField("B2_LOSS5", 21)

    # BLOCK 2 VERLUST TABELLE 6
    B2_LOSS6_D1 = TableField("B2_LOSS6", 1)
    B2_LOSS6_D2 = TableField("B2_LOSS6", 2)
    B2_LOSS6_D3 = TableField("B2_LOSS6", 3)
    B2_LOSS6_D4 = TableField("B2_LOSS6", 4)
    B2_LOSS6_D5 = TableField("B2_LOSS6", 5)
    B2_LOSS6_D6 = TableField("B2_LOSS6", 6)
    B2_LOSS6_D7 = TableField("B2_LOSS6", 7)
    B2_LOSS6_D8 = TableField("B2_LOSS6", 8)
    B2_LOSS6_D9 = TableField("B2_LOSS6", 9)
    B2_LOSS6_D10 = TableField("B2_LOSS6", 10)
    B2_LOSS6_D11 = TableField("B2_LOSS6", 11)
    B2_LOSS6_D12 = TableField("B2_LOSS6", 12)
    B2_LOSS6_D13 = TableField("B2_LOSS6", 13)
    B2_LOSS6_D14 = TableField("B2_LOSS6", 14)
    B2_LOSS6_D15 = TableField("B2_LOSS6", 15)
    B2_LOSS6_D16 = TableField("B2_LOSS6", 16)
    B2_LOSS6_D17 = TableField("B2_LOSS6", 17)
    B2_LOSS6_D18 = TableField("B2_LOSS6", 18)
    B2_LOSS6_D19 = TableField("B2_LOSS6", 19)
    B2_LOSS6_D20 = TableField("B2_LOSS6", 20)
    B2_LOSS6_D21 = TableField("B2_LOSS6", 21)

    # BLOCK 2 VERLUST TABELLE 7
    B2_LOSS7_D1 = TableField("B2_LOSS7", 1)
    B2_LOSS7_D2 = TableField("B2_LOSS7", 2)
    B2_LOSS7_D3 = TableField("B2_LOSS7", 3)
    B2_LOSS7_D4 = TableField("B2_LOSS7", 4)
    B2_LOSS7_D5 = TableField("B2_LOSS7", 5)
    B2_LOSS7_D6 = TableField("B2_LOSS7", 6)
    B2_LOSS7_D7 = TableField("B2_LOSS7", 7)
    B2_LOSS7_D8 = TableField("B2_LOSS7", 8)
    B2_LOSS7_D9 = TableField("B2_LOSS7", 9)
    B2_LOSS7_D10 = TableField("B2_LOSS7", 10)
    B2_LOSS7_D11 = TableField("B2_LOSS7", 11)
    B2_LOSS7_D12 = TableField("B2_LOSS7", 12)
    B2_LOSS7_D13 = TableField("B2_LOSS7", 13)
    B2_LOSS7_D14 = TableField("B2_LOSS7", 14)
    B2_LOSS7_D15 = TableField("B2_LOSS7", 15)
    B2_LOSS7_D16 = TableField("B2_LOSS7", 16)
    B2_LOSS7_D17 = TableField("B2_LOSS7", 17)
    B2_LOSS7_D18 = TableField("B2_LOSS7", 18)
    B2_LOSS7_D19 = TableField("B2_LOSS7", 19)
    B2_LOSS7_D20 = TableField("B2_LOSS7", 20)
    B2_LOSS7_D21 = TableField("B2_LOSS7", 21)

    # BLOCK 2 VERLUST TABELLE 8
    B2_LOSS8_D1 = TableField("B2_LOSS8", 1)
    B2_LOSS8_D2 = TableField("B2_LOSS8", 2)
    B2_LOSS8_D3 = TableField("B2_LOSS8", 3)
    B2_LOSS8_D4 = TableField("B2_LOSS8", 4)
    B2_LOSS8_D5 = TableField("B2_LOSS8", 5)
    B2_LOSS8_D6 = TableField("B2_LOSS8", 6)
    B2_LOSS8_D7 = TableField("B2_LOSS8", 7)
    B2_LOSS8_D8 = TableField("B2_LOSS8", 8)
    B2_LOSS8_D9 = TableField("B2_LOSS8", 9)
    B2_LOSS8_D10 = TableField("B2_LOSS8", 10)
    B2_LOSS8_D11 = TableField("B2_LOSS8", 11)
    B2_LOSS8_D12 = TableField("B2_LOSS8", 12)
    B2_LOSS8_D13 = TableField("B2_LOSS8", 13)
    B2_LOSS8_D14 = TableField("B2_LOSS8", 14)
    B2_LOSS8_D15 = TableField("B2_LOSS8", 15)
    B2_LOSS8_D16 = TableField("B2_LOSS8", 16)
    B2_LOSS8_D17 = TableField("B2_LOSS8", 17)
    B2_LOSS8_D18 = TableField("B2_LOSS8", 18)
    B2_LOSS8_D19 = TableField("B2_LOSS8", 19)
    B2_LOSS8_D20 = TableField("B2_LOSS8", 20)
    B2_LOSS8_D21 = TableField("B2_LOSS8", 21)

    # BLOCK 2 VERLUST TABELLE 9
    B2_LOSS9_D1 = TableField("B2_LOSS9", 1)
    B2_LOSS9_D2 = TableField("B2_LOSS9", 2)
    B2_LOSS9_D3 = TableField("B2_LOSS9", 3)
    B2_LOSS9_D4 = TableField("B2_LOSS9", 4)
    B2_LOSS9_D5 = TableField("B2_LOSS9", 5)
    B2_LOSS9_D6 = TableField("B2_LOSS9", 6)
    B2_LOSS9_D7 = TableField("B2_LOSS9", 7)
    B2_LOSS9_D8 = TableField("B2_LOSS9", 8)
    B2_LOSS9_D9 = TableField("B2_LOSS9", 9)
    B2_LOSS9_D10 = TableField("B2_LOSS9", 10)
    B2_LOSS9_D11 = TableField("B2_LOSS9", 11)
    B2_LOSS9_D12 = TableField("B2_LOSS9", 12)
    B2_LOSS9_D13 = TableField("B2_LOSS9", 13)
    B2_LOSS9_D14 = TableField("B2_LOSS9", 14)
    B2_LOSS9_D15 = TableField("B2_LOSS9", 15)
    B2_LOSS9_D16 = TableField("B2_LOSS9", 16)
    B2_LOSS9_D17 = TableField("B2_LOSS9", 17)
    B2_LOSS9_D18 = TableField("B2_LOSS9", 18)
    B2_LOSS9_D19 = TableField("B2_LOSS9", 19)
    B2_LOSS9_D20 = TableField("B2_LOSS9", 20)
    B2_LOSS9_D21 = TableField("B2_LOSS9", 21)

    # BLOCK 2 VERLUST TABELLE 10
    B2_LOSS10_D1 = TableField("B2_LOSS10", 1)
    B2_LOSS10_D2 = TableField("B2_LOSS10", 2)
    B2_LOSS10_D3 = TableField("B2_LOSS10", 3)
    B2_LOSS10_D4 = TableField("B2_LOSS10", 4)
    B2_LOSS10_D5 = TableField("B2_LOSS10", 5)
    B2_LOSS10_D6 = TableField("B2_LOSS10", 6)
    B2_LOSS10_D7 = TableField("B2_LOSS10", 7)
    B2_LOSS10_D8 = TableField("B2_LOSS10", 8)
    B2_LOSS10_D9 = TableField("B2_LOSS10", 9)
    B2_LOSS10_D10 = TableField("B2_LOSS10", 10)
    B2_LOSS10_D11 = TableField("B2_LOSS10", 11)
    B2_LOSS10_D12 = TableField("B2_LOSS10", 12)
    B2_LOSS10_D13 = TableField("B2_LOSS10", 13)
    B2_LOSS10_D14 = TableField("B2_LOSS10", 14)
    B2_LOSS10_D15 = TableField("B2_LOSS10", 15)
    B2_LOSS10_D16 = TableField("B2_LOSS10", 16)
    B2_LOSS10_D17 = TableField("B2_LOSS10", 17)
    B2_LOSS10_D18 = TableField("B2_LOSS10", 18)
    B2_LOSS10_D19 = TableField("B2_LOSS10", 19)
    B2_LOSS10_D20 = TableField("B2_LOSS10", 20)
    B2_LOSS10_D21 = TableField("B2_LOSS10", 21)

    # BLOCK 2 VERLUST TABELLE 11
    B2_LOSS11_D1 = TableField("B2_LOSS11", 1)
    B2_LOSS11_D2 = TableField("B2_LOSS11", 2)
    B2_LOSS11_D3 = TableField("B2_LOSS11", 3)
    B2_LOSS11_D4 = TableField("B2_LOSS11", 4)
    B2_LOSS11_D5 = TableField("B2_LOSS11", 5)
    B2_LOSS11_D6 = TableField("B2_LOSS11", 6)
    B2_LOSS11_D7 = TableField("B2_LOSS11", 7)
    B2_LOSS11_D8 = TableField("B2_LOSS11", 8)
    B2_LOSS11_D9 = TableField("B2_LOSS11", 9)
    B2_LOSS11_D10 = TableField("B2_LOSS11", 10)
    B2_LOSS11_D11 = TableField("B2_LOSS11", 11)
    B2_LOSS11_D12 = TableField("B2_LOSS11", 12)
    B2_LOSS11_D13 = TableField("B2_LOSS11", 13)
    B2_LOSS11_D14 = TableField("B2_LOSS11", 14)
    B2_LOSS11_D15 = TableField("B2_LOSS11", 15)
    B2_LOSS11_D16 = TableField("B2_LOSS11", 16)
    B2_LOSS11_D17 = TableField("B2_LOSS11", 17)
    B2_LOSS11_D18 = TableField("B2_LOSS11", 18)
    B2_LOSS11_D19 = TableField("B2_LOSS11", 19)
    B2_LOSS11_D20 = TableField("B2_LOSS11", 20)
    B2_LOSS11_D21 = TableField("B2_LOSS11", 21)

    # BLOCK 2 VERLUST TABELLE 12
    B2_LOSS12_D1 = TableField("B2_LOSS12", 1)
    B2_LOSS12_D2 = TableField("B2_LOSS12", 2)
    B2_LOSS12_D3 = TableField("B2_LOSS12", 3)
    B2_LOSS12_D4 = TableField("B2_LOSS12", 4)
    B2_LOSS12_D5 = TableField("B2_LOSS12", 5)
    B2_LOSS12_D6 = TableField("B2_LOSS12", 6)
    B2_LOSS12_D7 = TableField("B2_LOSS12", 7)
    B2_LOSS12_D8 = TableField("B2_LOSS12", 8)
    B2_LOSS12_D9 = TableField("B2_LOSS12", 9)
    B2_LOSS12_D10 = TableField("B2_LOSS12", 10)
    B2_LOSS12_D11 = TableField("B2_LOSS12", 11)
    B2_LOSS12_D12 = TableField("B2_LOSS12", 12)
    B2_LOSS12_D13 = TableField("B2_LOSS12", 13)
    B2_LOSS12_D14 = TableField("B2_LOSS12", 14)
    B2_LOSS12_D15 = TableField("B2_LOSS12", 15)
    B2_LOSS12_D16 = TableField("B2_LOSS12", 16)
    B2_LOSS12_D17 = TableField("B2_LOSS12", 17)
    B2_LOSS12_D18 = TableField("B2_LOSS12", 18)
    B2_LOSS12_D19 = TableField("B2_LOSS12", 19)
    B2_LOSS12_D20 = TableField("B2_LOSS12", 20)
    B2_LOSS12_D21 = TableField("B2_LOSS12", 21)

    # BLOCK 2 VERLUST TABELLE 13
    B2_LOSS13_D1 = TableField("B2_LOSS13", 1)
    B2_LOSS13_D2 = TableField("B2_LOSS13", 2)
    B2_LOSS13_D3 = TableField("B2_LOSS13", 3)
    B2_LOSS13_D4 = TableField("B2_LOSS13", 4)
    B2_LOSS13_D5 = TableField("B2_LOSS13", 5)
    B2_LOSS13_D6 = TableField("B2_LOSS13", 6)
    B2_LOSS13_D7 = TableField("B2_LOSS13", 7)
    B2_LOSS13_D8 = TableField("B2_LOSS13", 8)
    B2_LOSS13_D9 = TableField("B2_LOSS13", 9)
    B2_LOSS13_D10 = TableField("B2_LOSS13", 10)
    B2_LOSS13_D11 = TableField("B2_LOSS13", 11)
    B2_LOSS13_D12 = TableField("B2_LOSS13", 12)
    B2_LOSS13_D13 = TableField("B2_LOSS13", 13)
    B2_LOSS13_D14 = TableField("B2_LOSS13", 14)
    B2_LOSS13_D15 = TableField("B2_LOSS13", 15)
    B2_LOSS13_D16 = TableField("B2_LOSS13", 16)
    B2_LOSS13_D17 = TableField("B2_LOSS13", 17)
    B2_LOSS13_D18 = TableField("B2_LOSS13", 18)
    B2_LOSS13_D19 = TableField("B2_LOSS13", 19)
    B2_LOSS13_D20 = TableField("B2_LOSS13", 20)
    B2_LOSS13_D21 = TableField("B2_LOSS13", 21)

    # BLOCK 2 VERLUST TABELLE 14
    B2_LOSS14_D1 = TableField("B2_LOSS14", 1)
    B2_LOSS14_D2 = TableField("B2_LOSS14", 2)
    B2_LOSS14_D3 = TableField("B2_LOSS14", 3)
    B2_LOSS14_D4 = TableField("B2_LOSS14", 4)
    B2_LOSS14_D5 = TableField("B2_LOSS14", 5)
    B2_LOSS14_D6 = TableField("B2_LOSS14", 6)
    B2_LOSS14_D7 = TableField("B2_LOSS14", 7)
    B2_LOSS14_D8 = TableField("B2_LOSS14", 8)
    B2_LOSS14_D9 = TableField("B2_LOSS14", 9)
    B2_LOSS14_D10 = TableField("B2_LOSS14", 10)
    B2_LOSS14_D11 = TableField("B2_LOSS14", 11)
    B2_LOSS14_D12 = TableField("B2_LOSS14", 12)
    B2_LOSS14_D13 = TableField("B2_LOSS14", 13)
    B2_LOSS14_D14 = TableField("B2_LOSS14", 14)
    B2_LOSS14_D15 = TableField("B2_LOSS14", 15)
    B2_LOSS14_D16 = TableField("B2_LOSS14", 16)
    B2_LOSS14_D17 = TableField("B2_LOSS14", 17)
    B2_LOSS14_D18 = TableField("B2_LOSS14", 18)
    B2_LOSS14_D19 = TableField("B2_LOSS14", 19)
    B2_LOSS14_D20 = TableField("B2_LOSS14", 20)
    B2_LOSS14_D21 = TableField("B2_LOSS14", 21)

    # BLOCK 2 VERLUST TABELLE 15
    B2_LOSS15_D1 = TableField("B2_LOSS15", 1)
    B2_LOSS15_D2 = TableField("B2_LOSS15", 2)
    B2_LOSS15_D3 = TableField("B2_LOSS15", 3)
    B2_LOSS15_D4 = TableField("B2_LOSS15", 4)
    B2_LOSS15_D5 = TableField("B2_LOSS15", 5)
    B2_LOSS15_D6 = TableField("B2_LOSS15", 6)
    B2_LOSS15_D7 = TableField("B2_LOSS15", 7)
    B2_LOSS15_D8 = TableField("B2_LOSS15", 8)
    B2_LOSS15_D9 = TableField("B2_LOSS15", 9)
    B2_LOSS15_D10 = TableField("B2_LOSS15", 10)
    B2_LOSS15_D11 = TableField("B2_LOSS15", 11)
    B2_LOSS15_D12 = TableField("B2_LOSS15", 12)
    B2_LOSS15_D13 = TableField("B2_LOSS15", 13)
    B2_LOSS15_D14 = TableField("B2_LOSS15", 14)
    B2_LOSS15_D15 = TableField("B2_LOSS15", 15)
    B2_LOSS15_D16 = TableField("B2_LOSS15", 16)
    B2_LOSS15_D17 = TableField("B2_LOSS15", 17)
    B2_LOSS15_D18 = TableField("B2_LOSS15", 18)
    B2_LOSS15_D19 = TableField("B2_LOSS15", 19)
    B2_LOSS15_D20 = TableField("B2_LOSS15", 20)
    B2_LOSS15_D21 = TableField("B2_LOSS15", 21)

    # BLOCK 2 VERLUST TABELLE 16
    B2_LOSS16_D1 = TableField("B2_LOSS16", 1)
    B2_LOSS16_D2 = TableField("B2_LOSS16", 2)
    B2_LOSS16_D3 = TableField("B2_LOSS16", 3)
    B2_LOSS16_D4 = TableField("B2_LOSS16", 4)
    B2_LOSS16_D5 = TableField("B2_LOSS16", 5)
    B2_LOSS16_D6 = TableField("B2_LOSS16", 6)
    B2_LOSS16_D7 = TableField("B2_LOSS16", 7)
    B2_LOSS16_D8 = TableField("B2_LOSS16", 8)
    B2_LOSS16_D9 = TableField("B2_LOSS16", 9)
    B2_LOSS16_D10 = TableField("B2_LOSS16", 10)
    B2_LOSS16_D11 = TableField("B2_LOSS16", 11)
    B2_LOSS16_D12 = TableField("B2_LOSS16", 12)
    B2_LOSS16_D13 = TableField("B2_LOSS16", 13)
    B2_LOSS16_D14 = TableField("B2_LOSS16", 14)
    B2_LOSS16_D15 = TableField("B2_LOSS16", 15)
    B2_LOSS16_D16 = TableField("B2_LOSS16", 16)
    B2_LOSS16_D17 = TableField("B2_LOSS16", 17)
    B2_LOSS16_D18 = TableField("B2_LOSS16", 18)
    B2_LOSS16_D19 = TableField("B2_LOSS16", 19)
    B2_LOSS16_D20 = TableField("B2_LOSS16", 20)
    B2_LOSS16_D21 = TableField("B2_LOSS16", 21)

    # BLOCK 2 VERLUST TABELLE 17
    B2_LOSS17_D1 = TableField("B2_LOSS17", 1)
    B2_LOSS17_D2 = TableField("B2_LOSS17", 2)
    B2_LOSS17_D3 = TableField("B2_LOSS17", 3)
    B2_LOSS17_D4 = TableField("B2_LOSS17", 4)
    B2_LOSS17_D5 = TableField("B2_LOSS17", 5)
    B2_LOSS17_D6 = TableField("B2_LOSS17", 6)
    B2_LOSS17_D7 = TableField("B2_LOSS17", 7)
    B2_LOSS17_D8 = TableField("B2_LOSS17", 8)
    B2_LOSS17_D9 = TableField("B2_LOSS17", 9)
    B2_LOSS17_D10 = TableField("B2_LOSS17", 10)
    B2_LOSS17_D11 = TableField("B2_LOSS17", 11)
    B2_LOSS17_D12 = TableField("B2_LOSS17", 12)
    B2_LOSS17_D13 = TableField("B2_LOSS17", 13)
    B2_LOSS17_D14 = TableField("B2_LOSS17", 14)
    B2_LOSS17_D15 = TableField("B2_LOSS17", 15)
    B2_LOSS17_D16 = TableField("B2_LOSS17", 16)
    B2_LOSS17_D17 = TableField("B2_LOSS17", 17)
    B2_LOSS17_D18 = TableField("B2_LOSS17", 18)
    B2_LOSS17_D19 = TableField("B2_LOSS17", 19)
    B2_LOSS17_D20 = TableField("B2_LOSS17", 20)
    B2_LOSS17_D21 = TableField("B2_LOSS17", 21)

    # BLOCK 2 VERLUST TABELLE 18
    B2_LOSS18_D1 = TableField("B2_LOSS18", 1)
    B2_LOSS18_D2 = TableField("B2_LOSS18", 2)
    B2_LOSS18_D3 = TableField("B2_LOSS18", 3)
    B2_LOSS18_D4 = TableField("B2_LOSS18", 4)
    B2_LOSS18_D5 = TableField("B2_LOSS18", 5)
    B2_LOSS18_D6 = TableField("B2_LOSS18", 6)
    B2_LOSS18_D7 = TableField("B2_LOSS18", 7)
    B2_LOSS18_D8 = TableField("B2_LOSS18", 8)
    B2_LOSS18_D9 = TableField("B2_LOSS18", 9)
    B2_LOSS18_D10 = TableField("B2_LOSS18", 10)
    B2_LOSS18_D11 = TableField("B2_LOSS18", 11)
    B2_LOSS18_D12 = TableField("B2_LOSS18", 12)
    B2_LOSS18_D13 = TableField("B2_LOSS18", 13)
    B2_LOSS18_D14 = TableField("B2_LOSS18", 14)
    B2_LOSS18_D15 = TableField("B2_LOSS18", 15)
    B2_LOSS18_D16 = TableField("B2_LOSS18", 16)
    B2_LOSS18_D17 = TableField("B2_LOSS18", 17)
    B2_LOSS18_D18 = TableField("B2_LOSS18", 18)
    B2_LOSS18_D19 = TableField("B2_LOSS18", 19)
    B2_LOSS18_D20 = TableField("B2_LOSS18", 20)
    B2_LOSS18_D21 = TableField("B2_LOSS18", 21)

    # BLOCK 2 VERLUST TABELLE 19
    B2_LOSS19_D1 = TableField("B2_LOSS19", 1)
    B2_LOSS19_D2 = TableField("B2_LOSS19", 2)
    B2_LOSS19_D3 = TableField("B2_LOSS19", 3)
    B2_LOSS19_D4 = TableField("B2_LOSS19", 4)
    B2_LOSS19_D5 = TableField("B2_LOSS19", 5)
    B2_LOSS19_D6 = TableField("B2_LOSS19", 6)
    B2_LOSS19_D7 = TableField("B2_LOSS19", 7)
    B2_LOSS19_D8 = TableField("B2_LOSS19", 8)
    B2_LOSS19_D9 = TableField("B2_LOSS19", 9)
    B2_LOSS19_D10 = TableField("B2_LOSS19", 10)
    B2_LOSS19_D11 = TableField("B2_LOSS19", 11)
    B2_LOSS19_D12 = TableField("B2_LOSS19", 12)
    B2_LOSS19_D13 = TableField("B2_LOSS19", 13)
    B2_LOSS19_D14 = TableField("B2_LOSS19", 14)
    B2_LOSS19_D15 = TableField("B2_LOSS19", 15)
    B2_LOSS19_D16 = TableField("B2_LOSS19", 16)
    B2_LOSS19_D17 = TableField("B2_LOSS19", 17)
    B2_LOSS19_D18 = TableField("B2_LOSS19", 18)
    B2_LOSS19_D19 = TableField("B2_LOSS19", 19)
    B2_LOSS19_D20 = TableField("B2_LOSS19", 20)
    B2_LOSS19_D21 = TableField("B2_LOSS19", 21)

    # BLOCK 2 VERLUST TABELLE 20
    B2_LOSS20_D1 = TableField("B2_LOSS20", 1)
    B2_LOSS20_D2 = TableField("B2_LOSS20", 2)
    B2_LOSS20_D3 = TableField("B2_LOSS20", 3)
    B2_LOSS20_D4 = TableField("B2_LOSS20", 4)
    B2_LOSS20_D5 = TableField("B2_LOSS20", 5)
    B2_LOSS20_D6 = TableField("B2_LOSS20", 6)
    B2_LOSS20_D7 = TableField("B2_LOSS20", 7)
    B2_LOSS20_D8 = TableField("B2_LOSS20", 8)
    B2_LOSS20_D9 = TableField("B2_LOSS20", 9)
    B2_LOSS20_D10 = TableField("B2_LOSS20", 10)
    B2_LOSS20_D11 = TableField("B2_LOSS20", 11)
    B2_LOSS20_D12 = TableField("B2_LOSS20", 12)
    B2_LOSS20_D13 = TableField("B2_LOSS20", 13)
    B2_LOSS20_D14 = TableField("B2_LOSS20", 14)
    B2_LOSS20_D15 = TableField("B2_LOSS20", 15)
    B2_LOSS20_D16 = TableField("B2_LOSS20", 16)
    B2_LOSS20_D17 = TableField("B2_LOSS20", 17)
    B2_LOSS20_D18 = TableField("B2_LOSS20", 18)
    B2_LOSS20_D19 = TableField("B2_LOSS20", 19)
    B2_LOSS20_D20 = TableField("B2_LOSS20", 20)
    B2_LOSS20_D21 = TableField("B2_LOSS20", 21)




