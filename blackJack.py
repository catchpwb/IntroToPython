# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 13:26:27 2025

@author: Will
"""

"""
Simulates a game of blackjack utilizing user input
Can be updated as more is learned
"""

import random

def shuffleDeck():
    #creates a deck of cards and returns a shuffled deck
    
    #initialize 2 sets to represent eh different suits and ranks of cards
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

    #initialize empty list
    deck = []
    
    #nested for loop to iterate over sets list and ranks to create a deck
    for suit in suits:
        for rank in ranks:
            #this is list of strings with rank at [0], and suit at [2]
            deck.append(rank + ' ' + suit)
            
    #utilizes the random module to shuffle deck
    random.shuffle(deck)
    
    #print(deck)
    
    return deck

def dealCards(participant, deck):
    #deals cards to participant and "house" using 2 lists
    
    #takes deck and appends top card and removes from deck
    card = deck.pop()
    #print('card= {}'.format(card))
    participant.append(card)
    
    return card


def computeTotal(hand):
    #computes each players hand total
    
    #initialize dictionary containing integer values for each rank
    #chose '1' : 10 because the first element in the string representation of 10 is 1
    values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
              '9' : 9, '1' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11}
    
    total = 0
    numAces = 0
    
    #hand has multiple cards so we iterate over cards
    #values is the dictionary and we evaluate it at the first character in the string card 
    #add up number of aces in hand
    for card in hand:
        #print('card[0]= {}'.format(card[0]))
        total += values[card[0]]
        #print('total= {0}, card = {1}'.format(total, card))
        if card[0] == 'A':
            numAces += 1
    
        #print('numAces= {}'.format(numAces))
    
    #if total is over 21 with aces in hand, evaluate ace with value 1 instead of 10
    while total > 21 & numAces > 0:
        total -= 10
        numAces -= 1
    
    return total

def compareHands(house, player):
    #compares each players hands and declares winner
    
    #mutual assignment 
    houseTotal, playerTotal = computeTotal(house), computeTotal(player)
    
    if (houseTotal > playerTotal):
        print('YOU LOSE')
    elif (playerTotal > houseTotal):
        print('YOU WIN')
    elif (houseTotal == 21 and 2 == len(house) < len(player)):
        print('YOU LOSE! HOUSE WINS WITH BLACKJACK!')
    elif(playerTotal == 21 and 2 == len(player) < len(house)):
        print('YOU WIN! PLAYER WINS WITH BLACKJACK!')
    else:
        print('IT\'S A TIE')
    return
          
def blackJack():
    #main function 
    
    house = []
    player = []
    
    #initialize shuffled deck
    deck = shuffleDeck()
    
    #deal 2 cards to player and house
    for i in range(2):
        dealCards(player, deck)
        dealCards(house, deck)
        print('player hand {0}, house hand {1}'.format(player, house))
    
    #choose cards until player stands
    answer = input('Would you like hit or stand? ')
    while answer == 'hit':
        dealCards(player, deck);
        print('player hand {0}, house hand {1}'.format(player, house))
        
        if computeTotal(player) > 21:
            print('PLAYER WENT OVER! YOU LOSE!')
            return
        
        answer = input('Would you like hit or stand? ')

    #house chooses cards acoording to house rules (house must hit if total is lower than 17)
    while computeTotal(house) < 17:
        dealCards(house,deck)
        print('player hand {0}, house hand {1}'.format(player, house))
        
        
        if computeTotal(house) > 21:
            print('HOUSE WENT OVER! YOU WIN!')
            return
        
    compareHands(house, player)


#LET'S PLAY BLACKJACK
blackJack()
