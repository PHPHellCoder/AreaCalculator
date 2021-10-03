"""
Ten program oblicza obszar trójkąta z trzech punktów na płaszczyźnie współrzędnych
"""

import math
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, a, b, c):
        self.point_a = a
        self.point_b = b
        self.point_c = c
        self.height_a = None
        self.height_b = None
        self.height_c = None
        self.calc_heights()
        self.length_ab = math.sqrt((self.point_a.x - self.point_b.x)**2 + (self.point_a.y - self.point_b.y)**2)
        self.length_ac = math.sqrt((self.point_a.x - self.point_c.x)**2 + (self.point_a.y - self.point_c.y)**2)
        self.length_bc = math.sqrt((self.point_b.x - self.point_c.x)**2 + (self.point_b.y - self.point_c.y)**2)
        self.s = (self.height_b * self.length_ac) / 2

    def calc_heights(self):
        straight = Straight()
        straight.calc_equation(self.point_c, self.point_b)
        self.height_a = self.calc_length(straight, self.point_a)
        straight.calc_equation(self.point_a, self.point_c)
        self.height_b = self.calc_length(straight, self.point_b)
        straight.calc_equation(self.point_a, self.point_b)
        self.height_c = self.calc_length(straight, self.point_c)

    def update_points(self, a, b, c):
        self.point_a = a
        self.point_b = b
        self.point_c = c
        self.calc_heights()
        self.length_ab = math.sqrt((self.point_a.x - self.point_b.x) ** 2 + (self.point_a.y - self.point_b.y) ** 2)
        self.length_ac = math.sqrt((self.point_a.x - self.point_c.x) ** 2 + (self.point_a.y - self.point_c.y) ** 2)
        self.length_bc = math.sqrt((self.point_b.x - self.point_c.x) ** 2 + (self.point_b.y - self.point_c.y) ** 2)
        self.s = (self.height_a * self.length_bc) / 2

    def calc_length(self, straight, point):
        return abs(straight.A*point.x + straight.B*point.y + straight.C) / math.sqrt(straight.A**2 + straight.B**2)

    def print_area(self):
        print('Triangle\'s area:', self.s)


class Straight:
    def __init__(self):
        self.a = None
        self.b = None
        self.A = None
        self.B = None
        self.C = None

    def calc_equation(self, point1, point2):
        self.a = (point1.y - point2.y) / (point1.x - point2.x)
        self.b = point1.y - self.a*point1.x
        self.A = -self.a
        self.B = 1
        self.C = -self.b


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


data = []
coord_x = int(input('x coordinate of point A: '))
coord_y = int(input('y coordinate of point A: '))
pointA = Point(coord_x, coord_y)
data.append((pointA.x, pointA.y))
coord_x = int(input('x coordinate of point B: '))
coord_y = int(input('y coordinate of point B: '))
pointB = Point(coord_x, coord_y)
data.append((pointA.x, pointA.y))
coord_x = int(input('x coordinate of point C: '))
coord_y = int(input('y coordinate of point C: '))
pointC = Point(coord_x, coord_y)
data.append((pointA.x, pointA.y))
triangle = Triangle(pointA, pointB, pointC)
triangle.print_area()

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([triangle.point_a.x, triangle.point_b.x], [triangle.point_a.y, triangle.point_b.y])
ax.plot([triangle.point_b.x, triangle.point_c.x], [triangle.point_b.y, triangle.point_c.y])
ax.plot([triangle.point_a.x, triangle.point_c.x], [triangle.point_a.y, triangle.point_c.y])
plt.show()
