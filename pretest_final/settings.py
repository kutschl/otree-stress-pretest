from os import environ

SESSION_CONFIGS = [
    dict(
        name='Intro',
        app_sequence=['Intro'],
        num_demo_participants=1,
    ),
    dict(
        name='Game',
        app_sequence=['Game'],
        num_demo_participants=1,
    ),
    dict(
        name='PostGame',
        app_sequence=['PostGame'],
        num_demo_participants=1,
    ),
    dict(
        name='IntroTest',
        app_sequence=['Intro'],
        num_demo_participants=1,
        use_browser_bots=True
    ),
    dict(
        name='GamePostTest',
        app_sequence=['PostGame'],
        num_demo_participants=1,
        use_browser_bots=True
    ),
    dict(
        name='Outro',
        app_sequence=['Outro'],
        num_demo_participants=1,
    ),
    dict(
        name='PayoffTest',
        app_sequence=['Game', 'Outro'],
        num_demo_participants=4,
        use_browser_bots=True
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3576715542976'
