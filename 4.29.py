# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:01:42 2025

@author: Will
"""
'''
Write a function stats() that takes one input argument: the name of a text file. The
function should print, on the screen, the number of lines, words, and characters in the file;
your function should open the file only once
'''

def stats(text):
    infile = open(text, 'r')
    content = infile.read()
    lineCount = content.count('\n') + 1
    wordCount = len(content.split())
    numChar = len(content)
    print('Line count : {}'.format(lineCount))
    print('Word count : {}'.format(wordCount))
    print('Number of characters : {}'.format(numChar))
    return
    
stats('text.txt')