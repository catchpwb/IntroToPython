# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:58:30 2025

@author: Will
"""

"""
The mirror image of string vow is string wov, and the mirror image wood is string
boow. The mirror image of string bed cannot be represented as a string, however, because
the mirror image of e is not a valid character.
Develop function mirror() that takes a string and returns its mirror image but only if
the mirror image can be represented using letters in the alphabet.
>>> mirror('vow')
'wov'
>>> mirror('wood')
'boow'
>>> mirror('bed')
'INVALID'
"""

def mirror(string):
    validLetters = {'b':'d', 'd':'b', 'h':'h', 'i':'i', 'o':'o', 't':'t', 'v':'v', 'w':'w', 'x':'x'}
    mirroredString = ''
    
    for char in string:
        if char in validLetters.values():
            mirroredString += validLetters.get(char)
        else:
            print("INVALID")
            return
    
    print(mirroredString[::-1])

string = input("Please enter a string to be mirrored: ")
mirror(string)