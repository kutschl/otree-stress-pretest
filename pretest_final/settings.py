from os import environ

SESSION_CONFIGS = [
    dict(
        name='Intro',
        app_sequence=['Intro'],
        num_demo_participants=1,
    ),
    dict(
        name='Intro_Test',
        app_sequence=['Intro'],
        num_demo_participants=10,
        use_browser_bots=True
    ),
    dict(
        name='Instructions',
        app_sequence=['Instructions'],
        num_demo_participants=1,
    ),
    dict(
        name='Instructions_Test',
        app_sequence=['Instructions'],
        num_demo_participants=10,
        use_browser_bots=True
    ),
    dict(
        name='Comprehension',
        app_sequence=['Comprehension'],
        num_demo_participants=1,
    ),
    dict(
        name='Game',
        app_sequence=['Game'],
        num_demo_participants=3,
    ),
    dict(
        name='Outro',
        app_sequence=['Outro'],
        num_demo_participants=1,
    ),
    dict(
        name='Game_Outro_Test',
        app_sequence=['Game', 'Outro'],
        num_demo_participants=50,
        use_browser_bots=True
    ),
    dict(
        name='Game_Outro',
        app_sequence=['Game', 'Outro'],
        num_demo_participants=50,
    ),
    dict(
        name='Experiment',
        app_sequence=['Intro', 'Instructions', 'Comprehension', 'Game', 'AfterGame', 'Outro'],
        num_demo_participants=1,
    )

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

ADMIN_USERNAME = 'admin#56'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3576715542976'
