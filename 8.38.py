"""
8.38 A stack is a sequence container type that, like a queue, supports very restrictive access
methods: All insertions and removals are from one end of the stack, typically referred to as
the top of the stack. Implement container class Stack that implements a stack. It should be
a subclass of object, support the len() overloaded operator, and support the methods:
• push(): Take an item as input and push it on top of the stack
• pop(): Remove and return the item at the top of the stack
• isEmpty(): Return True if the stack is empty, False otherwise
A stack is often referred to as a last-in first-out (LIFO) container because the last item
inserted is the first removed. The stack methods are illustrated next.
>>> s = Stack()
>>> s.push('plate 1')
>>> s.push('plate 2')
>>> s.push('plate 3')
>>> s
['plate 1', 'plate 2', 'plate 3']
>>> len(s)
3
>>> s.pop()
'plate 3'
>>> s.pop()
'plate 2'
>>> s.pop()
'plate 1'
>>> s.isEmpty()
True
"""

class Stack:
    """
    Implements a LIFO stack object
    Methods: __init__, push, pop, isEmpty, overloaded len()
    """

    def __init__(self):
        """
        Initialize empty stack object
        """
        self._stack = []

    def push(self, element):
        """
        Push element onto the stack
        Element must be string
        """
        self._stack.append(element)

    def pop(self):
        """
        Remove and return element from the stack LIFO order
        """
        if self.isEmpty():
            raise IndexError("Cannot remove from empty stack")
        else:
            print(self._stack.pop())

    def isEmpty(self):
        """
        Checks if stack object is empty. returns true if empty
        """
        return len(self._stack) == 0

    def __len__(self):
        """
        Overides length operator and returns length
        """
        return len(self._stack)
    
    def __str__(self):
        """
        Cananonical string representation
        """
        return str(self._stack)
    
s = Stack()
s.push('plate 1')
s.push('plate 2')
s.push('plate 3')
print(s)
print(len(s))
s.pop()
s.pop()
s.pop()
print(s.isEmpty())