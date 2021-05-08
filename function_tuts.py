# def func(a, b, c, d=5.0):
#     print("{}, {}, {}".format(a,b,c))
#     print("{}".format(d))

# func(10.0, 2.0, 3.2, 100.0)

# def func(*args):
#     print(args)
#     for item in args:
#         print(item)
# def sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# func(1,2,3,4,5,6,7,8,9)
# print(sum(1))
#
# def func2(**kwargs):
#     print(kwargs)
#
#
# func2(key1=10.0, key2=5.0, key3=25)

# print(1,2,3,4,5, sep=' ; ')

#1st positional args, 2nd var-positional, 3rd keword only, 4th var-keword

def func(a: int, b: int, c:int, *args, d: float =25.0, **kwargs)->None:
    """
    this function print the various argument types
    Args:
        a: positional
        b: positional
        c: positiona
        *args: var-positional
        d: keyword, default is 25.0
        **kwargs: var-keyword

    Returns: not returning anything

    """
    print("The positional args are {},{},{}".format(a,b,c))
    print("The var-positional args are {}".format(args))
    print("The kw argument is {}".format(d))
    print("The var-kw argument is {}".format(kwargs))

func(1, 2, 3, 7, 8, 9, 10.0, d=11.0, e=[2,2], key1='hjg', key2=False)
