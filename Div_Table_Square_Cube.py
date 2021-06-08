with open('tables_square_cube.txt', 'w') as document:
    a="**"
    for i in range(1,16):
        print("{} Table".format(i),file=document)
        print('',file=document)
        for j in range (1,16):
            print('{:>2} times {} is {:^3}'.format(j,i, i*j),file=document)
        print('',file=document)
        print(a*10,file=document)
    print('',file=document)


with open ('tables_square_cube.txt', 'a') as document1:
    print('Squares', file=document1)
    print('',file=document1)
    for i in range (1,21):
        print('{:>2} Square is {:>3}'.format(i,i**2), file=document1)
    print('',file=document1)
    print(a*10,file=document1)


with open('tables_square_cube.txt', 'a') as document2:
    print('Cubes', file=document2)
    print('',file=document2)
    for i in range(1,21):
        print('{} Cube is {:>4}'.format(i, i**3), file=document2)
    print(a*10,file=document2)