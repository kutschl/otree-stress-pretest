from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='entire_survey', num_demo_participants=100, app_sequence=['intro','MPL_intro','MPL_main']),
dict(name='wtp_only', num_demo_participants=100, app_sequence=['MPL_intro','MPL_main'])]
LANGUAGE_CODE = 'de'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# 'intro','umwelt_wissen','WTP','DUAL','duschform','wasser_aufbereitung','umwelt_einstellung','psychologie','essen'
