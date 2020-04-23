import math

class Circle:
    def __init__(self, radius=1.0, color="red"):
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


# circle1 = Circle()
# circle2 = Circle(1.5)
# circle3 = Circle(2.4, 'yellow')
#
# print(circle1)
# print(circle2)
# print(circle3)
#
# print(circle3.getArea())
# print(circle2.getArea())
# print(circle1.getArea())


class Cylinder(Circle):
    def __init__(self, radius = 1.0, color="red", height=1.0):
        Circle.__init__(self, radius, color)
        self.height = height

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getVolume(self):
        return math.pi * self.height * self.radius ** 2

    def __str__(self):
        return "Cylinder" + "your solution"
        # Cylinder[radius=?,color=?,height=?]


cylinder1 = Cylinder()
cylinder2 = Cylinder(1.0)
cylinder3 = Cylinder(1.0, "green")
cylinder4 = Cylinder(1.0, "green", 2.5)
print(cylinder1)