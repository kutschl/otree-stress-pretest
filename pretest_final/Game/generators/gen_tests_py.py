import numpy as np
import random as rd

blocks = 2
decisions = 21
tables_per_block = 40
gain_tables_per_block = 20
loss_tables_per_block = 20


code = ''
for block in np.arange(1, blocks+1, 1):
    for gain_table in np.arange(1, gain_tables_per_block+1, 1):
        code_dict = ''
        for decision in np.arange(1, decisions+1, 1):
             code_dict = code_dict + f'B{block}_GAIN{gain_table}_D{decision} = {rd.randint(1,2)}, '
        code = code + f'yield pages.B{block}_GAIN{gain_table}, dict({code_dict})\n'
    for loss_table in np.arange(1, loss_tables_per_block+1, 1):
        code_dict = ''
        for decision in np.arange(1, decisions+1, 1):
            code_dict = code_dict + f'B{block}_LOSS{loss_table}_D{decision} = {rd.randint(1,2)}, '
        code = code + f'yield pages.B{block}_LOSS{loss_table}, dict({code_dict}),\n'

print(code)
