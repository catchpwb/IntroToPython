"""
8.39 Write a container class called PriorityQueue. The class should supports methods:
• insert(): Takes a number as input and adds it to the container
• min(): Returns the smallest number in the container
• removeMin(): Removes the smallest number in the container
• isEmpty(): Returns True if container is empty, False otherwise
The overloaded operator len() should also be supported.
>>> pq = PriorityQueue()
>>> pq.insert(3)
>>> pq.insert(1)
>>> pq.insert(5)
>>> pq.insert(2)
>>> pq.min()
1
>>> pq.removeMin()
>>> pq.min()
2
>>> pq.size()
3
>>> pq.isEmpty()
False
"""

class PriorityQueue:
    """
    
    """

    def __init__(self):
        self._pqueue = []

    def insert(self, element):
        if not isinstance(element, (int)):
            raise TypeError("Must be an integer")
        else:
            self._pqueue.append(element)

    def min(self):
        return min(self._pqueue)

    def removeMin(self):
        minimum = self.min()
        print(minimum)
        return self._pqueue.remove(minimum)

    def isEmpty():
        pass

    def __len__(self):
        return len(self._pqueue)
    

pq = PriorityQueue()
pq.insert(3)
pq.insert(1)
pq.insert(5)
pq.insert(2)
print(pq.min())
pq.removeMin()
pq.min()
pq.size()
pq.isEmpty()