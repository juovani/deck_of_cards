import random


class Deck:
    def __init__(self):
        self.cards = []

        for i in [" Clubs", " Spades", " Hearts", " Diamonds"]:
            for y in range(1, 14):
                x = y
                if x == 1:
                    str(x)
                    x = "A"
                elif x == 11:
                    str(x)
                    x = "J"
                elif x == 12:
                    str(x)
                    x = "Q"
                elif x == 13:
                    str(x)
                    x = "K"
                self.cards.append(Card(i, x))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def add(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        drawn_card = self.cards[0]
        self.cards = self.cards[1:]
        return drawn_card


class Suit:
    def __init__(self, suit_name):
        self.suit_name = suit_name


class Rank:
    def __init__(self, rank_value, icon):
        self.rank_value = rank_value
        self.icon = icon


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '{}{}'. format(self.rank, self.suit)


deck_cards = Deck()
deck_cards.shuffle()
deck_cards.print_deck()
card = deck_cards.draw()
print("------")
print(card)







