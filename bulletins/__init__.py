
import random
from otree.api import *


doc = """
Non-blind report-card evaluation task.

Each participant is assigned a randomized order over the 16 available report
cards. The interface displays 10 report cards per participant, matching the
participant-facing instructions and progress indicator.
"""

class C(BaseConstants):
    NAME_IN_URL = 'random_task_order'
    PLAYERS_PER_GROUP = None
    DISPLAYED_BULLETINS = 10
    LAST_DISPLAY_ROUND = DISPLAYED_BULLETINS + 1
    TASKS = ['bulletin_1', 'bulletin_2', 'bulletin_3', 'bulletin_4',
                      'bulletin_5', 'bulletin_6',
                      'bulletin_7', 'bulletin_8', 'bulletin_9',
                      'bulletin_10', 'bulletin_11', 'bulletin_12',
                      'bulletin_13', 'bulletin_14', 'bulletin_15',
                      'bulletin_16'
                      ]
    NUM_ROUNDS = len(TASKS) + 1



class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            participant = p.participant
            participant.progress = 1
            # Assign each report card to a round; only rounds up to
            # LAST_DISPLAY_ROUND are shown, yielding 10 randomized cards.
            round_number = list(range(2, C.NUM_ROUNDS + 1))
            random.shuffle(round_number)
            task_rounds = dict(zip(C.TASKS, round_number))
            participant.task_rounds = task_rounds


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    note_bulletin_1 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_2 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_3 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_4 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_5 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_6 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_7 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_8 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_9 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_10 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_11 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_12 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_13 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_14 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_15 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    note_bulletin_16 = models.FloatField(label="Quelle note donneriez-vous à ce bulletin?")
    mention_1 = models.IntegerField(
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
    growth_1 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Vos intuitions et votre curiosité vous ont permis d’être parmi les meilleurs élèves "],
            [2, "Vos efforts vous ont permis d’être parmi les meilleurs élèves"],
            [3, "Elève brillant.e qui figure parmi les meilleurs élèves "],
            [4, "Votre travail personnel vous a permis d’être parmi les meilleurs élèves de la classe, je vous encourage à poursuivre !"]
        ]
    )
    mention_2 = models.IntegerField(
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
    growth_2 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Votre travail personnel vous a permis d’être parmi les meilleurs élèves de la classe, je vous encourage à poursuivre ! "],
            [2, "Vos efforts vous ont permis d’être parmi les meilleurs élèves"],
            [3, "Elève brillant.e qui figure parmi les meilleurs élèves "],
            [4, "Vos intuitions et votre curiosité vous ont permis d’être parmi les meilleurs élèves"]
        ]
    )
    mention_3 = models.IntegerField(
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
    growth_3 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [2, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [3, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    mention_4 = models.IntegerField(
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
    growth_4 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Intensifier votre travail à la maison pour progresser, vos efforts paieront ! "],
            [2, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [3, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    mention_5 = models.IntegerField(
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
    growth_5 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [2, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [3, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année "]
        ]
    )
    mention_6 = models.IntegerField(
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
    growth_6 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [2, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes "],
            [3, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"],
            [4, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"]
        ]
    )
    mention_7 = models.IntegerField(
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
    mention_8 = models.IntegerField(
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
    mention_9 = models.IntegerField(
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
    mention_10 = models.IntegerField(
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
    mention_11 = models.IntegerField(
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
    mention_12 = models.IntegerField(
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
    mention_13 = models.IntegerField(
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
    mention_14 = models.IntegerField(
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
    mention_15 = models.IntegerField(
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
    mention_16 = models.IntegerField(
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
    growth_7 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Des efforts supplémentaires vous permettront d’atteindre la moyenne"],
            [2, "Des lacunes qui semblent difficiles à surmonter"],
            [3, "Capacités limitées pour poursuivre dans la voie générale, devrait s’orienter vers la voie professionnelle"],
            [4, "Voyez vos lacunes comme des opportunités pour apprendre, n’hésitez pas à me solliciter "]
        ]
    )
    growth_8 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Voyez vos lacunes comme des opportunités pour apprendre, n’hésitez pas à me solliciter"],
            [2, "Des lacunes qui semblent difficiles à surmonter"],
            [3, "Des efforts supplémentaires vous permettront d’atteindre la moyenne"],
            [4, "Capacités limitées pour poursuivre dans la voie générale, devrait s’orienter vers la voie professionnelle"]
        ]
    )
    growth_9 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Vos intuitions et votre curiosité vous ont permis d’être parmi les meilleurs élèves"],
            [2, "Vos efforts vous ont permis d’être parmi les meilleurs élèves"],
            [3, "Elève brillant.e qui figure parmi les meilleurs élèves"],
            [4, "Votre travail personnel vous a permis d’être parmi les meilleurs élèves de la classe, je vous encourage à poursuivre ! "]
        ]
    )
    growth_10 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Votre travail personnel vous a permis d’être parmi les meilleurs élèves de la classe, je vous encourage à poursuivre !"],
            [2, "Vos efforts vous ont permis d’être parmi les meilleurs élèves"],
            [3, "Elève brillant.e qui figure parmi les meilleurs élèves"],
            [4, "Vos intuitions et votre curiosité vous ont permis d’être parmi les meilleurs élèves"]
        ]
    )
    growth_11 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [2, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [3, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    growth_12 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Intensifier votre travail à la maison pour progresser, vos efforts paieront ! "],
            [2, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [3, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    growth_13 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"],
            [2, "Intensifier votre travail à la maison pour progresser, vos efforts paieront !"],
            [3, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [4, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"]
        ]
    )
    growth_14 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Intensifier votre travail à la maison pour progresser, vos efforts paieront ! "],
            [2, "Poursuivez vos efforts dans les matières dans lesquelles vous avez des lacunes"],
            [3, "Votre manque d’intuition risque de vous pénaliser aux examens de fin d’année"],
            [4, "Vos intuitions ne sont pas toujours correctes, ce qui explique certaines difficultés"]
        ]
    )
    growth_15 = models.IntegerField(
        label="Quelle appréciation choisissez-vous de donner à l’élève parmi celles proposées ci-dessous :",
        choices=[
            [1, "Des efforts supplémentaires vous permettront d’atteindre la moyenne"],
            [2, "Des lacunes qui semblent difficiles à surmonter"],
            [3, "Capacités limitées pour poursuivre dans la voie générale, devrait s’orienter vers la voie professionnelle"],
            [4, "Voyez vos lacunes comme des opportunités pour apprendre, n’hésitez pas à me solliciter"]
        ]
    )
    growth_16 = models.IntegerField(
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

        return player.round_number == 1 and not player.participant.vars.get('treatment_blind', True)

    form_model = 'player'
    form_fields = ['attention_check_1']

class bulletin_1(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_1']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_1','mention_1', 'growth_1']


class bulletin_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number <= C.LAST_DISPLAY_ROUND
               and player.round_number == participant.task_rounds['bulletin_2']
               and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_2','mention_2', 'growth_2']


class bulletin_3(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number <= C.LAST_DISPLAY_ROUND
               and player.round_number == participant.task_rounds['bulletin_3']
               and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_3','mention_3', 'growth_3']


class bulletin_4(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_4']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_4','mention_4','growth_4']


class bulletin_5(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_5']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_5','mention_5','growth_5']


class bulletin_6(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_6']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_6','mention_6','growth_6']


class bulletin_7(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
               and player.round_number == participant.task_rounds['bulletin_7']
               and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_7', 'mention_7', 'growth_7']

class bulletin_8(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
               and player.round_number == participant.task_rounds['bulletin_8']
               and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_8', 'mention_8', 'growth_8']


class bulletin_9(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_9']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_9', 'mention_9', 'growth_9']


class bulletin_10(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
               and player.round_number == participant.task_rounds['bulletin_10']
               and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_10', 'mention_10', 'growth_10']


class bulletin_11(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_11']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_11', 'mention_11', 'growth_11']


class bulletin_12(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_12']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_12', 'mention_12', 'growth_12']


class bulletin_13(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_13']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_13', 'mention_13', 'growth_13']


class bulletin_14(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_14']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_14', 'mention_14', 'growth_14']


class bulletin_15(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_15']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_15', 'mention_15', 'growth_15']


class bulletin_16(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return (player.round_number <= C.LAST_DISPLAY_ROUND
                and player.round_number == participant.task_rounds['bulletin_16']
                and not player.participant.vars.get('treatment_blind', True))

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress += 1

    form_model = 'player'
    form_fields = ['note_bulletin_16', 'mention_16', 'growth_16']


page_sequence = [bulletin_intro,
    bulletin_1, bulletin_2, bulletin_3,
    bulletin_4, bulletin_5, bulletin_6,
    bulletin_7, bulletin_8, bulletin_9,
    bulletin_10, bulletin_11, bulletin_12,
    bulletin_13, bulletin_14, bulletin_15,
    bulletin_16
]
