import pandas as pd
import random as rd
import numpy as np


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
        d['NUMBER'].append(i+1)
    return d


gain_data = loadLotteries('../_static/data/lotteries.xls', 'GAIN')
loss_data = loadLotteries('../_static/data/lotteries.xls', 'LOSS')


print(gain_data)
print(loss_data)


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


print('block1', '\n', gain_data[0], '\n', 'block2', gain_data[1], '\n','\n',)
print('block1', '\n', loss_data[0], '\n', 'block2', loss_data[1], '\n','\n',)


def TableB1_Numbering():
    return np.arange(1, 21 + 1).tolist()


print(TableB1_Numbering())


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
        'TYPE': data[block-1]['TYPE'][table-1],
        'ORDER': data[block-1]['ORDER'][table-1],
        'Choice': [
             [0, 'A'],
             [1, 'B']
        ],
        # 'Widget': widgets.RadioSelectHorizontal
    }


def getBlock(block):
    b = []
    for i in np.arange(1, 20+1, 1):
        b.append(getTable(block, i, 0))
        b.append(getTable(block, i, 1))
    rd.shuffle(b)
    return b


block1 = getBlock(1)
block2 = getBlock(2)

print(block1, block2)



