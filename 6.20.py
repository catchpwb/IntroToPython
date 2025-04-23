# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 10:34:15 2025

@author: Will
"""

"""
Write function reverse() that takes as input a phone book, that is, a dictionary mapping names (the keys) 
to phone numbers (the values). The function should return another
dictionary representing the reverse phone book mapping phone numbers (the keys) to the
names (the values).
>>> phonebook = {'Smith, Jane':'123-45-67',
'Doe, John':'987-65-43','Baker,David':'567-89-01'}
>>> reverse(phonebook)
{'123-45-67': 'Smith, Jane', '567-89-01': 'Baker,David',
'987-65-43': 'Doe, John'}
"""

def reverse(phonebook):
    
    reversePhonebook = {}
    for key in phonebook.keys():
        
        #update adds to the dictionary the key value pair specified
        #the get() method returns the value at the specified key
        reversePhonebook.update({ phonebook.get(key) : key} )
    
    print(reversePhonebook)
    
    return

phonebook = {'Smith, Jane':'123-45-67','Doe, John':'987-65-43','Baker,David':'567-89-01'}
reverse(phonebook)