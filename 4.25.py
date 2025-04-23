# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 13:31:39 2025

@author: Will
"""

def vowelCount(sentence):

    '''
    #using list comprehension. Equivalent to:
    temp = []
    for x in 'aeiou':
        temp.append(sentence.count(x))
    
    return sum(temp)
    '''
      
    temp = [sentence.count(x) for x in 'aeiou']
    
    return sum(temp)
    
print(vowelCount('What is the capital of Canada?'))