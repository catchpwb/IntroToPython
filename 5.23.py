# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 11:55:50 2025

@author: Will
"""

'''
Write function pay() that takes as input an hourly wage and the number of hours an
employee worked in the last week. The function should compute and return the employee’s
pay. Overtime work should be paid in this way: Any hours beyond 40 but less than or equal
60 should be paid at 1.5 times the regular hourly wage. Any hours beyond 60 should be
paid at 2 times the regular hourly wage
'''

def pay(wage, numHours):
    
    pay = 0
    if (40 < numHours <= 60):
        pay += (numHours - 40) * wage * 1.5
        pay += 40 * wage
    elif (60 < numHours):
        pay += (numHours - 60) * wage * 2
        pay += 20 * wage * 1.5
        pay += 40 * wage
    else:
        pay += numHours * 10
    
    print(pay)
    
    return 
        
pay(10,35)
pay(10,45)
pay(10,61)