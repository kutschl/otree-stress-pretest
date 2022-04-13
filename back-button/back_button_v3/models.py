from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'back_button_v3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.StringField(choices=[
                            '2', '3', '4', '5'], widget=widgets.RadioSelect, label='What is 2+2?')
    q2 = models.StringField(choices=[
                            '8', '9', '10', '11'], widget=widgets.RadioSelect, label='What is 4+4?')







    def set_error_message(self,value):
        correct_answers = {
                                "q1" :'4',
                                "q2" :'8',
                                 }

        list_answers = list(value.items())[0:] 
        list_correct_answers = list(correct_answers.items())

        if list_answers != list_correct_answers:

          Text = 'You did not answer all questions correctly. Please read the instructions again and correct your answers.'

          return Text    