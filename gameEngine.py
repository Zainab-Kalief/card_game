from random import shuffle
from card import Card
from deck import Deck
from player import Player
drawCards = []

class Game(object):

    def deal(self,deck, ply1, ply2):
        ply1.hand = deck.cards[:4]
        ply2.hand = deck.cards[5:9]
        del deck.cards[:4]
        del deck.cards[5:9]
        return self

    def playOneRound(self, ply1, ply2):
        count = 1

        for x in range(0,20): #at 20 rounds end the game
            if len(ply1.hand) == 0 or len(ply2.hand) == 0:
                return 'GAME OVERRRRR'
            else:
                player1card = ply1.hand.pop(0)
                player2card = ply2.hand.pop(0)
                global drawCards
                if player1card.value > player2card.value:
                    ply1.hand.extend((player2card, player1card))
                    print '~~~ROUND ' + str(count) + '~~~~'
                    if drawCards != []:
                        for card in drawCards:
                            ply1.hand.append(card)
                    drawCards = []
                    print ply1.name, 'played', player1card.rank, 'of', player1card.suit, 'while', ply2.name, 'played', player2card.rank, 'of', player2card.suit, '~>', ply1.name, 'won!!!'
                    print 'Cards Left ~~>', ply1.name, 'has', len(ply1.hand), '~', ply2.name, 'has', len(ply2.hand), '\n'
                elif player1card.rank < player2card.rank:
                    print '~~~ROUND ' + str(count) + '~~~~'
                    ply2.hand.extend((player2card, player1card))
                    if drawCards != []:
                        for card in drawCards:
                            ply2.hand.append(card)
                    drawCards = []
                    print ply2.name, 'played', player2card.rank, 'of', player2card.suit, 'while', ply1.name, 'played', player1card.rank, 'of', player1card.suit, '~>', ply2.name, 'won!!!'
                    print 'Cards Left ~~>', ply1.name, 'has', len(ply1.hand), '~', ply2.name, 'has', len(ply2.hand), '\n'
                else:
                    print '~~~ROUND ' + str(count) + '~~~~'
                    drawCards.extend((player2card, player1card))
                    print 'DRAWWWWW, save the cards for the next round'
                    print 'Cards Left ~~>', ply1.name, 'has', len(ply1.hand), '~', ply2.name, 'has', len(ply2.hand), '\n'
                count += 1

        return self


round1 = Game()

player1 = Player('Wura')
player2 = Player('Raymond')

deck1 = Deck()
deck1.shuffleCards() #52 cards shuffled

round1.deal(deck1, player1, player2) #give each ply 4 cards and remove cards from deal

round1.playOneRound(player1, player2) #play until 20 rounds and end the game OR until some is out of cards
