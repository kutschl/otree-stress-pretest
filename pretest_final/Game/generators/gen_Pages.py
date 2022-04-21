from generators import OtreePagesGenerator
import numpy as np

# INITS
url = '../pages.py'
imports = """from ._builtin import Page, WaitPage"""
page_sequence = []
pages = ''


# GENERATORS
def codePagesBlockIntro(block_number: int):
    page_name = f'Block{block_number}Intro'
    page_sequence.append(page_name)
    return OtreePagesGenerator.getPageWithPass(page_name)


def codePagesBlock(block_number: int):
    # INITS
    decisions = 21
    gain_tables = 20
    loss_tables = 20

    # GENERATOR
    code = ''
    for gain_table in np.arange(1, gain_tables + 1, 1):
        page_name = f'Block{block_number}GewinnTabelle{gain_table}'
        page_sequence.append(page_name)
        form_model = 'player'
        form_fields = ''
        for decision in np.arange(1, decisions + 1, 1):
            form_fields = form_fields + f"'B{block_number}_GAIN{gain_table}_D{decision}', "
        code = code + OtreePagesGenerator.getPageWithFields(
            page_name,
            form_model,
            form_fields
        )
    for loss_table in np.arange(1, loss_tables + 1, 1):
        page_name = f'Block{block_number}VerlustTabelle{loss_table}'
        page_sequence.append(page_name)
        form_model = 'player'
        form_fields = ''
        for decision in np.arange(1, decisions + 1, 1):
            form_fields = form_fields + f"'B{block_number}_LOSS{loss_table}_D{decision}', "
        code = code + OtreePagesGenerator.getPageWithFields(
            page_name,
            form_model,
            form_fields
        )
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


