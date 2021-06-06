# print(len('Jinshah'))
# print(len([1, 2, 3, 4, 5]))
#
#
# def func(a, b, c=0):
#     return a * b + c
#
#
# print(func(10, 20))
# print(func(10, 20, 5))
# def printloop(n):
#     for num in n:
#         print(num)
#
# printloop(range(10))
# printloop(range(5, 10))
# printloop(range(5, 10, 2))

print(1 + 2)
print('jin' + 'shah')

# Method overloading
# class addition:
#
#     def sum(self, a=0, b=0, c=0, d=0, e=0):
#         s = 0
#         s = a + b + c + d + e
#         return s
#
#
# s = addition()
#
# print(s.sum())
# print(s.sum(1))
# print(s.sum(1,2,3,4,5))

# Operator overloading
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class CoOrdinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        X = self.x + other.x
        Y = self.y + other.y
        s3 = CoOrdinate(X, Y)
        return s3


comp = Complex(2 , 3)
c1 = CoOrdinate(0, 4)
c2 = CoOrdinate(5, 6)
c3 = c1 + comp
print(c3.x, c3.y)

#method overriding

class Parent:
    def print1(self):
        print('This is parent')

    def print2(self):
        print('This is another print in parent')


class Child(Parent):
    def print2(self):
        print("This is the overriden method in child")


obj_c = Child()
obj_p = Parent()

obj_p.print2()
obj_c.print2()

obj_p.print1()
obj_c.print1()
