import numpy as np
import pandas as pd
import random as rd
import pdb
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)

doc = ""


def loadLotteries(url, sheet):
    f = pd.read_excel(url, sheet_name=f'{sheet}')
    d = {
        'TYPE': [],
        'NUMBER': []
    }
    cols = f.columns.tolist()
    for col in cols:
        d[col] = []
        for row in np.arange(0, len(f), 1):
            d[col].append(f[col].loc[row])
    if sheet == "GAIN":
        sheet = 0
    elif sheet == "LOSS":
        sheet = 1
    for i in np.arange(0, len(f), 1):
        d['TYPE'].append(sheet)
        d['NUMBER'].append(int(i+1))
    return d


gain_data = loadLotteries('_static/data/lotteries.xls', 'GAIN')
loss_data = loadLotteries('_static/data/lotteries.xls', 'LOSS')


def separateLotteries(d):
    d1 = dict(d)
    d2 = dict(d)
    d1['ORDER'] = []
    d2['ORDER'] = []
    for _ in np.arange(0, len(d[list(d.keys())[0]]), 1):
        randomizer = rd.choice([True, False])
        if randomizer is True:
            d1['ORDER'].append(1)
            d2['ORDER'].append(0)
        if randomizer is False:
            d1['ORDER'].append(0)
            d2['ORDER'].append(1)
    return [d1, d2]


gain_data = separateLotteries(gain_data)
loss_data = separateLotteries(loss_data)


def TableB1_Numbering():
    return np.arange(1, 21 + 1).tolist()


def TableB2_OptionA(data, block, table):
    # Gain Table
    if data[block]['TYPE'][table] == 0:
        return {
            'p1': str("{0:.0%}".format(data[block]['p'][table])),
            'p2': str("{0:.0%}".format(1-data[block]['p'][table])),
            'x1': str("{:.2f}".format(data[block]['x1'][table])),
            'x2': str("{:.2f}".format(data[block]['x2'][table]))
        }
    # Loss Table
    elif data[block]['TYPE'][table] == 1:
        return {
            'p1': str("{0:.0%}".format(data[block]['p'][table])),
            'p2': str("{0:.0%}".format(1-data[block]['p'][table])),
            'x1': str("{:.2f}".format((-1)*data[block]['x1'][table])),
            'x2': str("{:.2f}".format((-1)*data[block]['x2'][table]))
        }


def TableB4_OptionB(data, block, table):
    li = []
    # Gain Table
    if data[block]['TYPE'][table] == 0:
        b_start = data[block]['x1'][table]
        b_step = (-1)*(data[block]['x1'][table] - data[block]['x2'][table])/20
        b_stop = data[block]['x2'][table] + b_step
        # Descending Order
        for i in np.arange(b_start, b_stop, b_step):
            li.append(str("{:.2f}".format(i)))
        # Ascending Order
        if data[block]['ORDER'][table] == 0:
            li.reverse()
        return li

    # Loss Table
    elif data[block]['TYPE'][table] == 1:
        b_start = data[block]['x1'][table]
        b_step = (-1)*(data[block]['x1'][table] - data[block]['x2'][table])/20
        b_stop = data[block]['x2'][table] + b_step
        # Ascending Order
        for i in np.arange(b_start, b_stop, b_step):
            li.append(str("{:.2f}".format(i*(-1))))
        # Descending Order
        if data[block]['ORDER'][table] == 1:
            li.reverse()
        return li


def Payoff_OptionA(data, block, table):
    return {
        'p1': data[block]['p'][table],
        'p2': 1-data[block]['p'][table],
        'x1': data[block]['x1'][table],
        'x2': data[block]['x2'][table]
    }


