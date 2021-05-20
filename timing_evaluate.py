import timeit

max_value = 10000000
min_valid = 10
max_valid = 9999997

data_list1 = list(range(max_value))
data_list2 = list(range(max_value))

def sanitise_1(data):
    # process the low values in the list
    stop = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break

    del data[:stop]

    start = 0
    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
            # We have the index of last item to keep.
            # Set 'start' to the position of the first
            # item to delete, which is 1 after 'index'.
            start = index + 1
            break

    del data[start:]


def sanitise_2(data):
    top_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
            del data[top_index - index]


def sanitise_3(data):
    for index in range(len(data) - 1, -1, -1):
        if data[index] < min_valid or data[index] > max_valid:
            del data[index]


if __name__ == "__main__":
    print("Timing")
    x = timeit.timeit("sanitise_1(data_list1)",
                      setup="from __main__ import sanitise_1,"
                            "data_list1",
                      number=1)
    print("{:15.15f}".format(x))
    y = timeit.timeit("sanitise_2(data_list2)",
                      setup="from __main__ import sanitise_2,"
                            "data_list2",
                      number=1)
    print("{:15.15f}".format(y))