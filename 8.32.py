"""
8.32 Implement class Hand that represents a hand of playing cards. The class should have a
constructor that takes as input the player ID (a string). It should support method addCard()
that takes a card as input and adds it to the hand and method showHand() that displays the
player’s hand in the format shown.
>>> hand = Hand('House')
>>> deck = Deck()
>>> deck.shuffle()
>>> hand.addCard(deck.dealCard())
>>> hand.addCard(deck.dealCard())
>>> hand.addCard(deck.dealCard())
>>> hand.showHand()
House: 10 ♥ 8 ♠ 2 ♠
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
        self.deck = [] # deck is initially empty

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

"""
addCard() that takes a card as input and adds it to the hand and method showHand() that displays the
player’s hand
"""

class Hand:

    def __init__(self, ID):
        self.ID = ID
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def showHand(self):
        stuff = ''
        for card in self.hand:
            """print(card.getRank())
            print(card.getSuit())"""
            stuff += card.getRank() + " "
            stuff += card.getSuit() + " "
        print("House: {0}".format(stuff))


hand = Hand('House')
deck = Deck()
deck.shuffle()
hand.addCard(deck.dealCard())
hand.addCard(deck.dealCard())
hand.addCard(deck.dealCard())
hand.showHand()