def Payoff_OptionB(data, block, table):
    li = []
    # Gain Table
    if data[block]['TYPE'][table] == 0:
        b_start = data[block]['x1'][table]
        b_step = (-1)*(data[block]['x1'][table] - data[block]['x2'][table])/20
        b_stop = data[block]['x2'][table] + b_step
        # Descending Order
        for i in np.arange(b_start, b_stop, b_step):
            li.append(i)
        # Ascending Order
        if data[block]['ORDER'][table] == 0:
            li.reverse()
        return li

    # Loss Table
    elif data[block]['TYPE'][table] == 1:
        b_start = data[block]['x1'][table]
        b_step = (-1)*(data[block]['x1'][table] - data[block]['x2'][table])/20
        b_stop = data[block]['x2'][table] + b_step
        # Ascending Order
        for i in np.arange(b_start, b_stop, b_step):
            li.append(i)
        # Descending Order
        if data[block]['ORDER'][table] == 1:
            li.reverse()
        return li


def getTable(block, table, typ):
    data = None
    if typ == 0:
        data = gain_data
    elif typ == 1:
        data = loss_data
    return {
        'NUMBER': data[block-1]['NUMBER'][table-1],
        'NUMBERING': TableB1_Numbering(),
        'OPTION_A': TableB2_OptionA(data, block-1, table-1),
        'OPTION_B': TableB4_OptionB(data, block-1, table-1),
        'PAYOFF_A': Payoff_OptionA(data, block-1, table-1),
        'PAYOFF_B': Payoff_OptionB(data, block-1, table-1),
        'TYPE': data[block-1]['TYPE'][table-1],
        'ORDER': data[block-1]['ORDER'][table-1],
        'Choice': [
            [0, 'A'],
            [1, 'B']
        ],
        'Widget': widgets.RadioSelectHorizontal
    }


def getBlock(block):
    b = []
    for i in np.arange(1, 20+1, 1):
        b.append(getTable(block, i, 0))
        b.append(getTable(block, i, 1))
    rd.shuffle(b)
    return b


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


def getZwischenfragen(question):
    return {
        'label': zwischenfragen_data[question]['label'],
        'choices': zwischenfragen_data[question]['choices'],
        'image': zwischenfragen_data[question]['img'],
        'answer': zwischenfragen_data[question]['answer']
    }


