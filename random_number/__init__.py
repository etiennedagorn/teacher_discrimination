import random
from otree.api import *

doc = """
Final contact and participant identifier app.

The app collects contact details for the payment lottery and shows the
participant identifier that can be used for withdrawal requests.
"""


class C(BaseConstants):
    NAME_IN_URL = 'numb'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.StringField(
        label="Quel est votre email ? Il sera utilisé uniquement pour vous contacter suite au tirage au sort pour le paiement.")
    follow_up = models.IntegerField(
        label="Je souhaite être tenu informé des résultats de l'enquête par mail via l'adresse mentionnée ci-dessus",
        choices=[
            [1, "Oui"],
            [2, "Non"]
        ]
    )

# PAGES

class contact(Page):
    form_model = 'player'

    form_fields = ['email',
                   'follow_up']

class random_number(Page):
    form_model = 'player'




page_sequence = [contact,random_number]
