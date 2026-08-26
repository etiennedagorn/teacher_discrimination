
import random
from otree.api import *


doc = """
Blind report-card evaluation task.

Participants assigned to the blind condition evaluate the report cards without
the gender image cue used in the non-blind task.
"""

class C(BaseConstants):
    NAME_IN_URL = 'bulletin'
    PLAYERS_PER_GROUP = None
    DISPLAYED_BULLETINS = 8
    TASKS = ['bulletin_1', 'bulletin_2', 'bulletin_3', 'bulletin_4',
                      'bulletin_5', 'bulletin_6',
                      'bulletin_7', 'bulletin_8'
                      ]
    NUM_ROUNDS = DISPLAYED_BULLETINS + 1



class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            participant = p.participant
            participant.progress = 1
            # Assign each blind report card to one displayed round.
            round_number = list(range(2, C.NUM_ROUNDS + 1))
            random.shuffle(round_number)
            task_rounds = dict(zip(C.TASKS, round_number))
            participant.task_rounds = task_rounds


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    note_bulletin_blind_1 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_2 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_3 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_4 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_5 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_6 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_7 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_blind_8 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    mention_blind_1 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_1 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Vos intuitions et votre curiosité vous ont permis d’être parmi les meilleurs élèves "],
            [2, "Vos efforts vous ont permis d’être parmi les meilleurs élèves"],
            [3, "Elève brillant.e qui figure parmi les meilleurs élèves "],
            [4, "Votre travail personnel vous a permis d’être parmi les meilleurs élèves de la classe, je vous encourage à poursuivre !"]
        ]
    )
    mention_blind_2 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_2 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Votre travail personnel vous a permis d’être parmi les meilleurs élèves de la classe, je vous encourage à poursuivre ! "],
            [2, "Vos efforts vous ont permis d’être parmi les meilleurs élèves"],
            [3, "Elève brillant.e qui figure parmi les meilleurs élèves "],
            [4, "Vos intuitions et votre curiosité vous ont permis d’être parmi les meilleurs élèves"]
        ]
    )
    mention_blind_3 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_3 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [2, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [3, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    mention_blind_4 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_4 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Intensifier votre travail à la maison pour progresser, vos efforts paieront ! "],
            [2, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [3, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    mention_blind_5 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_5 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [2, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [3, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année "]
        ]
    )
    mention_blind_6 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_6 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [2, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes "],
            [3, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"],
            [4, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"]
        ]
    )
    mention_blind_7 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    mention_blind_8 = models.IntegerField(
        label="Quelle mention choisissez-vous pour cet élève parmi celles proposées ci-dessous:",
        choices=[
            [1, "Bilan inquiétant"],
            [2, "Mise en garde pour le travail"],
            [3, "Mise en garde pour la conduite"],
            [4, "Encouragements"],
            [5, "Compliments"],
            [6, "Félicitations"],
            [7, "Excellence"]
        ]
    )
    growth_blind_7 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Des efforts supplémentaires vous permettront d’atteindre la moyenne"],
            [2, "Des lacunes qui semblent difficiles à surmonter"],
            [3, "Capacités limitées pour poursuivre dans la voie générale, devrait s’orienter vers la voie professionnelle"],
            [4, "Voyez vos lacunes comme des opportunités pour apprendre, n’hésitez pas à me solliciter "]
        ]
    )
    growth_blind_8 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Voyez vos lacunes comme des opportunités pour apprendre, n’hésitez pas à me solliciter"],
            [2, "Des lacunes qui semblent difficiles à surmonter"],
            [3, "Des efforts supplémentaires vous permettront d’atteindre la moyenne"],
            [4, "Capacités limitées pour poursuivre dans la voie générale, devrait s’orienter vers la voie professionnelle"]
        ]
    )
    attention_check_1= models.IntegerField(
        label="Dans cette partie, je dois évaluer:",
        choices=[
            [1, "Des copies"],
            [2, "Des bulletins"]
        ]
    )


# PAGES
class bulletin_intro(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.vars.get('treatment_blind', True)


    form_model = 'player'
    form_fields = ['attention_check_1']

class bulletin_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds['bulletin_1']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_1','mention_blind_1', 'growth_blind_1']


class bulletin_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds['bulletin_2']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_2','mention_blind_2', 'growth_blind_2']


class bulletin_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds['bulletin_3']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_3','mention_blind_3', 'growth_blind_3']


class bulletin_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number == participant.task_rounds['bulletin_4']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_4','mention_blind_4','growth_blind_4']


class bulletin_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number == participant.task_rounds['bulletin_5']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_5','mention_blind_5','growth_blind_5']


class bulletin_6(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number == participant.task_rounds['bulletin_6']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_6','mention_blind_6','growth_blind_6']


class bulletin_7(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number == participant.task_rounds['bulletin_7']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_7', 'mention_blind_7', 'growth_blind_7']


class bulletin_8(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number == participant.task_rounds['bulletin_8']
                and player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_blind_8', 'mention_blind_8', 'growth_blind_8']



page_sequence = [bulletin_intro,
    bulletin_1, bulletin_2, bulletin_3,
    bulletin_4, bulletin_5, bulletin_6,
    bulletin_7, bulletin_8]
