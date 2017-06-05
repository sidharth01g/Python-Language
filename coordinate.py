class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coordinate: " + str(self.__dict__)


def plus(c1, c2):
    return Coordinate(c1.x + c2.x, c1.y + c2.y)


def minus(c1, c2):
    return Coordinate(c1.x - c2.x, c1.y - c2.y)


c0 = Coordinate(0, 0)
print dir(c0)
print c0.__repr__()

p1 = Coordinate(10, 40)
p2 = Coordinate(50, 60)

p3 = minus(p2, p1)
print p3.__repr__()
