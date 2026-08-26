import random
from otree.api import *

doc = """
Introductory app for the teacher survey.

This app performs the device check, records baseline respondent
characteristics, and assigns the participant-level treatment flags used by
later apps.
"""


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number != 1:
        return

    # Shared session counter displayed on the first page.
    subsession.session.vars.setdefault('num_finished', 0)

    for player in subsession.get_players():
        participant = player.participant
        # treatment=False routes the participant to the first IAT; treatment=True
        # routes the participant to the second IAT after the dictator game.
        participant.vars['treatment'] = random.choice([True, False])

        # About 10% of participants see the blind bulletin condition.
        participant.vars['treatment_blind'] = random.randint(1, 10) == 5


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.BooleanField()
    is_mobile = models.BooleanField()
    gender = models.IntegerField(
        label='Êtes-vous ?',
        choices=[
            [1, "Un homme"],
            [2, "Une femme"],
            [3, "Ne souhaite pas répondre"]
        ]
    )
    department = models.IntegerField(
        label="Dans quelle académie exercez-vous ?",
        choices=[
            [1, "Aix-Marseille"],
            [2, "Amiens"],
            [3, "Besançon"],
            [4, "Bordeaux"],
            [5, "Clermont-Ferrand"],
            [6, "Corse"],
            [7, "Créteil"],
            [8, "Dijon"],
            [9, "Grenoble"],
            [10, "Guadeloupe"],
            [11, "Guyane"],
            [12, "La Réunion"],
            [13, "Lille "],
            [14, "Limoges"],
            [15, "Lyon"],
            [16, "Martinique"],
            [17, "Mayotte"],
            [18, "Montpellier"],
            [19, "Nancy-Metz"],
            [20, "Nantes"],
            [201, "Nice"],
            [21, "Normandie"],
            [22, "Nouvelle-Calédonie"],
            [23, "Orléans-Tours"],
            [24, "Paris"],
            [25, "Poitiers"],
            [26, "Polynésie-Française"],
            [27, "Reims"],
            [28, "Rennes"],
            [29, "Saint-Pierre et Miquelon"],
            [30, "Strasbourg"],
            [31, "Toulouse"],
            [32, "Versailles"],
            [33, "Wallis-et-Futuna"]
        ]
    )
    disciplines = models.IntegerField(
        label="Quelle discipline enseignez-vous ?",
        choices=[
            [1, "Mathématiques"],
            [2, "Physique-chimie"],
            [3, "Sciences de la vie et de la Terre"],
            [4, "Technologie - Sciences numériques et technologie"],
            [5, "Histoire-géographie"],
            [6, "Français"],
            [7, "Philosophie"],
            [8, "Anglais"],
            [9, "Allemand"],
            [10, "Espagnol"],
            [11, "Italien"],
            [12, "Sciences économiques et sociales (SES)"],
            [13, "Éducation physique et sportive"],
            [14, "Arts plastiques"],
            [15, "Éducation musicale"],
            [16, "Autre"]
        ]
    )
    niveau = models.IntegerField(
        label="A quel niveau enseignez-vous ?",
        choices=[
            [1, "Collège"],
            [2, "Lycée"],
            [3, "Collège & Lycée"]
        ]
    )
    experience = models.IntegerField(
        label="Depuis combien d'années enseignez-vous ?",
        min=0,
        max=50)

# PAGES
class Intro(Page):
    form_model = 'player'
    form_fields = ['is_mobile']

    def error_message(player: Player, values):
        if values['is_mobile']:
            return "Nous sommes désolés, mais cette enquête ne peut se dérouler que sur un ordinateur et non sur un mobile."

    def vars_for_template(self):
        return {
            'num_finished': self.session.vars['num_finished']
        }


class intro_2(Page):
    form_model = 'player'

class intro_3(Page):
    form_model = 'player'
    form_fields = ['gender',
                   'department',
                   'niveau',
                   'disciplines',
                   'experience']

page_sequence = [Intro,intro_2, intro_3]
