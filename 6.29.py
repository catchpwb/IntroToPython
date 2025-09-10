# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 13:11:38 2025

@author: Will
"""

"""
In your class, many students are friends. Let’s assume that two students sharing
a friend must be friends themselves; in other words, if students 0 and 1 are friends and
students 1 and 2 are friends, then students 0 and 2 must be friends. Using this rule, we can
partition the students into circles of friends.
To do this, implement a function networks() that takes two input arguments. The first
is the number n of students in the class. We assume students are identified using integers
0 through n-1. The second input argument is a list of tuple objects that define friends.
For example, tuple (0,2) defines students 0 and 2 as friends. Function networks() should
print the partition of students into circles of friends as illustrated:
>>> networks(5, [(0, 1), (1, 2), (3, 4)])
Social network 0 is {0, 1, 2}
Social network 1 is {3, 4}
"""

def network(numStudents, listTuples):
    socialDict = {}
    socialNetwork = 0
    
    for n in range(len(listTuples)-1):
        if listTuples[n][1] == listTuples[n+1][0]:
            socialDict.update({socialNetwork : (listTuples[n][0], listTuples[n][1], listTuples[n+1][1])})
            socialNetwork += 1
        else:
            socialDict.update({socialNetwork : (listTuples[n+1][0], listTuples[n+1][1])})
            socialNetwork += 1
            
    for key in socialDict:
        print("Social network {0} is {1}".format(key, socialDict[key]))

numStudents = 5
listTuples = [(0,1), (1,2), (3,4), (4,6)]
network(numStudents, listTuples)