def ZwischenfragenField(question):
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

    # BLOCKS FUNCTION
    @staticmethod
    def getBlock(number):
        return getBlock(number)

    # PAYOFF FUNKTION
    def setPayoff(self):
        # Random Decision
        RANDOM_BLOCK = self.participant.vars['payoff_random_block']
        RANDOM_TABLE = self.participant.vars['payoff_random_table']
        RANDOM_DECISION = self.participant.vars['payoff_random_decision']

        # Real Player Decision
        PLAYER_SP_OPTION = self.participant.vars['payoff_player_sp_option']
        PLAYER_SP_DECISION = self.participant.vars['payoff_player_sp_decision']
        PLAYER_OPTION = None

        # Table Properties
        TABLE_TYPE = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['TYPE']
        TABLE_ORDER = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['ORDER']
        LOTTERY = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['NUMBER']

        # 1. Case: Top Right to Bottom Left
        if (TABLE_TYPE == 1 & TABLE_ORDER == 0) | (TABLE_TYPE == 0 & TABLE_ORDER == 1):
            if RANDOM_DECISION < PLAYER_SP_DECISION:
                PLAYER_OPTION = 1
            elif RANDOM_DECISION == PLAYER_SP_DECISION:
                PLAYER_OPTION = PLAYER_SP_OPTION
            elif RANDOM_DECISION > PLAYER_SP_DECISION:
                PLAYER_OPTION = 0

        # 2. Case: Top Left to Bottom Right
        if (TABLE_TYPE == 0 & TABLE_ORDER == 0) | (TABLE_TYPE == 1 & TABLE_ORDER == 1):
            if RANDOM_DECISION < PLAYER_SP_DECISION:
                PLAYER_OPTION = 0
            elif RANDOM_DECISION == PLAYER_SP_DECISION:
                PLAYER_OPTION = PLAYER_SP_OPTION
            elif RANDOM_DECISION > PLAYER_SP_DECISION:
                PLAYER_OPTION = 1

        # Payoff Calculation
        if PLAYER_OPTION == 0:
            p1 = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['PAYOFF_A']['p1']
            p2 = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['PAYOFF_A']['p2']
            x1 = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['PAYOFF_A']['x1']
            x2 = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['PAYOFF_A']['x2']

            urn = []
            for _ in np.arange(0, p1 * 100, 1):
                urn.append(x1)
            for _ in np.arange(0, p2*100, 1):
                urn.append(x2)
            rd.shuffle(urn)

            self.payoff = c(Constants.endowment_in_euro + (urn[rd.randint(0, 99)] / Constants.multiplier))

        elif PLAYER_OPTION == 1:
            value = self.participant.vars[f'block{RANDOM_BLOCK}'][RANDOM_TABLE-1]['PAYOFF_B'][RANDOM_DECISION-1]
            self.payoff = c(Constants.endowment_in_euro + (value / Constants.multiplier))

        # Payoff Information
        self.participant.vars['payoff_table_type'] = TABLE_TYPE
        self.participant.vars['payoff_table_order'] = TABLE_ORDER
        self.participant.vars['payoff_lottery'] = LOTTERY
        self.participant.vars['payoff_player_option'] = PLAYER_OPTION
        self.participant.vars['payoff'] = self.payoff

    # BLOCK 1 TABLE 1
    BLOCK1_TABLE1_LOTTERY = models.IntegerField()
    BLOCK1_TABLE1_TYPE = models.IntegerField()
    BLOCK1_TABLE1_ORDER = models.IntegerField()
    BLOCK1_TABLE1_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE1_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 2
    BLOCK1_TABLE2_LOTTERY = models.IntegerField()
    BLOCK1_TABLE2_TYPE = models.IntegerField()
    BLOCK1_TABLE2_ORDER = models.IntegerField()
    BLOCK1_TABLE2_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE2_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 3
    BLOCK1_TABLE3_LOTTERY = models.IntegerField()
    BLOCK1_TABLE3_TYPE = models.IntegerField()
    BLOCK1_TABLE3_ORDER = models.IntegerField()
    BLOCK1_TABLE3_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE3_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 4
    BLOCK1_TABLE4_LOTTERY = models.IntegerField()
    BLOCK1_TABLE4_TYPE = models.IntegerField()
    BLOCK1_TABLE4_ORDER = models.IntegerField()
    BLOCK1_TABLE4_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE4_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 5
    BLOCK1_TABLE5_LOTTERY = models.IntegerField()
    BLOCK1_TABLE5_TYPE = models.IntegerField()
    BLOCK1_TABLE5_ORDER = models.IntegerField()
    BLOCK1_TABLE5_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE5_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 6
    BLOCK1_TABLE6_LOTTERY = models.IntegerField()
    BLOCK1_TABLE6_TYPE = models.IntegerField()
    BLOCK1_TABLE6_ORDER = models.IntegerField()
    BLOCK1_TABLE6_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE6_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 7
    BLOCK1_TABLE7_LOTTERY = models.IntegerField()
    BLOCK1_TABLE7_TYPE = models.IntegerField()
    BLOCK1_TABLE7_ORDER = models.IntegerField()
    BLOCK1_TABLE7_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE7_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 8
    BLOCK1_TABLE8_LOTTERY = models.IntegerField()
    BLOCK1_TABLE8_TYPE = models.IntegerField()
    BLOCK1_TABLE8_ORDER = models.IntegerField()
    BLOCK1_TABLE8_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE8_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 9
    BLOCK1_TABLE9_LOTTERY = models.IntegerField()
    BLOCK1_TABLE9_TYPE = models.IntegerField()
    BLOCK1_TABLE9_ORDER = models.IntegerField()
    BLOCK1_TABLE9_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE9_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 10
    BLOCK1_TABLE10_LOTTERY = models.IntegerField()
    BLOCK1_TABLE10_TYPE = models.IntegerField()
    BLOCK1_TABLE10_ORDER = models.IntegerField()
    BLOCK1_TABLE10_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE10_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 11
    BLOCK1_TABLE11_LOTTERY = models.IntegerField()
    BLOCK1_TABLE11_TYPE = models.IntegerField()
    BLOCK1_TABLE11_ORDER = models.IntegerField()
    BLOCK1_TABLE11_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE11_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 12
    BLOCK1_TABLE12_LOTTERY = models.IntegerField()
    BLOCK1_TABLE12_TYPE = models.IntegerField()
    BLOCK1_TABLE12_ORDER = models.IntegerField()
    BLOCK1_TABLE12_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE12_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 13
    BLOCK1_TABLE13_LOTTERY = models.IntegerField()
    BLOCK1_TABLE13_TYPE = models.IntegerField()
    BLOCK1_TABLE13_ORDER = models.IntegerField()
    BLOCK1_TABLE13_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE13_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 14
    BLOCK1_TABLE14_LOTTERY = models.IntegerField()
    BLOCK1_TABLE14_TYPE = models.IntegerField()
    BLOCK1_TABLE14_ORDER = models.IntegerField()
    BLOCK1_TABLE14_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE14_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 15
    BLOCK1_TABLE15_LOTTERY = models.IntegerField()
    BLOCK1_TABLE15_TYPE = models.IntegerField()
    BLOCK1_TABLE15_ORDER = models.IntegerField()
    BLOCK1_TABLE15_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE15_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 16
    BLOCK1_TABLE16_LOTTERY = models.IntegerField()
    BLOCK1_TABLE16_TYPE = models.IntegerField()
    BLOCK1_TABLE16_ORDER = models.IntegerField()
    BLOCK1_TABLE16_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE16_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 17
    BLOCK1_TABLE17_LOTTERY = models.IntegerField()
    BLOCK1_TABLE17_TYPE = models.IntegerField()
    BLOCK1_TABLE17_ORDER = models.IntegerField()
    BLOCK1_TABLE17_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE17_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 18
    BLOCK1_TABLE18_LOTTERY = models.IntegerField()
    BLOCK1_TABLE18_TYPE = models.IntegerField()
    BLOCK1_TABLE18_ORDER = models.IntegerField()
    BLOCK1_TABLE18_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE18_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 19
    BLOCK1_TABLE19_LOTTERY = models.IntegerField()
    BLOCK1_TABLE19_TYPE = models.IntegerField()
    BLOCK1_TABLE19_ORDER = models.IntegerField()
    BLOCK1_TABLE19_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE19_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 20
    BLOCK1_TABLE20_LOTTERY = models.IntegerField()
    BLOCK1_TABLE20_TYPE = models.IntegerField()
    BLOCK1_TABLE20_ORDER = models.IntegerField()
    BLOCK1_TABLE20_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE20_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 21
    BLOCK1_TABLE21_LOTTERY = models.IntegerField()
    BLOCK1_TABLE21_TYPE = models.IntegerField()
    BLOCK1_TABLE21_ORDER = models.IntegerField()
    BLOCK1_TABLE21_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE21_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 22
    BLOCK1_TABLE22_LOTTERY = models.IntegerField()
    BLOCK1_TABLE22_TYPE = models.IntegerField()
    BLOCK1_TABLE22_ORDER = models.IntegerField()
    BLOCK1_TABLE22_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE22_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 23
    BLOCK1_TABLE23_LOTTERY = models.IntegerField()
    BLOCK1_TABLE23_TYPE = models.IntegerField()
    BLOCK1_TABLE23_ORDER = models.IntegerField()
    BLOCK1_TABLE23_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE23_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 24
    BLOCK1_TABLE24_LOTTERY = models.IntegerField()
    BLOCK1_TABLE24_TYPE = models.IntegerField()
    BLOCK1_TABLE24_ORDER = models.IntegerField()
    BLOCK1_TABLE24_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE24_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 25
    BLOCK1_TABLE25_LOTTERY = models.IntegerField()
    BLOCK1_TABLE25_TYPE = models.IntegerField()
    BLOCK1_TABLE25_ORDER = models.IntegerField()
    BLOCK1_TABLE25_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE25_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 26
    BLOCK1_TABLE26_LOTTERY = models.IntegerField()
    BLOCK1_TABLE26_TYPE = models.IntegerField()
    BLOCK1_TABLE26_ORDER = models.IntegerField()
    BLOCK1_TABLE26_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE26_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 27
    BLOCK1_TABLE27_LOTTERY = models.IntegerField()
    BLOCK1_TABLE27_TYPE = models.IntegerField()
    BLOCK1_TABLE27_ORDER = models.IntegerField()
    BLOCK1_TABLE27_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE27_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 28
    BLOCK1_TABLE28_LOTTERY = models.IntegerField()
    BLOCK1_TABLE28_TYPE = models.IntegerField()
    BLOCK1_TABLE28_ORDER = models.IntegerField()
    BLOCK1_TABLE28_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE28_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 29
    BLOCK1_TABLE29_LOTTERY = models.IntegerField()
    BLOCK1_TABLE29_TYPE = models.IntegerField()
    BLOCK1_TABLE29_ORDER = models.IntegerField()
    BLOCK1_TABLE29_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE29_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 30
    BLOCK1_TABLE30_LOTTERY = models.IntegerField()
    BLOCK1_TABLE30_TYPE = models.IntegerField()
    BLOCK1_TABLE30_ORDER = models.IntegerField()
    BLOCK1_TABLE30_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE30_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 31
    BLOCK1_TABLE31_LOTTERY = models.IntegerField()
    BLOCK1_TABLE31_TYPE = models.IntegerField()
    BLOCK1_TABLE31_ORDER = models.IntegerField()
    BLOCK1_TABLE31_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE31_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 32
    BLOCK1_TABLE32_LOTTERY = models.IntegerField()
    BLOCK1_TABLE32_TYPE = models.IntegerField()
    BLOCK1_TABLE32_ORDER = models.IntegerField()
    BLOCK1_TABLE32_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE32_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 33
    BLOCK1_TABLE33_LOTTERY = models.IntegerField()
    BLOCK1_TABLE33_TYPE = models.IntegerField()
    BLOCK1_TABLE33_ORDER = models.IntegerField()
    BLOCK1_TABLE33_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE33_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 34
    BLOCK1_TABLE34_LOTTERY = models.IntegerField()
    BLOCK1_TABLE34_TYPE = models.IntegerField()
    BLOCK1_TABLE34_ORDER = models.IntegerField()
    BLOCK1_TABLE34_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE34_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 35
    BLOCK1_TABLE35_LOTTERY = models.IntegerField()
    BLOCK1_TABLE35_TYPE = models.IntegerField()
    BLOCK1_TABLE35_ORDER = models.IntegerField()
    BLOCK1_TABLE35_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE35_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 36
    BLOCK1_TABLE36_LOTTERY = models.IntegerField()
    BLOCK1_TABLE36_TYPE = models.IntegerField()
    BLOCK1_TABLE36_ORDER = models.IntegerField()
    BLOCK1_TABLE36_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE36_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 37
    BLOCK1_TABLE37_LOTTERY = models.IntegerField()
    BLOCK1_TABLE37_TYPE = models.IntegerField()
    BLOCK1_TABLE37_ORDER = models.IntegerField()
    BLOCK1_TABLE37_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE37_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 38
    BLOCK1_TABLE38_LOTTERY = models.IntegerField()
    BLOCK1_TABLE38_TYPE = models.IntegerField()
    BLOCK1_TABLE38_ORDER = models.IntegerField()
    BLOCK1_TABLE38_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE38_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 39
    BLOCK1_TABLE39_LOTTERY = models.IntegerField()
    BLOCK1_TABLE39_TYPE = models.IntegerField()
    BLOCK1_TABLE39_ORDER = models.IntegerField()
    BLOCK1_TABLE39_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE39_SP_DECISION = models.IntegerField()

    # BLOCK 1 TABLE 40
    BLOCK1_TABLE40_LOTTERY = models.IntegerField()
    BLOCK1_TABLE40_TYPE = models.IntegerField()
    BLOCK1_TABLE40_ORDER = models.IntegerField()
    BLOCK1_TABLE40_SP_OPTION = models.IntegerField()
    BLOCK1_TABLE40_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 1
    BLOCK2_TABLE1_LOTTERY = models.IntegerField()
    BLOCK2_TABLE1_TYPE = models.IntegerField()
    BLOCK2_TABLE1_ORDER = models.IntegerField()
    BLOCK2_TABLE1_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE1_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 2
    BLOCK2_TABLE2_LOTTERY = models.IntegerField()
    BLOCK2_TABLE2_TYPE = models.IntegerField()
    BLOCK2_TABLE2_ORDER = models.IntegerField()
    BLOCK2_TABLE2_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE2_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 3
    BLOCK2_TABLE3_LOTTERY = models.IntegerField()
    BLOCK2_TABLE3_TYPE = models.IntegerField()
    BLOCK2_TABLE3_ORDER = models.IntegerField()
    BLOCK2_TABLE3_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE3_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 4
    BLOCK2_TABLE4_LOTTERY = models.IntegerField()
    BLOCK2_TABLE4_TYPE = models.IntegerField()
    BLOCK2_TABLE4_ORDER = models.IntegerField()
    BLOCK2_TABLE4_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE4_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 5
    BLOCK2_TABLE5_LOTTERY = models.IntegerField()
    BLOCK2_TABLE5_TYPE = models.IntegerField()
    BLOCK2_TABLE5_ORDER = models.IntegerField()
    BLOCK2_TABLE5_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE5_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 6
    BLOCK2_TABLE6_LOTTERY = models.IntegerField()
    BLOCK2_TABLE6_TYPE = models.IntegerField()
    BLOCK2_TABLE6_ORDER = models.IntegerField()
    BLOCK2_TABLE6_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE6_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 7
    BLOCK2_TABLE7_LOTTERY = models.IntegerField()
    BLOCK2_TABLE7_TYPE = models.IntegerField()
    BLOCK2_TABLE7_ORDER = models.IntegerField()
    BLOCK2_TABLE7_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE7_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 8
    BLOCK2_TABLE8_LOTTERY = models.IntegerField()
    BLOCK2_TABLE8_TYPE = models.IntegerField()
    BLOCK2_TABLE8_ORDER = models.IntegerField()
    BLOCK2_TABLE8_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE8_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 9
    BLOCK2_TABLE9_LOTTERY = models.IntegerField()
    BLOCK2_TABLE9_TYPE = models.IntegerField()
    BLOCK2_TABLE9_ORDER = models.IntegerField()
    BLOCK2_TABLE9_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE9_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 10
    BLOCK2_TABLE10_LOTTERY = models.IntegerField()
    BLOCK2_TABLE10_TYPE = models.IntegerField()
    BLOCK2_TABLE10_ORDER = models.IntegerField()
    BLOCK2_TABLE10_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE10_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 11
    BLOCK2_TABLE11_LOTTERY = models.IntegerField()
    BLOCK2_TABLE11_TYPE = models.IntegerField()
    BLOCK2_TABLE11_ORDER = models.IntegerField()
    BLOCK2_TABLE11_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE11_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 12
    BLOCK2_TABLE12_LOTTERY = models.IntegerField()
    BLOCK2_TABLE12_TYPE = models.IntegerField()
    BLOCK2_TABLE12_ORDER = models.IntegerField()
    BLOCK2_TABLE12_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE12_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 13
    BLOCK2_TABLE13_LOTTERY = models.IntegerField()
    BLOCK2_TABLE13_TYPE = models.IntegerField()
    BLOCK2_TABLE13_ORDER = models.IntegerField()
    BLOCK2_TABLE13_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE13_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 14
    BLOCK2_TABLE14_LOTTERY = models.IntegerField()
    BLOCK2_TABLE14_TYPE = models.IntegerField()
    BLOCK2_TABLE14_ORDER = models.IntegerField()
    BLOCK2_TABLE14_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE14_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 15
    BLOCK2_TABLE15_LOTTERY = models.IntegerField()
    BLOCK2_TABLE15_TYPE = models.IntegerField()
    BLOCK2_TABLE15_ORDER = models.IntegerField()
    BLOCK2_TABLE15_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE15_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 16
    BLOCK2_TABLE16_LOTTERY = models.IntegerField()
    BLOCK2_TABLE16_TYPE = models.IntegerField()
    BLOCK2_TABLE16_ORDER = models.IntegerField()
    BLOCK2_TABLE16_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE16_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 17
    BLOCK2_TABLE17_LOTTERY = models.IntegerField()
    BLOCK2_TABLE17_TYPE = models.IntegerField()
    BLOCK2_TABLE17_ORDER = models.IntegerField()
    BLOCK2_TABLE17_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE17_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 18
    BLOCK2_TABLE18_LOTTERY = models.IntegerField()
    BLOCK2_TABLE18_TYPE = models.IntegerField()
    BLOCK2_TABLE18_ORDER = models.IntegerField()
    BLOCK2_TABLE18_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE18_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 19
    BLOCK2_TABLE19_LOTTERY = models.IntegerField()
    BLOCK2_TABLE19_TYPE = models.IntegerField()
    BLOCK2_TABLE19_ORDER = models.IntegerField()
    BLOCK2_TABLE19_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE19_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 20
    BLOCK2_TABLE20_LOTTERY = models.IntegerField()
    BLOCK2_TABLE20_TYPE = models.IntegerField()
    BLOCK2_TABLE20_ORDER = models.IntegerField()
    BLOCK2_TABLE20_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE20_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 21
    BLOCK2_TABLE21_LOTTERY = models.IntegerField()
    BLOCK2_TABLE21_TYPE = models.IntegerField()
    BLOCK2_TABLE21_ORDER = models.IntegerField()
    BLOCK2_TABLE21_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE21_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 22
    BLOCK2_TABLE22_LOTTERY = models.IntegerField()
    BLOCK2_TABLE22_TYPE = models.IntegerField()
    BLOCK2_TABLE22_ORDER = models.IntegerField()
    BLOCK2_TABLE22_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE22_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 23
    BLOCK2_TABLE23_LOTTERY = models.IntegerField()
    BLOCK2_TABLE23_TYPE = models.IntegerField()
    BLOCK2_TABLE23_ORDER = models.IntegerField()
    BLOCK2_TABLE23_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE23_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 24
    BLOCK2_TABLE24_LOTTERY = models.IntegerField()
    BLOCK2_TABLE24_TYPE = models.IntegerField()
    BLOCK2_TABLE24_ORDER = models.IntegerField()
    BLOCK2_TABLE24_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE24_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 25
    BLOCK2_TABLE25_LOTTERY = models.IntegerField()
    BLOCK2_TABLE25_TYPE = models.IntegerField()
    BLOCK2_TABLE25_ORDER = models.IntegerField()
    BLOCK2_TABLE25_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE25_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 26
    BLOCK2_TABLE26_LOTTERY = models.IntegerField()
    BLOCK2_TABLE26_TYPE = models.IntegerField()
    BLOCK2_TABLE26_ORDER = models.IntegerField()
    BLOCK2_TABLE26_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE26_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 27
    BLOCK2_TABLE27_LOTTERY = models.IntegerField()
    BLOCK2_TABLE27_TYPE = models.IntegerField()
    BLOCK2_TABLE27_ORDER = models.IntegerField()
    BLOCK2_TABLE27_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE27_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 28
    BLOCK2_TABLE28_LOTTERY = models.IntegerField()
    BLOCK2_TABLE28_TYPE = models.IntegerField()
    BLOCK2_TABLE28_ORDER = models.IntegerField()
    BLOCK2_TABLE28_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE28_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 29
    BLOCK2_TABLE29_LOTTERY = models.IntegerField()
    BLOCK2_TABLE29_TYPE = models.IntegerField()
    BLOCK2_TABLE29_ORDER = models.IntegerField()
    BLOCK2_TABLE29_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE29_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 30
    BLOCK2_TABLE30_LOTTERY = models.IntegerField()
    BLOCK2_TABLE30_TYPE = models.IntegerField()
    BLOCK2_TABLE30_ORDER = models.IntegerField()
    BLOCK2_TABLE30_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE30_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 31
    BLOCK2_TABLE31_LOTTERY = models.IntegerField()
    BLOCK2_TABLE31_TYPE = models.IntegerField()
    BLOCK2_TABLE31_ORDER = models.IntegerField()
    BLOCK2_TABLE31_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE31_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 32
    BLOCK2_TABLE32_LOTTERY = models.IntegerField()
    BLOCK2_TABLE32_TYPE = models.IntegerField()
    BLOCK2_TABLE32_ORDER = models.IntegerField()
    BLOCK2_TABLE32_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE32_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 33
    BLOCK2_TABLE33_LOTTERY = models.IntegerField()
    BLOCK2_TABLE33_TYPE = models.IntegerField()
    BLOCK2_TABLE33_ORDER = models.IntegerField()
    BLOCK2_TABLE33_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE33_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 34
    BLOCK2_TABLE34_LOTTERY = models.IntegerField()
    BLOCK2_TABLE34_TYPE = models.IntegerField()
    BLOCK2_TABLE34_ORDER = models.IntegerField()
    BLOCK2_TABLE34_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE34_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 35
    BLOCK2_TABLE35_LOTTERY = models.IntegerField()
    BLOCK2_TABLE35_TYPE = models.IntegerField()
    BLOCK2_TABLE35_ORDER = models.IntegerField()
    BLOCK2_TABLE35_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE35_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 36
    BLOCK2_TABLE36_LOTTERY = models.IntegerField()
    BLOCK2_TABLE36_TYPE = models.IntegerField()
    BLOCK2_TABLE36_ORDER = models.IntegerField()
    BLOCK2_TABLE36_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE36_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 37
    BLOCK2_TABLE37_LOTTERY = models.IntegerField()
    BLOCK2_TABLE37_TYPE = models.IntegerField()
    BLOCK2_TABLE37_ORDER = models.IntegerField()
    BLOCK2_TABLE37_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE37_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 38
    BLOCK2_TABLE38_LOTTERY = models.IntegerField()
    BLOCK2_TABLE38_TYPE = models.IntegerField()
    BLOCK2_TABLE38_ORDER = models.IntegerField()
    BLOCK2_TABLE38_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE38_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 39
    BLOCK2_TABLE39_LOTTERY = models.IntegerField()
    BLOCK2_TABLE39_TYPE = models.IntegerField()
    BLOCK2_TABLE39_ORDER = models.IntegerField()
    BLOCK2_TABLE39_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE39_SP_DECISION = models.IntegerField()

    # BLOCK 2 TABLE 40
    BLOCK2_TABLE40_LOTTERY = models.IntegerField()
    BLOCK2_TABLE40_TYPE = models.IntegerField()
    BLOCK2_TABLE40_ORDER = models.IntegerField()
    BLOCK2_TABLE40_SP_OPTION = models.IntegerField()
    BLOCK2_TABLE40_SP_DECISION = models.IntegerField()

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






