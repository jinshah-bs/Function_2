# print "hai bro"
# x = 5/0
# lis = [20, 12, 25, 30]
# lis[10]
# lis + 35
# c = 'b'
# d = {'a':20, 'b':30, 'c':80}
# d['e']
# print(x)
# lis.add
# class EvenIntList(list):
#     def append(self, value):
#         if not isinstance(value, int):
#             raise TypeError("Only integer value can be appended")
#         if value % 2 != 0:
#             raise ValueError("Only even numbers can be appended")
#         super().append(value)
#
#
# el = EvenIntList()
# el.append(2)
# el.append(6)

# def check_exception():
#     print("This is the first line in function")
#     print("Second line of function")
#     raise Exception("This is an exception")
#     print("First line after exception")
#     print("Second line after exception")


# def outer_func():
#     print("first line of outer func")
#     check_exception()
#     print("Line after calling the exeption function")
#     print("______________________________")

# outer_func()
# try:
#     check_exception()
# except:
#     print("Success -  I have bypassed the exception")

try:
    x = 5/0
except ZeroDivisionError:
    print("Denominator cant be zero")
except TypeError:
    print("Check the denominator type")

# def getvalue(d, e):
#     try:
#         return d['e']
#     except KeyError:
#         return 0
#
# d = {'a':20, 'b':30, 'c':80}
#
# print(getvalue(d,'e'))