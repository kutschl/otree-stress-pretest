import numpy as np
import pandas as pd


def load(url: str, name: str):
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



