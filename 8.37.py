"""
Chapter 8 Problems 303
8.37 Implement the container class Stat that stores a sequence of numbers and provides
statistical information about the numbers. It supports an overloaded constructor that initial-
izes the container and the methods shown.
>>> s = Stat()
>>> s.add(2) # adds 2 to the Stat container
>>> s.add(4)
>>> s.add(6)
>>> s.add(8)
>>> s.min() # returns minimum value in container
2
>>> s.max() # returns maximum value in container
8
>>> s.sum() # returns sum of values in container
20
>>> len(s) # returns number of items in container
4
>>> s.mean() # returns average of items in container
5.0
>>> 4 in s # returns True if in the container
True
>>> s.clear() # Empties the sequence
"""

class Stat:

    def __init__(self, data=None):
        """
        Initialize stat container
        data (optional, list)
        """

        if data is None:
            #initialize to empty list if no input data
            self._data = []
        else:
            #if not every element is an integer or float, raise an error
            if not all(isinstance(n, (int, float)) for n in data):
                raise TypeError("All elements in data must be integers or floats")
            else:
                #forces input into a list
                self._data = list(data)

    def add(self, num):
        """
        adds a number to the list
        """
        #if num is not an int or float, raise an error, else add to list
        if not isinstance(num, (int, float)):
            raise TypeError("ELement needs to be an int or float")
        else:
            self._data.append(num)

    def min(self):
        """
        uses lsit method to find minimum
        """

        #if self._data is None return None
        if self._data is None:
            return None
        else:
            print(min(self._data))
        
    def max(self):
        """
        Uses list method to find maximum
        """

        #if self.data is None return None
        if self._data is None:
            return None
        else:
            print(max(self._data))
        
    def sum(self):
        """
        adds all numbers in container
        """

        #sum nubers using list method
        print(sum(self._data))
    
    def __len__(self):
        """
        Overloads the __len__ function
        """
        return len(self._data)
        
    def __contains__(self, key):
        """
        overloads in operator
        """
        return key in self._data

    def __clear__(self):
        return clear(self._data)

s = Stat()
s.add(2) # adds 2 to the Stat container
s.add(4)
s.add(6)
s.add(8)
s.min()
s.max()
s.sum()
print(len(s))
#s.mean()
print(4 in s)
print(s.clear())