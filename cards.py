import random


class Suit:
    def __init__(self, suit_name):
        self.suit_name = suit_name


class Rank:
    def __init__(self, rank_value, icon):
        self.rank_value = rank_value
        self.icon = icon


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{}{}'. format(self.rank.icon, self.suit.suit_name)


this_cards_suit = Suit("D")
this_cards_rank = Suit(5, "5")
this_card = Card(this_cards_rank, this_cards_suit)
print(this_card)










