# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 12:56:47 2025

@author: Will
"""
"""
Write function week() that takes no arguments. It will repeatedly ask the user to enter
an abbreviation for a day of the week (Mo, Tu, We, Th, Fr, Sa, or Su) and then print the
corresponding day.
>>> week()
Enter day abbreviation: Tu
Tuesday
Enter day abbreviation: Su
Sunday
Enter day abbreviation: Sa
Saturday
Enter day abbreviation:
"""

def week():
    daysOfWeek = {'Mo' : 'Monday', 'Tu' : 'Tuesday', 'We' : 'Wednesday', 'Th' : 'Thursday',
                  'Fr' : 'Friday', 'Sa' : 'Saturday', 'Su' : 'Sunday'}
    
    string = input('Enter day abbreviation: ')
    while string != '':
        if string in daysOfWeek:
            print(daysOfWeek[string])
        else:
            string = input('Enter day abbreviation: ')
            continue #skip to top of while loop
            
        string = input('Enter day abbreviation: ')

week()