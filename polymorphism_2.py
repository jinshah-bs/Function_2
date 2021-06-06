import math

class Data:
    """
    This class saves the data associated with the shape
    r = radius
    theta = angle in degree
    l = length
    b = breadth
    a = side of a square
    """

    def __init__(self, **kwargs):
        if self.shape == "Square":
            self.a = kwargs.get('a', 0)
        elif self.shape == "Rectangle":
            self.b = kwargs.get('b', 0)
            self.l = kwargs.get('l', 0)
        else:
            self.r = kwargs.get('r', 0)
            self.theta = kwargs.get('theta', 360)


class Square(Data):
    shape = 'Square'

    def area(self):
        print("Area of the square is {}".format(self.a ** 2))

    def perimeter(self):
        print("Perimeter of the square is {}".format(self.a * 4))


class Circle(Data):
    shape = "Circle"

    def area(self):
        a = self.theta * math.pi * math.pow(self.r, 2) / 360
        print("Area of the circle is {}".format(a))

    def perimeter(self):
        p =2 * math.pi * self.r * self.theta / 360
        print("Perimeter of the circle is {}".format(p))


class Rectangle(Data):
    shape = 'Rectangle'

    def area(self):
        print("Area of the rectangle is {}".format(self.l * self.b))

    def perimeter(self):
        print("Perimeter of the Rectangle is {}".format(2 * (self.l + self.b)))


c1 = Circle(r=10)
c2 = Circle(r=10, theta=180)
c1.area()
c1.perimeter()
print()
c2.area()
c2.perimeter()

# print(hasattr(c1, 'l'))
print(isinstance(c1, Data))
