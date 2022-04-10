from generators import OtreeBotsGenerator
import numpy as np


# INITS
url = '../tests.py'
imports = """from . import pages
from ._builtin import Bot
import random as rd
"""
code = ''


# GENERATORS
def codeBotsBlock(block_number: int):
    # INITS
    decisions = 21
    gain_tables = 20
    loss_tables = 20

    # GENERATOR
    code = f'yield pages.Block{block_number}Intro, \n'
    for gain_table in np.arange(1, gain_tables+1):
        code_dict = ''
        for decision in np.arange(1, decisions+1):
            code_dict = code_dict + f'B{block_number}_GAIN{gain_table}_D{decision} = rd.randint(1,2), '
        code = code + f'yield pages.Block{block_number}GewinnTabelle{gain_table}, dict({code_dict})\n'
    for loss_table in np.arange(1, loss_tables+1, 1):
        code_dict = ''
        for decision in np.arange(1, decisions+1, 1):
            code_dict = code_dict + f'B{block_number}_LOSS{loss_table}_D{decision} = rd.randint(1,2), '
        code = code + f'yield pages.Block{block_number}VerlustTabelle{loss_table}, dict({code_dict}),\n'
    return code


def codeBotsZwischenfragen():
    # INITS
    order = [[7, 4, 5, 9], [10, 12, 8, 15], [11, 13, 2, 16], [14, 1, 3, 6]]
    pages = 4

    # GENERATOR
    code = 'yield pages.ZwischenfragenIntro, \n'
    for page in np.arange(1, pages+1):
        code_dict = ''
        for question in np.arange(0, len(order[page-1])):
            code_dict = code_dict + f'ZWISCHENFRAGE{order[page-1][question]} = 1, '
        code = code + f'yield pages.Zwischenfragen{page}, dict({code_dict}), \n'
    return code


def codeBotsSetPayoff():
    return 'yield pages.SetPayoff, \n'


# OUTPUT
code = codeBotsBlock(1) + codeBotsZwischenfragen() + codeBotsBlock(2) + codeBotsSetPayoff()
OtreeBotsGenerator.writeBotsFile(url, imports, code)

