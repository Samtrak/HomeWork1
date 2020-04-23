class Rectangle:
    def __init__(self, width=1.0, length=1.0):
        self.width = width
        self.length = length

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def setLength(self, newLength):
        self.length = newLength

    def setWidth(self, newWidth):
        self.width = newWidth

    def __str__(self):
        return "{width = " + str(self.width) + \
               ", length=" + str(self.length) + "}"

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return self.width * 2 + self.length * 2


# ============== using classes =====================
nesne1 = Rectangle()
nesne2 = Rectangle(3.0, 4.5)

print(nesne1.getLength())
print(nesne1.getWidth())

print(nesne2.getLength())
print(nesne2.getWidth())

nesne1.setWidth(5)
nesne1.setLength(2.0)

##print(nesne1.getWidth())
##print(nesne1.getLength())
print(nesne1)
print(nesne2)

print(nesne1.getArea())
print(nesne1.getPerimeter())






