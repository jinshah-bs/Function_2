with open("table.text", "w") as new_file:
    a = "*"
    print("     TABLES  ", file=new_file)
    print("", file=new_file)
    for i in range(1, 13):
        for j in range(1, 17):
            print("{0:>2} times {1} is {2}".format(j, i, i*j), file=new_file)
        print("{}".format(a*20), file=new_file)

with open("table.text", "a") as new_file2:
    print(" ", file=new_file2)
    print("      Squares", file=new_file2)
    print("", file=new_file2)
    for i in range(1, 13):
        print("{0:>2} square is {1:>3}".format(i, i*i), file=new_file2)
    print("{}".format(a*20), file=new_file2)