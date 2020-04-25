import random


class Card:
    SUITS = "♤♧♡♢"
    RANKS = range(1, 14)
    SYMBOLS = "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.index = suit + self.SYMBOLS[rank - self.RANKS[0]]

    def __repr__(self):
        return self.index


class Deck:

    def __init__(self):
        self.cards = [Card(suit, rank)
                      for suit in Card.SUITS
                      for rank in Card.RANKS]
        random.shuffle(self.cards)

    def draw(self, n=1):
        cards = self.cards[:n]
        del self.cards[:n]
        return cards


deck = Deck()
player_deck = deck.draw(26)
cpu_deck = deck.draw(26)
print(player_deck)
print(cpu_deck)

print(deck.cards)
