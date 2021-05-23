# print("Hello")
lists = [1, 5, 8, 0, 45]
sorte_list = sorted(lists, reverse=True)


# print(sorte_list)
# lists.sort()

# def addition(x, y, k):
#     b = 11
#     sum_num = x + y*k + b
#     print(sum_num)
#     print("b within the function is {}".format(b))
#     return sum_num
#
# a = 10.0
# b = 3.0
# number = addition(a, b, 25)
# print(number)
# print("b outside the function is {}".format(b))

# def is_palinadrome(string):
#     rev_string = string[::-1]
#     return rev_string.casefold() == string.casefold()
#
# def is_sen_paliandrome(string):
#     name = ''
#     for char in string:
#         if char.isalnum():
#             name  += char
#     return is_palinadrome(name)
#
#
# name = str(input("Enter something: "))
# if is_sen_paliandrome(name):
#     print(f"The name {name} is a plaientrome")
# else:
#     print("Get lost")

def addition(x:float, y:float)-> float:
    """
    This function will add two numbers and return the sum
    :param x: any 'float' value
    :param y: any 'float' value
    :return: the sum which is a 'float'
    """
    return x + y


a = 10.0
b = 3.0
sum = addition(a, b)
print(sum)
