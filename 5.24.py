# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:22:26 2025

@author: Will
"""

'''
Write function case() that takes a string as input and returns 'capitalized', 'not
capitalized', or 'unknown', depending on whether the string starts with an uppercase
letter, lowercase letter, or something other than a letter in the English alphabet, respectively.
'''

def case(string):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    
    if string[0] in upper:
        print('capitalized')
        return
    elif string[0] in lower:
        print('not capitalized')
        return
    else:
        print('unknown')
        return

case('Capitalized')
case('notcapitalized')
case('~unknown')