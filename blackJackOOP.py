"""
8.33 Reimplement the blackjack application from the case study in Chapter 6 using classes
Card and Deck developed in this chapter and class Hand from Problem 8.32
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
        print("{0}: {1}".format(self.ID, stuff))

    def __len__(self):
        'overrides length operator'
        return (len(self.hand))

    def __getitem__(self, index):
        'override getitem to make the hand class subscriptable'
        return self.hand[index]


def total(currentHand):
    'returns the value of the blackjack hand'
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
    '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    result = 0
    numAces = 0

    # add up the values of the cards in the hand
    # also add the number of aces
    for i in range(len(currentHand)):
        result += values[currentHand[i].getRank()]
        if currentHand[0].getRank() == 'A':
            numAces +=1

    # while value of hand is > 21 and there is an ace
    # in the hand with value 11, convert its value to 1
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1

    return result

def compareHands(house, player):
    'compares house and player hands and prints outcome'

    # compute house and player hand total
    houseTotal, playerTotal = total(house), total(player)

    if houseTotal > playerTotal:
        print('You lose.')
    elif houseTotal < playerTotal:
        print('You win.')
    elif houseTotal == 21 and 2 == len(house) < len(player):
        print('You lose.') # house wins with a blackjack
    elif playerTotal == 21 and 2 == len(player) < len(house):
        print('You win.') # players wins with a blackjack
    else:
        print('A tie.')

def BlackJack():
    'Play a game of blackjack'

    'Initiliaze deck of 52 cards'
    deck = Deck()

    deck.shuffle()

    house = Hand("House")
    player = Hand("Player")

    #deal 2 cards
    for i in range(2):
        player.addCard(deck.dealCard())
        house.addCard(deck.dealCard())

    #print hands
    player.showHand()
    house.showHand()

    answer = input("Hit or stand? (default is hit): ")
    while answer in ({"", "h", "hit"}):
        player.addCard(deck.dealCard())
        print("Your new hand: ")
        player.showHand()

        if total(player) > 21: # player total is > 21
            print('You went over... You lose.')
            return
        
        answer = input('Hit or stand? (default: hit): ')

        # house must play the "house rules"
        while total(house) < 17:
            house.addCard(deck.dealCard())
            print("House new hand: ")
            house.showHand()

            if total(house) > 21: # house total is > 21
                print('House went over... You win.')
                return

    print("Player total is {0}".format(total(player)))
    print("House total is {0}".format(total(house)))
    compareHands(house, player)

BlackJack()