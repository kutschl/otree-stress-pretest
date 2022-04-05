import numpy as np
import pandas as pd
import random as rd


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





