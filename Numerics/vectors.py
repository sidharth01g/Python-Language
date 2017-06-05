class Vector2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # For "+" operator
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):  # inclusive add : "+=" oparator
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):  # For "-" operator
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):  # inclusive add : "-=" oparator
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):  # For "*" operator
        return Vector2D(self.x * other.x, self.y * other.y)

    def __imul__(self, other):  # inclusive add : "*=" oparator
        self.x *= other.x
        self.y *= other.y
        return self

    def show(self):
        print(str(self.x) + ", " + str(self.y) )


v1 = Vector2D(20, 30)
v2 = Vector2D(10, 10)
(v1 + v2).show()
v1 += v2
v1.show()
(v1 - v2).show()
v2 -= v1
v2.show()
v2 *= v2
v2.show()
