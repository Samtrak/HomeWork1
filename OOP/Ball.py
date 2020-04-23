class Ball:
    def __init__(self, x, y, radius, xDelta, yDelta):
        self.x = x
        self.y = y
        self.radius = radius
        self.xDelta = xDelta
        self.yDelta = yDelta

    def __str__(self):
        return "Ball[(" + str(self.x) + "," + str(self.y) + "),speed(" + \
               str(self.xDelta) + "," + str(self.yDelta) + \
               ")]"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadius(self):
        return self.radius

    def getXDelta(self):
        return self.xDelta

    def getYDelta(self):
        return self.yDelta

    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def setRadius(self, newRadius):
        self.radius = newRadius

    def setXDelta(self, newXDelta):
        self.xDelta = newXDelta

    def setYDelta(self, newYDelta):
        self.yDelta = newYDelta

    def move(self):
        self.x += self.xDelta
        self.y += self.yDelta

    def reflectVertical(self):
        self.yDelta -= self.yDelta

    def reflectHorizontal(self):
        self.xDelta -= self.xDelta


ball = Ball(0,0, 1, 0.5, 0.5)
print(ball)
ball.move()
print(ball)