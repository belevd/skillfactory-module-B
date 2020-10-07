import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, a):
        self.a = a

    def getAreaSquare(self):
        return self.a ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getAreaCircle(self):
        return round(self.radius ** 2 * math.pi, 2)