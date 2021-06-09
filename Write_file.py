# scholars = ['jinshah', 'Kottala', 'Jayabalaganesh', 'Divakar', 'Dinesh']
#
# with open('scholar.txt', 'w') as new_file:
#     for scholar in scholars:
#         # new_file.write(scholar)
#         print(scholar, file=new_file, flush=True)

# mech_scholar = []
# with open('scholar.txt', 'r') as new_file:
#     for name in new_file:
#         mech_scholar.append(name.strip('\n'))
#
# print(mech_scholar)

# muthalvan = ('ARR', 2000, ('song1', 'song2', 'song3'))
#
# with open('film.txt', 'w') as new_file:
#     print(muthalvan, file=new_file)

# with open('film.txt', 'r') as new_file:
#     content = new_file.readlines()
#
# print(content)
#
# film = eval(content[0])
# print(film)
# composer, year, songs = film
# print(composer)
# print(year)
# print(songs)

# scholars = ['Midhun', 'Solai', 'Cyril', 'Micheal']

# with open('scholar1.txt', 'x') as new_file:
#     for scholar in scholars:
#         # new_file.write(scholar)
#         print(scholar, file=new_file, flush=True)

another_scholar = ['Vishnu', 'rahul', "Aravind", 'Phunny']

with open('scholar.txt', 'a') as new_file:
    for scholar in another_scholar:
        print(scholar, file=new_file)