class Rectangle:

    def __init__(self, length, bredth):
        self.l = length
        self.b = bredth

    def area(self):
        Area = 0;
        Area += self.l * self.b
        return Area

    def perimeter(self):
        return 2.0*(self.l + self.b)


Rec1 = Rectangle(10, 20)
Rec2 = Rectangle(5, 2.3)
Area1 = Rec1.area()
Per2 = Rec2.perimeter()
print(Area1, Per2)
#
# A = list()
# A.append(10)
# A.append(15)
#
# B = list()
# B.append(25)

