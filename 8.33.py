"""
8.33 Reimplement the blackjack application from the case study in Chapter 6 using classes
Card and Deck developed in this chapter and class Hand from Problem 8.32

def blackjack()
    'simulates the house in a game of blackjack'

    deck = shuffledDeck() # get shuffled deck

    house = [] # house hand
    player = [] # player hand

    for i in range(2): # dealing initial hands in 2 rounds
    dealCard(deck, player) # deal to player first
    dealCard(deck, house) # deal to house second

    # print hands
    print('House:{:>7}{:>7}'.format(house[0] , house[1]))
    print(' You:{:>7}{:>7}'.format(player[0], player[1]))

    # while user requests an additional card , house deals it
    answer = input('Hit or stand? (default: hit): ')
    while answer in {'', 'h', 'hit'}:
    card = dealCard(deck, player)
    print('You got{:>7}'.format(card))

    if total(player) > 21: # player total is > 21
    print('You went over... You lose.')
    return

    answer = input('Hit or stand? (default: hit): ')

    # house must play the "house rules"
    while total(house) < 17:
    card = dealCard(deck, house)
    print('House got{:>7}'.format(card))

    if total(house) > 21: # house total is > 21
    print('House went over... You win.')
    return

    # compare house and player hands and print result
    compareHands(house, player)
"""

from random import shuffle

class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = [] # deck is initially empty list

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank, suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        shuffle(self.deck)

"""    def __repr__(self):
        strRepr = ''
        for card in self.deck:
            strRepr += self.deck.getRank()
        print(strRepr)"""

class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of playing card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit


class Hand:
    'allows the player to look at and add to their hand'
    def __init__(self, ID):
        'initialiaze hand'
        self.ID = ID
        self.hand = []

    def addCard(self, card):
        'adds card to hand'
        self.hand.append(card)

    def showHand(self):
        'reveals hand'
        stuff = ''
        for card in self.hand:
            stuff += card.getRank() + " "
            stuff += card.getSuit() + " "
        print("House: {0}".format(stuff))


def BlackJack():
    'Play a game of blackjack'

    'Initiliaze deck of 52 cards'
    deck = Deck()
    print(deck.dealCard())
    deck.shuffle()
    print(deck)


BlackJack()