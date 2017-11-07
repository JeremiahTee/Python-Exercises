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
            raise TypeError("Cannot multiply types Vector and %s" % type(other))
        return Vector(self.x * other.x, self.y * other.y)

    # dunder methods to overload add, mul
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Cannot add types Vector and %s" % type(other))
        return self.x + other.x, self.y + other.y

    def __iadd__(self, other):
        if type(self) != type(other):
            raise TypeError("Cannot add types Vector and %s" % type(other))
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, other):
        if type(self) != type(other):
            raise TypeError("Cannot multiply types Vector and %s" % type(other))
        return self.x * other.x + self.y * other.y

    def __eq__(self, other):
        if type(self) != type(other):
            raise TypeError("Cannot compare types Vector and %s" % type(other))
        return self.x == other.x, self.y == other.y

    def __div__(self, num):
        if not isinstance(num, int):
            raise TypeError("Cannot divided types Vector and %s" % type(num))
        return self.x / num.x, self.y / num.y

    def __mul__(self, other):
        if isinstance(other, int):
            self.x *= other
            self.y *= other
            return self
        else:
            return self.x * other.x + self.y * other.y

    def __str__(self):
        return '(%g,%g)' % (self.x, self.y)

    def __repr__(self):
        return ("Vector({%g},{%g})" % (self.x, self.y))

vec = Vector(1,2)
print(str(vec))
print(str(vec.add(Vector(1,1))))
print(str(vec.mul(Vector(3,4))))
print(str(vec.__mul__(2)))