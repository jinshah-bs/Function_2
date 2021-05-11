# lists = [1, 2, 3, 4, 5, 5]
#
# for item in lists:
#     print(item)

# automobiles = {"4 wheels": "It is a car",
#                "3 wheels": "It is an auto",
#                "2 wheels": "It is a bike",
#                "6 wheel ": "A bus or a truck",
#                }
# print(automobiles)
# print(automobiles["3 wheels"])
#
# for item in automobiles:
#     print(item + ";" + automobiles[item])
#
# auto_tuple = tuple(automobiles.items())
# print(auto_tuple)
# for item in auto_tuple:
#     key, value = item
#     print(key + ";" + value)
#
# auto_dict = dict(auto_tuple)
# print(auto_dict)

# keys = list(automobiles.keys())
# keys.sort()
# keys = sorted(automobiles.keys())
# print(keys)
# for item in keys:
#     print(item + ";" + automobiles[item])
#
# for item in sorted(automobiles.keys()):
#     print(item + " ; " + automobiles[item])
#
# print(automobiles.keys())
# print(automobiles.values())

# dome_animals = {
#     "cow": "gives milk",
#     "goat": "gives mutton",
#     "cat": "eats rat",
#     "dog": "bark",
# }
# print(dome_animals)
# # for item in sorted(dome_animals.keys()):
# #     print(item + " ; " + dome_animals[item])
#
# dome_animals["horse"] = "We can ride"
# dome_animals["cow"] = "It s a nice animal"
# print(dome_animals)
#
# del dome_animals["cat"]
# print(dome_animals)
#
# dome_animals.clear()
# print(dome_animals)

# classic = {
#     "puffs": "cruchy and tasty",
#     "biscut": "Its super crispy",
#     "meat roll": "Its masala",
#     "cake": "It wont be good",
#     "coffee": "Its nice filter coffee",
#     "tea": "Tea is not good"
# }
#
# while True:
#     item = input("Please enter the dish you like to order, quit for escape: ")
#     if item.casefold()=='quit':
#         break
#     print("The item {} you you ordered, {}".format(item, classic.get(item.casefold(),"Sorry the item " + item +" is not here")))
    # if item in classic:
    #     print("The item {} you you ordered, {}".format(item, classic[item.casefold()]))
    # else:
    #     print("Sorry the item, {} you order is not here".format(item))

# set1 = {1, 2, 3, 4, 8, 41, 51, 4}
# print(set1)
#
# newlist = list(set1)
# print(newlist)
#
# list1 = [2, 4, 6, 8, 10, 12]
# list2 = [4, 16, 36, 64, 100, 144]
#
# even = set(list1)
# squares = set(list2)
#
# print(even)
# print(squares)
#
# print(even.union(squares), len(even.union(squares)))
# print(squares.union(even))
#
# print(even.intersection(squares))
#
# even.add(0)
# print(even)

# name = {} # this will create an empty dict instead of set
# name = set()
# name.add("divakar")
# print(name)
name = {"Jinshah", "Divakar", "JB", "Dinesh", "Kottala", "Peter"}

print(name)
name.remove("Peter")
print(name)
name.discard("Peter")

