print('welcome to unit converter')
conv=int(input('''select the type of conversion
           enter 1 for temperature
           enter 2 for pressure
           enter 3 for length '''))
if conv==1:
    print('welcome to temperature converter')
    temp=str(input('enter the value and unit "WITH A SPACE IN BETWEEN" to be converted e.g 2 K 2 C or 2 F '))
    if temp[len(temp)-1].casefold() == "k":
        x=temp.split()
        a,b=x
        z=float(a)
        C= z-273.15
        F= (z-273.5)*9/5+32
        print('{} K can be expressed as {:.2f} C or {:.2f} F'.format(z, C, F))
    elif temp[len(temp)-1].casefold() == "c":
        x=temp.split()
        a,b=x
        z=float(a)
        K=z+273.15
        F=z*9/5+32
        print('{} C can be expressed as {:.2f} K or {:.2f} F'.format(z, K, F))
    elif temp[len(temp)-1].casefold() == "f":
        x=temp.split()
        a,b=x
        z=float(a)
        C=(z-32)*5/9
        K=(z-32)*(5/9)+273.15
        print('{} F can be expressed as {:.2f} K or {:.2f} C'.format(z, K, C))
    else:
        print('check ur entered value')

elif conv==2:
    print('welcome to pressure converter')
    press=str(input('enter the value and unit "WITH A SPACE IN BETWEEN" to be converted e.g 2 P 2 B or 2 A '))
    if press[len(press)-1].casefold() == "p":
        x=press.split()
        a,b=x
        z=float(a)
        A=z/101325
        B=z/10**5
        print('{} Pascal can be expressed as {:.6f} Atm or {:.6f} Bar'.format(z, A, B))
    elif press[len(press)-1].casefold() == "b":
        x=press.split()
        a,b=x
        z=float(a)
        A=z*.986923
        P=z*10**5
        print('{} Bar can be expressed as {:.6f} Atm or {:.6f} Pascal'.format(z, A, P))
    elif press[len(press)-1].casefold() == "a":
        x=press.split()
        a,b=x
        z=float(a)
        P=z*101325
        B=z*1.01325
        print('{} Atm can be expressed as {:.6f} Pascal or {:.6f} Bar'.format(z, P, B))
    else:
        print('check ur entered value')
elif conv==3:
    print('welcome to Length converter')
    length=str(input('enter the value and unit "WITH A SPACE IN BETWEEN" to be converted e.g 2 mm 2 cm or 2 m or 2 ft '))
    if length[len(length)-1].casefold() == "mm":
        x=length.split()
        a,b=x
        z=float(a)
        cm=z/10
        m=z/1000
        ft=z/304.8
        print('{} mm can be expressed as {:.5f} Cm or {:.5f} Metre or {} Feet'.format(z, cm, m, ft))
    elif length[len(length)-1].casefold() == "cm":
        x=length.split()
        a,b=x
        z=float(a)
        mm=z*10
        m=z/100
        ft=z/30.48
        print('{} cm can be expressed as {:.5f} mm or {:.5f} Metre or {} Feet'.format(z, mm, m, ft))
    elif length[len(length)-1].casefold() == "m":
        x=length.split()
        a,b=x
        z=float(a)
        mm=z*1000
        cm=z*100
        ft=z*3.281
        print('{} cm can be expressed as {:.5f} mm or {:.5f} Metre or {} Feet'.format(z, mm, cm, ft))
    elif length[len(length)-1].casefold() == "ft":
        x=length.split()
        a,b=x
        z=float(a)
        mm=z*304.8
        cm=z*30.48
        m=z/3.281
        print('{} cm can be expressed as {:.5f} mm or {:.5f} Metre or {} Feet'.format(z, mm, cm, m))
    else:
        print('check ur entered value')
else:
    print('check ur conversion input')



