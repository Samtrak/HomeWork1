class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{" + str(self.x) + ":" + str(self.y) + "}"


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def __str__(self):
        result = "["
        for item in self.data:
            result += str(item) + ","

        result += "]"
        return result


canta = Bag()
canta.add("kitap")
canta.add("gozluk")
canta.addtwice("kalem")
print(canta)









