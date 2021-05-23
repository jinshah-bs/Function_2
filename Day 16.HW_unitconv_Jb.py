def banner(a="", setlimit = 90):

        b = "Welcome to program for unit conversion of "
        c = b + a
        centred_text = c.center(setlimit-4)
        print(setlimit * "*")
        print()
        print("**{0}**".format(centred_text))
        print()
        print(setlimit * "*")


def temperature():
    print("""
Data entering format:
Temperature value as a whole number and Unit as K for Kelvin 
                                                C for Celcius
                                                F for Farenheit     
          """)

    a= str (input("Enter the temperature value (Space) unit in the above format "))
    temp = a.split()
    p , q = temp
    z = float (p)
    y = str (q)

    if y.casefold() == "k":
        c = z - 273
        f = (z- 273) * (9/5) + 32
        k = z

    elif y.casefold() == "c":
        c = z
        f = ( z * (9/5)) + 32
        k = z + 273

    elif y.casefold() == "f":
        c = (z - 32) * ( 5/9 )
        f = z
        k = ((z - 32) * ( 5/9 )) + 273

    else:
        print("You are entering the temperature value in wrong format")
        return()

    print()
    print("Temperature in Celcius {:.2f}".format(c))
    print("Temperature in Farenheit {:.2f}".format(f))
    print("Temperature in Kelvin {:.2f}".format(k))

    return()



def Pressure():
    print("""
Data entering format:
Pressure value as a whole number and Unit as atm for atmospheric 
                                                Pa for Pascal
                                                Bar for Bar     
          """)

    a= str (input("Enter the pressure value (Space) unit in the above format "))
    temp = a.split()
    p , q = temp
    z = float (p)
    y = str (q)

    if y.casefold() == "atm":
        at = z
        pa = z * 10135
        bar = z * 1.0135

    elif y.casefold() == "pa":
        at = z / 101325
        pa = z
        bar = z / 100000

    elif y.casefold() == "bar":
        at = z / 1.0135
        pa = z * 100000
        bar = z

    else:
        print("You are entering the pressure value in wrong format")
        return()

    print()
    print("Pressure in atm {:.2f}".format(at))
    print("Pressure in Pascal {:.2f}".format(pa))
    print("Pressure in Bar {:.3f}".format(bar))

    return()

def Length():
    print("""
Data entering format:
Length value as a whole number and Unit as  m for Meter 
                                            ft for feet
                                            cm for centimeter
                                            mm for millimeter    
          """)

    a= str (input("Enter the Length value (Space) unit in the above format "))
    temp = a.split()
    p , q = temp
    z = float (p)
    y = str (q)

    if y.casefold() == "m":
        meter = z
        feet = z * 3.281
        centi = z * 100
        milli = z * 1000

    elif y.casefold() == "ft":
        meter = z / 3.281
        feet = z
        centi = z / 3.281 * 100
        milli = z / 3.281 * 1000

    elif y.casefold() == "cm":
        meter = z / 100
        feet = z / 100 * 3.281
        centi = z
        milli = z * 10

    elif y.casefold() == "mm":
        meter = z / 1000
        feet = z / 1000 * 3.281
        centi = z / 10
        milli = z

    else:
        print("You are entering the length value in wrong format")
        return()

    print()
    print("Length in Meter {:.3f}".format(meter))
    print("Length in Feet {:.2f}".format(feet))
    print("Length in Centi Meter {:.1f}".format(centi))
    print("Length in Milli meter {:.0f}".format(milli))

    return()

select = ""

while select != "N":

    list = ["Temperature", "Pressure", "Length"]

    for index, item in enumerate (list):
        print("Code {} : {} ".format(index+1, item))

    i = int (input("Enter the code for unit conversion "))

    if i<= 3:
        banner(list[i-1])

        if i == 1:
            temperature()

        elif i == 2:
            Pressure()

        elif i == 3:
            Length()

    else:
        print("Select the valid code for unit conversion")

    print()
    print()
    select = str(input("Do you want to continue (Y/N)? "))


print("Thank you for using Unit Conversion program")