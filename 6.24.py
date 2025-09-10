# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:54:04 2025

@author: Will
"""

"""
Implement function names() that takes no input and repeatedly asks the user to enter
the first name of a student in a class. When the user enters the empty string, the function
should print for every name the number of students with that name.
>>> names()
Enter next name: Valerie
Enter next name: Bob
Enter next name: Valerie
Enter next name: Amelia
Enter next name: Bob
Enter next name:
There is 1 student named Amelia
There are 2 students named Bob
There are 2 students named Valerie
"""

def names():
    
    string = input('Enter next name: ')
    #initialize dictionary
    dictNames = {}
    
    #check its not empty
    while string != '':
        
        #incrememnt value of key if more than 1 student with same name otherwise set to 1
        if string in dictNames:
            dictNames[string] += 1
        else:
            dictNames[string] = 1
            
        string = input('Enter next name: ')
    
    #print results
    for key in dictNames:
        if dictNames[key] == 1:
            print("There is {0} student named {1}".format(dictNames[key], key))
        else:
            print("There are {0} students named {1}".format(dictNames[key], key))
names()