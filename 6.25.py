# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:42:19 2025

@author: Will
"""
"""
Write function different() that takes a two-dimensional table as input and returns
the number of distinct entries in the table.
>>> t = [[1,0,1],[0,1,0]]
>>> different(t)
2
>>> t = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
>>> different(t)
10
"""

def different(table):
    uniqueElements = []
    
    for row in table:
        for value in row:
            if value not in uniqueElements:
                uniqueElements.append(value)    
                
    print(len(uniqueElements))
    return


table = [[1,0,1], [0,1,0]]
different(table)

table = [[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
different(table)