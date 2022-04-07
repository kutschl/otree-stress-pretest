from ._builtin import Page, WaitPage


class Aufbau(Page):
    pass


class Beschreibung1(Page):
    pass


class Beschreibung2(Page):
    pass


page_sequence = [
    Aufbau,
    Beschreibung1,
    Beschreibung2
]
