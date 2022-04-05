import numpy as np
import pandas as pd
import random as rd


def loadLotteries(url: str):
    f1 = pd.read_excel(url, sheet_name='gain')
    f2 = pd.read_excel(url, sheet_name='loss')
    d = {}

    if f1.columns.tolist() != f2.columns.tolist():
        return None
    else:
        cols = f1.columns.tolist()
        for col in cols:
            d[col] = []
            for f1row in np.arange(0, len(f1), 1):
                d[col].append(f1[col].loc[f1row])
            for f2row in np.arange(0, len(f2), 1):
                d[col].append(f2[col].loc[f2row])
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





