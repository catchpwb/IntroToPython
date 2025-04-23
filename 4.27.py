# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:21:03 2025

@author: Will
"""

'''
Write a function fcopy() that takes as input two file names (as strings) and copies
the content of the first file into the second.
>>> fcopy('example.txt','output.txt')
>>> open('output.txt').read()
'The 3 lines in this file end with the new line character.\n\n
There is a blank line above this line.\n'
'''

def fcopy(file1, file2):
    outfile = open('text2.txt', 'w')
    temp = outfile.write(file1)
    return temp
    
infile = open('text.txt')
content = infile.read()
fcopy(content, 'text2.txt')
print(open('text2.txt').read())
infile.close()