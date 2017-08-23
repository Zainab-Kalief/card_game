from random import shuffle
from card import Card
from deck import Deck

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
