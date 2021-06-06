# def func(a):
#     try:
#         return 10/a
#     except:
#         return 0
#
# print("It is worked {}".format(func(0)))
# print(Hello_dear)
# import random
#
# except_list = [TypeError, NameError, AttributeError, SyntaxError, None]
#
# try:
#     expt = random.choice(except_list)
#     print("raising the {}".format(expt))
#     if expt:
#         raise expt("An error")
# except TypeError:
#     print("Type error")
# except NameError:
#     print("Name error")
# except AttributeError:
#     print("Attribute error")
# except SyntaxError:
#     print("syntax error")
# else:
#     print("There is no exception")
# finally:
#     print("This will be always executed")

class InvalidWithdrowal(Exception):
    pass

raise InvalidWithdrowal("You have too much than you have")
