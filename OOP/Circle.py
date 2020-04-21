import math

class Circle:
    def __init__(self, radius = 1.0, color = "red"):
        self.radius = radius
        self.color = color

    def __str__(self):
        return "Circle[" + \
               "radius=" + str(self.radius) + "," + \
               "color=" + self.color + \
               "]"

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def setRadius(self, newRadius):
        self.radius = newRadius

    def setColor(self, newColor):
        self.color = newColor

    def getArea(self):
        return math.pi * self.radius * self.radius


circle1 = Circle()
circle2 = Circle(3.5)
circle3 = Circle(5.4, 'green')

print(circle1)
print(circle2)
print(circle3)

print(circle3.getArea())
print(circle2.getArea())
print(circle1.getArea())