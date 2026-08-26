import random
from otree.api import *

doc = """
Dictator-game allocation task.

The app randomizes the order of dictator-game decisions and the red/green
presentation branch once per participant. Payment-relevant metadata are stored
in participant.vars for export.
"""


class C(BaseConstants):
    NAME_IN_URL = 'dictator_game'
    PLAYERS_PER_GROUP = None
    TASKS_DG_Red = ['DG1_game', 'DG_couleur_red',
                    'DG_couleur_red_green',
                    'DG3_game', 'DG3_femme']
    TASKS_DG_Green = ['DG1_game', 'DG_couleur_green',
                      'DG_couleur_green_red',
                      'DG3_game', 'DG3_femme']
    NUM_ROUNDS = len(TASKS_DG_Red) + 1
    LIST_PAY = ['DG1_amount','id_placebo_intra','id_placebo_intra',
                'id_placebo_inter','DG3_man','DG3_girl']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    DG1_amount = models.FloatField()
    id_placebo_intra = models.FloatField()
    id_placebo_inter = models.FloatField()
    DG3_man = models.FloatField()
    DG3_girl = models.FloatField()
    attention_check_2= models.IntegerField(
        label="Dans cette partie, je dois:",
        choices=[
            [1, "Partager des ressources avec un autre joueur"],
            [2, "Assigner un rôle à un autre joueur"]
        ]
    )


def creating_session(subsession: Subsession):
    if subsession.round_number != 1:
        return

    subsession.session.vars.setdefault('num_finished', 0)

    for player in subsession.get_players():
        participant = player.participant
        participant.progress_DG = 1
        # my_bool selects the red or green color framing branch.
        participant.my_bool = random.choice([True, False])
        participant.selected_round = list(C.LIST_PAY)
        participant.is_paid = random.randint(1, 100)
        random.shuffle(participant.selected_round)
        participant.payoff_round = participant.selected_round[1] if participant.is_paid == 1 else 0

        # The same shuffled round positions are reused across color branches so
        # common pages appear in the same positions regardless of branch.
        round_numbers = list(range(2, C.NUM_ROUNDS + 1))
        random.shuffle(round_numbers)
        participant.task_rounds_DG_red = dict(zip(C.TASKS_DG_Red, round_numbers))
        participant.task_rounds_DG_Green = dict(zip(C.TASKS_DG_Green, round_numbers))


# PAGES
class DG1_instruct_rouge(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.my_bool == True and player.round_number == 1

    form_model = 'player'
    form_fields = ['attention_check_2']


class DG1_instruct_vert(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.my_bool == False and player.round_number == 1

    form_model = 'player'
    form_fields = ['attention_check_2']


class DG1_game(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds_DG_red['DG1_game']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['DG1_amount']


class DG_couleur_red(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return participant.my_bool == True and player.round_number == participant.task_rounds_DG_red['DG_couleur_red']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['id_placebo_intra']


class DG_couleur_green(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.my_bool == False and player.round_number == participant.task_rounds_DG_Green['DG_couleur_green']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['id_placebo_intra']


class DG_couleur_red_green(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return participant.my_bool == True and player.round_number == participant.task_rounds_DG_red['DG_couleur_red_green']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['id_placebo_inter']


class DG_couleur_green_red(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return participant.my_bool == False and player.round_number == participant.task_rounds_DG_Green['DG_couleur_green_red']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['id_placebo_inter']


class DG3_game(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds_DG_red['DG3_game']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['DG3_man']


class DG3_femme(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds_DG_red['DG3_femme']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.progress_DG += 1

    form_model = 'player'
    form_fields = ['DG3_girl']



page_sequence = [DG1_instruct_vert,DG1_instruct_rouge, DG1_game, DG_couleur_red,DG_couleur_green,
                DG_couleur_red_green,DG_couleur_green_red,
                DG3_game, DG3_femme
                 ]
