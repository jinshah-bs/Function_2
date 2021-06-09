# new_file = open('E:\Books\sample.txt','r')
#
# for line in new_file:
#     print(line, end='')
#
# new_file.close()

# with open('sample.txt', 'r') as new_file:
#     for line in new_file:
#         print(line, end='')

# with open('sample.txt', 'r') as new_file:
#     for line in new_file:
#         if 'CUCKOO' in line.upper():
#             print(line, end='')

# with open('sample.txt', 'r') as new_file:
#     line = new_file.readline()
#     while line:
#         print(line, end='')
#         line = new_file.readline()

with open('sample.txt', 'r') as new_file:
    lines = new_file.readlines()

print(lines)
for line in lines:
    print(line, end='')
