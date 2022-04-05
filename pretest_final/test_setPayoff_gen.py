from lotteries_loader import LotteryLoader as lot
import numpy as np
import random as rd

data_gain = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'GAIN'
)
data_loss = lot.loadLotteries(
    'C:/Users/Lukas/OneDrive/Arbeit (offen)/otree Stress Pretest/pretest_final/_static/data/lotteries.xls', 'LOSS'
)


gain_tables_per_block = len(data_gain[list(data_gain.keys())[0]])
loss_tables_per_block = len(data_loss[list(data_loss.keys())[0]])
tables_per_block = gain_tables_per_block + loss_tables_per_block
blocks = 2
tables = blocks * tables_per_block
decisions_per_table = 21


# CODE: models.py.Player.IntegerFields
def codeModelsPlayerIntegerFields():
    code = ''
    for block in np.arange(1, blocks + 1, 1):
        for gain_table in np.arange(1, gain_tables_per_block + 1, 1):
            code = code + f'# Block {block} Gain {gain_table}\n'
            for decision in np.arange(1, decisions_per_table + 1, 1):
                code = code + f'B{block}_GAIN{gain_table}_D{decision} = {rd.randint(1, 2)}\n'
            code = code + '\n'
        for loss_table in np.arange(1, loss_tables_per_block + 1, 1):
            code = code + f'# Block {block} Loss {loss_table}\n'
            for decision in np.arange(1, decisions_per_table + 1, 1):
                code = code + f'B{block}_LOSS{loss_table}_D{decision} = {rd.randint(1, 2)}\n'
            code = code + '\n'
    return print(code)
codeModelsPlayerIntegerFields()