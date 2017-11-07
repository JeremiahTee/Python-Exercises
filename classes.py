class Vector:
    def __init__(self, x, y): #constructor
        self.x = x
        self.y = y

    #two methods
    def add(self, other):
        if type(self) != type(other):
            raise TypeError("Cannot add types Vector %s" % type(other))
        return Vector(self.x + other.x, self.y + other.y)

    def mul(self, other):
        if type(self) != type(other):
            raise TypeError("Cannot add types Vector and %s" % type(other))
        return Vector(self.x * other.x, self.y * other.y)

    