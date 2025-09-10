# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 15:21:51 2025

@author: Will
"""

"""
Implement function simul() that takes as input an integer n and simulates n rounds
of Rock, Paper, Scissors between players Player 1 and Player 2. The player who wins the
most rounds wins the n-round game, with ties possible. Your function should print the result
of the game as shown. (You may want to use your solution to Problem 5.26.)
>>> simul(1)
Player 1
>>> simul(1)
Tie
>>> simul(100)
Player 2
"""

import random


def printWinner(playerWins):
    #printing winnings
    if playerWins["Player 1"] > playerWins["Player 2"]:
        print("Player 1")
    elif playerWins["Player 1"] < playerWins["Player 2"]:
        print("Player 2")
    else:
        print("Tie")

#picks random choice for player 1
def player1():
    choices = ("Rock", "Paper", "Scissors")

    return choices[random.randint(0,2)]

#picks random choice for player 2
def player2():
    choices = ("Rock", "Paper", "Scissors")

    return choices[random.randint(0,2)]

#Compares choices and returns winning player
def compareChoice(player1Choice, player2Choice):
    if player1Choice == player2Choice:
        return "Tie"
    elif (player1Choice == "Rock") & (player2Choice == "Scissors"):
        return "Player 1"
    elif (player1Choice == "Paper") & (player2Choice == "Rock"):
        return "Player 1"
    elif (player1Choice == "Scissors") & (player2Choice == "Paper"):
        return "Player 1"
    else:
        return "Player 2"

#simulates n games using above functions
def simul(numGames):
    
    #initialize starting conditions
    playerWins = {"Player 1": 0, "Player 2": 0}
    
    for n in range(numGames):
        
        #get player choices (rock, paper, or scissors)
        player1Choice = player1()
        player2Choice = player2()
        #print(player1Choice, player2Choice)
    
        winner = compareChoice(player1Choice, player2Choice)\
        #skip next step if current match is a tie and resume next game
        if winner == "Tie":
            continue
        #increment valeu associated with winning player
        playerWins[winner] += 1
            
        #print(winner)
    
    printWinner(playerWins)

numGames = input("Enter number of rock, paper, scissor games to be played: ")
simul(int(numGames))