from random import shuffle
from card import Card

class Deck(object):
    def __init__(self):
        self.cards = []
        def createDeck():
            ranks = [2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King', 'Ace']
            suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
            for suit in suits:
                for rank in range(len(ranks)):
                    self.cards.append(Card(suit, ranks[rank], rank + 2))
        createDeck()
    def shuffleCards(self):
        shuffle(self.cards)
        return self
