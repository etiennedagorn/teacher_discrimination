from os import environ

# Room used for persistent participant links in production.
ROOMS = [
    dict(
        name='enquete_enseignant',
        display_name='Enquête pratiques enseignantes'
    )
    ]


SESSION_CONFIGS = [
    dict(
        name="main",
        display_name="Enquête enseignant",
        num_demo_participants=40,
        num_participants=40,
        # Main replication sequence. The two IAT apps are mutually exclusive:
        # the intro app assigns a participant-level treatment flag that routes
        # participants to either the pre-DG or post-DG IAT.
        app_sequence=['intro','bulletins_blind','bulletins','iat','dictator_game','iat_2','survey','random_number'],
        # IAT category labels. Matching stimuli are loaded from iat/stimuli.csv
        # and iat_2/stimuli.csv.
        primary=['Masculin', 'Féminin'],
        secondary=['Arts & Littérature', 'Sciences'],
        num_iterations={1: 5, 2: 5, 3: 10, 4: 20, 5: 5, 6: 10, 7: 20},
    )
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

INSTALLED_APPS = [
    'otree',
]


PARTICIPANT_FIELDS = {
    'round_numbers',
    'progress',
    'progress_DG',
    'progress_survey',
    'task_rounds',
    'task_rounds_DG',
    'task_rounds_DG_red',
    'task_rounds_DG_Green',
    'my_bool',
    'payoff_round',
    'selected_round',
    'is_paid',
    'norm_find',
    'find_equi',
    'treatment',
    'treatment_blind'
}

SESSION_FIELDS = ['params',
                  'num_finished',
                  'treatment']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "fr"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = True

ADMIN_USERNAME = "admin"
# For replication, set this in the environment rather than editing the code.
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_TITLE = "Otree development"
DEMO_PAGE_INTRO_HTML = """
Survey for teachers
"""

# Keep a development fallback so the replication package runs locally, while
# allowing deployments to inject their own secret key.
SECRET_KEY = environ.get("OTREE_SECRET_KEY", "dev-secret-key-change-me")
