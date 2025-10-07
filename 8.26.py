'''8.26 Create a class Segment that represents a line segment in the plane and supports
methods:
• __init__(): Constructor that takes as input a pair of Point objects that represent
the endpoints of the line segment
• length(): Returns the length of the segment
• slope(): Returns the slope of the segment or None if the slope is unbounded
>>> p1 = Point(3,4)
>>> p2 = Point()
>>> s = Segment(p1, p2)
>>> s.length()
5.0
>>> s.slope()
0.75'''

import math

class Point:
    'class that represents a point in the plane'
    def __init__(self, xcoord=0, ycoord=0):
        'initializes point coordinates to (xcoord, ycoord)'
        self.x = xcoord
        self.y = ycoord
 
    def setx(self, xcoord):
        'sets x coordinate of point to xcoord'
        self.x = xcoord
    def sety(self, ycoord):
        'sets y coordinate of point to ycoord'
        self.y = ycoord
    def get(self):
        'returns the x and y coordinates of the point as a tuple'
        return (self.x, self.y)
    def move(self, dx, dy):
        'changes the x and y coordinates by i and j, respectively'
        self.x += dx
        self.y += dy
    def __eq__(self, other):
        'self == other is they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'

class Segment:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def length(self):
        ycoords = p2.y - p1.y
        xcoords = p2.x - p1.x
        squaredLength = ycoords**2 + xcoords**2
        print(math.sqrt(squaredLength))

    def slope(self):
        rise = p2.y - p1.y
        run = p2.x - p1.x
        print(rise / run)

p1 = Point(3,4)
p2 = Point()
s = Segment(p1, p2)
s.length()
s.slope()