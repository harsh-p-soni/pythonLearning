"""
Object Oriented Programming

Homework Assignment
Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
"""
import math


class Line():
    def __init__(self, first_coordinate, second_coordinate):
        self.x1 = first_coordinate[0]
        self.y1 = first_coordinate[1]
        self.x2 = second_coordinate[0]
        self.y2 = second_coordinate[1]

    def distance(self):
        print((((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** 0.5)

    def slope(self):
        print((self.y2 - self.y1) / (self.x2 - self.x1))


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)


li.distance()
li.slope()


"""
Problem 2
"""


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.r = radius
        self.h = height

    def volume(self):
        return 3.14 * (self.r ** 2) * self.h

    def surface_area(self):
        return (2 * 3.14 * self.r * self.h) + (2 * 3.14 * self.r ** 2)


c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())

