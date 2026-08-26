import random
from otree.api import *

doc = """
Final survey app.

Participants answer the equality/norm elicitation items and the pedagogical
belief questions once, after the experimental tasks.
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number != 1:
        return

    for player in subsession.get_players():
        participant = player.participant
        # Randomize whether the direct elicitation or the norm elicitation is
        # shown first for this participant.
        participant.norm_find = random.choice([True, False])
        participant.progress_survey = 1

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label="En quelle année êtes-vous né ?",
        min=1940,
        max=2000)
    happy = models.IntegerField(
        label="Dans quelle mesure êtes-vous satisfait de votre travail en général ?",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7,8,9,10,11
                 ]
    )
    innate_1 = models.IntegerField(
        label="Pour être un bon élève, il faut des prédispositions particulières qui ne s’enseignent pas; ",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7
                 ]
    )
    innate_2 = models.IntegerField(
        label="Pour réussir à l’école, travailler dur ne suffit pas. Il faut également avoir un don ou un talent inné;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7
                 ]
    )
    innate_3 = models.IntegerField(
        label="Tout le monde peut devenir un bon élève en fournissant des efforts et en s’impliquant;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7
                 ]
    )
    innate_4 = models.IntegerField(
        label="Les facteurs de réussite scolaire les plus importants sont la motivation et l'effort soutenu ; les capacités innées sont secondaires;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7
                 ]
    )
    gender_bel_1 = models.IntegerField(
        label="Même s'il n'est pas politiquement correct de le dire, les garçons sont souvent meilleurs en mathématiques que les filles;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7
                 ]
    )
    gender_bel_2 = models.IntegerField(
        label="Bien qu'il y ait des exceptions, les garçons sont généralement plus doués en mathématiques que les filles;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7
                 ]
    )
    better_than_oth = models.IntegerField(
        label="J'ai une meilleure capacité à faire progresser mes étudiants que la plupart de mes collègues;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )
    moder_teach_1 = models.IntegerField(
        label="Une salle de classe bruyante n'est pas un problème tant que les élèves sont occupés à travailler;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )
    moder_teach_2 = models.IntegerField(
        label="Il est important de laisser les élèves exprimer leurs idées, même si elles sont fausses ou absurdes;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )
    moder_teach_3 = models.IntegerField(
        label="Je n'aime pas prendre du retard sur le programme à cause des difficultés et des questions des élèves;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )
    moder_teach_4 = models.IntegerField(
        label="Il est plus efficace d'enseigner directement aux élèves les bonnes réponses plutôt que de leur poser des questions et de passer du temps sur leurs réponses potentiellement erronées;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )
    moder_teach_5 = models.IntegerField(
        label="Les élèves devraient pouvoir choisir les activités que nous faisons en classe;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )
    moder_teach_6 = models.IntegerField(
        label="Lorsqu'un élève pose une question sur un sujet qui l'intrigue, je n'y réponds que si elle est en rapport avec le sujet que j'aborde à ce moment-là. Si elle n'est pas pertinente, je la remets à plus tard pour ne pas perturber le déroulement du cours;",
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4, 5, 6, 7]
    )

    find_equi = models.FloatField(
    min=-30,
    max=30)
    norm_equi = models.FloatField()

class transition(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


    form_model = 'player'


class find_equi(Page):
        
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return not participant.norm_find and player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1

    form_model = 'player'
    form_fields = ['find_equi']


class norm_equi(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1

    form_model = 'player'
    form_fields = ['norm_equi']

class find_equi_bis(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.norm_find and player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1

    form_model = 'player'
    form_fields = ['find_equi']


class survey(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1

    form_model = 'player'
    form_fields = ['happy',
                   'age']


class pedagogical(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    form_model = 'player'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1

    @staticmethod
    def get_form_fields(player: Player):
        # Randomize item order within the first pedagogical-beliefs block.
        form_fields = ['innate_1',  'innate_3',
                    'gender_bel_1',  'better_than_oth',
                    'moder_teach_2',
                   'moder_teach_4',  'moder_teach_6']
        random.shuffle(form_fields)
        return form_fields


class pedagogical_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1

    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        # Randomize item order within the second pedagogical-beliefs block.
        form_fields = ['innate_2','innate_4','gender_bel_2','moder_teach_1','moder_teach_3','moder_teach_5']
        random.shuffle(form_fields)
        return form_fields

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_survey += 1


page_sequence = [transition,find_equi,norm_equi,find_equi_bis, survey, pedagogical, pedagogical_2]
