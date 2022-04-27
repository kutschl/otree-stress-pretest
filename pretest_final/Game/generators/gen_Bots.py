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

def codeBotsBlockIntro(block):
    return f"""
        yield pages.Block{block}Intro,
"""


def codeBotsBlock(block):
    code = ''
    for table in np.arange(1, 40+1, 1):
        code = code + codeBotsTable(block, table)
    return code


def codeBotsTable(block, table):
    return f"""
        yield pages.Block{block}Table{table}, dict(
            BLOCK{block}_TABLE{table}_LOTTERY=rd.randint(1,20), 
            BLOCK{block}_TABLE{table}_TYPE=rd.randint(0,1),
            BLOCK{block}_TABLE{table}_ORDER=rd.randint(0,1),
            BLOCK{block}_TABLE{table}_SP_OPTION=rd.randint(0,1),
            BLOCK{block}_TABLE{table}_SP_DECISION=rd.randint(1, 21)
        ),
"""

def codeBotsZwischenfragenIntro():
    return """
        yield pages.ZwischenteilIntro,
"""


def codeBotsZwischenfragen():
    order = [7, 4, 5, 9, 10, 12, 8, 15, 11, 13, 2, 16, 14, 1, 3, 6]
    code = ''

    for page in np.arange(0, len(order)):
        code_dict = f'ZWISCHENFRAGE{order[page]} = 1, '
        code = code + f"""
        yield pages.Zwischenteil{page+1}, dict({code_dict}),
"""
    return code


def codeBotsSetPayoff():
    return """
        yield pages.SetPayoff,
"""


# OUTPUT
code =  codeBotsBlockIntro(1) + codeBotsBlock(1) + codeBotsZwischenfragenIntro() + codeBotsZwischenfragen() + codeBotsBlockIntro(2) + codeBotsBlock(2) + codeBotsSetPayoff()
OtreeBotsGenerator.writeBotsFile(url, imports, code)

