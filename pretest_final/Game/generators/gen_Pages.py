from generators import OtreePagesGenerator
import numpy as np

# INITS
url = '../pages.py'
imports = """from ._builtin import Page, WaitPage
import random as rd"""
page_sequence = []
pages = ''


# GENERATORS
def codePagesBlockIntro(block):
    page_name = f'Block{block}Intro'
    page_sequence.append(page_name)
    if block == 1:
        return f"""
class {page_name}(Page):
    def vars_for_template(self):
        self.player.participant.vars['block{block}'] = self.player.getBlock({block})
        
        self.player.participant.vars['payoff_random_block'] = rd.randint(1, 2)
        self.player.participant.vars['payoff_random_table'] = rd.randint(1, 40)
        self.player.participant.vars['payoff_random_decision'] = rd.randint(1, 21)

"""
    if block == 2:
        return f"""
class {page_name}(Page):
    def vars_for_template(self):
        self.player.participant.vars['block{block}'] = self.player.getBlock({block})
"""



def codePagesBlock(block):
    # INITS
    tables = 40

    # GENERATOR
    code = ''
    for table in np.arange(1, tables + 1, 1):
        page_name = f'Block{block}Table{table}'
        page_sequence.append(page_name)
        code = code + f"""
class {page_name}(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK{block}_TABLE{table}_LOTTERY',
        'BLOCK{block}_TABLE{table}_TYPE',
        'BLOCK{block}_TABLE{table}_ORDER',
        'BLOCK{block}_TABLE{table}_SP_OPTION',
        'BLOCK{block}_TABLE{table}_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER={block},
            TABLE_NUMBER={table},
            TYPE=self.player.participant.vars['block{block}'][{table-1}]['TYPE'],
            ORDER=self.player.participant.vars['block{block}'][{table-1}]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK{block}_TABLE{table}_LOTTERY = self.player.participant.vars['block{block}'][{table-1}]['NUMBER']
        self.player.BLOCK{block}_TABLE{table}_TYPE = self.player.participant.vars['block{block}'][{table-1}]['TYPE']
        self.player.BLOCK{block}_TABLE{table}_ORDER = self.player.participant.vars['block{block}'][{table-1}]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == {block}) and self.player.participant.vars['payoff_random_table'] == {table}: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK{block}_TABLE{table}_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK{block}_TABLE{table}_SP_DECISION


"""

    return code


def codePagesZwischenteil():
    # INITS
    order = [7, 4, 5, 9, 10, 12, 8, 15, 11, 13, 2, 16, 14, 1, 3, 6]

    # GENERATOR
    code = ''
    for question in np.arange(0, len(order), 1):
        page_name = f'Zwischenteil{question+1}'
        page_sequence.append(page_name)
        form_model = 'player'
        form_fields = [f'ZWISCHENFRAGE{order[question]}']
        code = code + OtreePagesGenerator.getPageWithFields(
            page_name,
            form_model,
            form_fields
        )
    return code


def codePagesZwischenteilIntro():
    page_name = 'ZwischenteilIntro'
    page_sequence.append(page_name)
    return OtreePagesGenerator.getPageWithPass(page_name)


def codePagesSetPayoff():
    page_name = 'SetPayoff'
    page_sequence.append(page_name)
    return f"""
class {page_name}(Page):
    def vars_for_template(self):
        self.player.setPayoff()    

"""


# OUTPUT
pages = codePagesBlockIntro(1) + codePagesBlock(1) + codePagesZwischenteilIntro() + codePagesZwischenteil() + codePagesBlockIntro(2) + codePagesBlock(2) + codePagesSetPayoff()
OtreePagesGenerator.writePagesFile(url, imports, pages, page_sequence)


