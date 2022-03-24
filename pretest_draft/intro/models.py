
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db.models.signals import pre_save

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Intro'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    comm_1_RTF = models.StringField(label="Platz für Kommentare, falls Ihnen die Beschreibungen auf dieser Seite unklar erscheinen", blank=True)
    vorname = models.StringField(label="Vorname")
    nachname = models.StringField(label="Nachname")
    straße = models.StringField(label="Straße und Hausnummer")
    plz = models.IntegerField(label="Postleitzahl")
    stadt = models.StringField(label="Stadt")
    email = models.StringField(label="E-Mail")
    iban = models.StringField(label="IBAN")
    bic = models.StringField(label="BIC")
    alter = models.IntegerField(label="Alter")
    job = models.IntegerField(widget=widgets.RadioSelect,
    choices=[
        [0, 'Student/Studentin'],
        [1, 'Berufstätig'],
        [2, 'Keines zutreffend'],
    ],
    label="Was beschreibt Ihre berufliche Situation am Besten?")
    gender = models.IntegerField(widget=widgets.RadioSelect,
    choices=[
        [0, 'Männlich'],
        [1, 'Weiblich'],
        [2, 'Divers'],
        [3, 'Keine Angabe'],
    ],
    label="Mit welchem Geschlecht identifizieren sie sich?")
    erwachsene = models.IntegerField(label="Anzahl der Erwachsenen in Ihrem Haushalt")
    kinder = models.IntegerField(label="Anzahl der Kinder in Ihrem Haushalt")
