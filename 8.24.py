"""
Implement a class Polygon that abstracts regular polygons and supports class methods:
• __init__(): A constructor that takes as input the number of sides and the side
length of a regular n-gon (n-sided polygon) object
• perimeter(): Returns the perimeter of n-gon object
• area(): returns the area of the n-gon object
Note: The area of a regular polygon with n sides of length s is
(s^2 * n) / 4tan( π/n )
>>> p2 = Polygon(6, 1)
>>> p2.perimeter()
6
>>> p2.area()
2.5980762113533165
"""
import math

class Polygon:
    'class that accepts polygons'
    
    def __init__(self, numSides=0, sideLength=0):
        'initlize polygon numSides and sideLength'
        self.numSides = numSides
        self.sideLength = sideLength

    def perimeter(self):
        'returns perimeter of polygon'
        print(self.numSides * self.sideLength)
    
    def area(self):
        'returns area of polygon'
        intermediate = 4 * math.tan(math.pi / self.numSides)
        print(self.numSides * math.pow(self.sideLength, 2) / intermediate)
    
p2 = Polygon(6, 1)
p2.perimeter()
p2.area()