# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 10:31:59 2025

@author: Will
"""
"""
bubblesort
"""

def bubblesort(lst):
    for j in range(len(lst)-1):    
        for i in range((len(lst) - j - 1)):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                print(lst)
            print('i ',i)
        print('j ',j)
    return lst

lst = [1,6,5,4,3,2,7]
print(bubblesort(lst))