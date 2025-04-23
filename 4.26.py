# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:05:24 2025

@author: Will
"""

'''The cryptography function crypto() takes as input a string (i.e., the name of a
file in the current directory). The function should print the file on the screen with this
modification: Every occurrence of string 'secret' in the file should be replaced with
string 'xxxxxx'.
File: crypto.txt >>> crypto('crypto.txt')
I will tell you my xxxxxx. But first, I have to explain
why it is a xxxxxx.
And that is all I will tell you about my xxxxxx.
'''

def crypto(text):
    return text.replace('secret', 'xxxxxx')

infile = open('text.txt', 'r')
content = infile.read()
print(crypto(content))
infile.close()