from .import models
from ._builtin import Page, WaitPage
from .models import Constants


class Tabelle(Page):
    form_model = 'player'
    form_fields = ['D1_1', 'D1_2', 'D1_3', 'D1_4', 'D1_5', 'D1_6', 'D1_7', 'D1_8', 'D1_9', 'D1_10', 'D1_11', 'D1_12', 'D1_13', 'D1_14', 'D1_15', 'D1_16', 'D1_17', 'D1_18', 'D1_19', 'D1_20', 'D1_21']


page_sequence = [Tabelle]
