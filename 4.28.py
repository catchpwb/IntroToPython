# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 14:43:15 2025

@author: Will
"""

'''
Implement function links() that takes as input the name of an HTML file (as a
string) and returns the number of hyperlinks in that file. To do this you will assume that
each hyperlink appears in an anchor tag. You also need to know that every anchor tag ends
with the substring <\a>.
Test your code on HTML file twolinks.html or any HTML file downloaded from the
web into the folder where your program is
'''

def links(file):
    infile = open(file, 'r')
    content = infile.read()
    numLinks = content.count('</a>')
    
    return numLinks
    
print(links('sample1.html'))
print(links('sample2.html'))