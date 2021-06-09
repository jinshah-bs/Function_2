# import sys
#
# def my_range(start: int, stop: int, step = 1):
#     # print("range function started")
#     if start > stop:
#         raise RuntimeError("Start should be less that stop")
#     i = start
#     while i < stop:
#         yield i
#         # print(f'The value yielded is {i}')
#         i += step
#
# trial_range = range(10)
# # trial_range = my_range(0, 10)
# # print("This is line 15")
#
# trial_list = []
# #
# # print(next(trial_range))
# # print(next(trial_range))
# # print(next(trial_range))
# # print(next(trial_range))
# # print(next(trial_range))
# # print(next(trial_range))
#
# for index in trial_range:
#     # print("Ya we got it **********************")
#     trial_list.append(index)
# # trial_range = my_range(0, 10)
# trial_list1 = []
# for index in trial_range:
#     trial_list1.append(index)
#
# # print(type(trial_range))
# print(trial_list)
# print('*'*10)
# print(trial_list1)
#
# # print("The size of the list is {} b".format(sys.getsizeof(trial_list)))
# # print("The size of the range is {} b".format(sys.getsizeof(trial_range)))

# fibonacci series

# def fibonacci_gen():
#     current, previous = 0, 1
#     while True:
#         yield current
#         current , previous = current + previous, current
#
# fibonacci = fibonacci_gen()
#
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
# # print(next(fibonacci))
#
# for index in range(50):
#     print(next(fibonacci))

## Pi value estimation

def odd_gen():
    num = 1
    while True:
        yield num
        num += 2


def est_pi():
    nxt_odd_num = odd_gen()
    pi = 0
    while True:
        pi += 4/next(nxt_odd_num)
        yield pi
        pi -= 4/next(nxt_odd_num)
        yield pi


pi_val = est_pi()

pival = []
for index in range(100):
    # print(next(pi_val))
    pival.append(next(pi_val))


