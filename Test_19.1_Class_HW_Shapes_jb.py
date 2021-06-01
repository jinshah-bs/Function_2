import math


class Shapes:

    def __init__(self, name, a, b=1.0):
        self.name = name
        self.dim1 = a
        self.dim2 = b
        self.area = 0
        self.perimeter = 0
        self.calc_prop()

    def calc_prop(self):

        if self.name.casefold() == "circle":
            self.area = math.pi * math.pow(self.dim1, 2) * (self.dim2 / 360)
            self.perimeter = 2 * math.pi * self.dim1 * (self.dim2 / 360)

        elif self.name.casefold() == "square":
            self.area = self.dim1 * self.dim1
            self.perimeter = 2 * (self.dim1 + self.dim1)

        elif self.name.casefold() == "rectangle":
            self.area = self.dim1 * self.dim2
            self.perimeter = 2 * (self.dim1 + self.dim2)

    def print_prop(self):

        print("The area of the given {0} is {1:.1f}".format(self.name, self.area))
        print("The perimeter of the given {0} is {1:.1f}".format(self.name, self.perimeter))


# circle = Shapes("circle", 10.0,360)
# circle.print_prop()
semicircle = Shapes("Circle", 10.0, 180)
semicircle.print_prop()
print()
# qua_circle = Shapes("Circle", 10.0,90)
# qua_circle.print_prop()
square = Shapes("square", 10.2)
square.print_prop()
print()
rect = Shapes("Rectangle", 20.5, 10.4)
rect.print_prop()
print()





