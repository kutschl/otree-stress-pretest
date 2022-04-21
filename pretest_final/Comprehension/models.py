from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency,
    currency_range
)
import re
import math
import numpy as np
from decimal import Decimal

doc = ''


def getComprehensionQuestionSolution(question_number: int):
    return [2, 1, 2, 3][question_number-1]


def getComprehensionQuestionLabel():
    return "Nun wird die markierte Reihe zufällig als auszahlungsrelevante Reihe bestimmt. Was erhalten Sie?"


def getComprehensionQuestionWidget():
    return widgets.RadioSelect


def getComprehensionQuestionChoices(question_number: int):
    d = {
        1: ['3.50', ['50%', '10', '50%', '0'], '5', ['50%', '10', '50%', '5']],
        2: ['5', ['50%', '10', '50%', '0'], '6', ['50%', '3.50', '50%', '6.50']],
        3: ['20', ['25%', '20', '75%', '50'], '35', ['25%', '20', '75%', '35']],
        4: ['20', ['25%', '20', '75%', '50'], '35', ['25%', '20', '75%', '0']],
    }
    if question_number == 1 or question_number == 2:
        return [
            [1, f'Sie erhalten mit Sicherheit {d[question_number][0]} Punkte.'],
            [2, f'Mit Wahrscheinlichkeit {d[question_number][1][0]} erhalten Sie {d[question_number][1][1]} Punkte und mit Wahrscheinlichkeit {d[question_number][1][2]} erhalten Sie {d[question_number][1][3]} Punkte.'],
            [3, f'Sie erhalten mit Sicherheit {d[question_number][2]} Punkte.'],
            [4, f'Mit Wahrscheinlichkeit {d[question_number][3][0]} erhalten Sie {d[question_number][3][1]} Punkte und mit Wahrscheinlichkeit {d[question_number][3][2]} erhalten Sie {d[question_number][3][3]} Punkte.'],
        ]
    if question_number == 3 or question_number == 4:
        return [
            [1, f'Sie verlieren mit Sicherheit {d[question_number][0]} Punkte.'],
            [2, f'Mit Wahrscheinlichkeit {d[question_number][1][0]} verlieren Sie {d[question_number][1][1]} Punkte und mit Wahrscheinlichkeit {d[question_number][1][2]} verlieren Sie {d[question_number][1][3]} Punkte.'],
            [3, f'Sie verlieren mit Sicherheit {d[question_number][2]} Punkte.'],
            [4, f'Mit Wahrscheinlichkeit {d[question_number][3][0]} verlieren Sie {d[question_number][3][1]} Punkte und mit Wahrscheinlichkeit {d[question_number][3][2]} verlieren Sie {d[question_number][3][3]} Punkte.'],
        ]


class Constants(BaseConstants):
    name_in_url = 'Comprehension'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def COMPREHENSION_Q1_error_message(self, values):
        if values != getComprehensionQuestionSolution(1):
            self.COMPREHENSION_Q1_ATTEMPS = self.COMPREHENSION_Q1_ATTEMPS + 1
            return 'Bitte beantworten Sie die Frage erneut.'

    def COMPREHENSION_Q2_error_message(self, values):
        if values != getComprehensionQuestionSolution(2):
            self.COMPREHENSION_Q2_ATTEMPS = self.COMPREHENSION_Q2_ATTEMPS + 1
            return 'Bitte beantworten Sie die Frage erneut.'

    def COMPREHENSION_Q3_error_message(self, values):
        if values != getComprehensionQuestionSolution(3):
            self.COMPREHENSION_Q3_ATTEMPS = self.COMPREHENSION_Q3_ATTEMPS + 1
            return 'Bitte beantworten Sie die Frage erneut.'

    def COMPREHENSION_Q4_error_message(self, values):
        if values != getComprehensionQuestionSolution(4):
            self.COMPREHENSION_Q4_ATTEMPS = self.COMPREHENSION_Q4_ATTEMPS + 1
            return 'Bitte beantworten Sie die Frage erneut.'

    COMPREHENSION_Q1 = models.IntegerField(
        choices=getComprehensionQuestionChoices(1),
        label=getComprehensionQuestionLabel(),
        widget=getComprehensionQuestionWidget(),
        solution=getComprehensionQuestionSolution(1)
    )
    COMPREHENSION_Q2 = models.IntegerField(
        choices=getComprehensionQuestionChoices(2),
        label=getComprehensionQuestionLabel(),
        widget=getComprehensionQuestionWidget(),
        solution=getComprehensionQuestionSolution(2)
    )
    COMPREHENSION_Q3 = models.IntegerField(
        choices=getComprehensionQuestionChoices(3),
        label=getComprehensionQuestionLabel(),
        widget=getComprehensionQuestionWidget(),
        solution=getComprehensionQuestionSolution(3)
    )
    COMPREHENSION_Q4 = models.IntegerField(
        choices=getComprehensionQuestionChoices(4),
        label=getComprehensionQuestionLabel(),
        widget=getComprehensionQuestionWidget(),
        solution=getComprehensionQuestionSolution(4)
    )

    COMPREHENSION_Q1_ATTEMPS = models.IntegerField(
        initial=0
    )
    COMPREHENSION_Q2_ATTEMPS = models.IntegerField(
        initial=0
    )
    COMPREHENSION_Q3_ATTEMPS = models.IntegerField(
        initial=0
    )
    COMPREHENSION_Q4_ATTEMPS = models.IntegerField(
        initial=0
    )
