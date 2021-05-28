def simple_int(p:float,n:float,r:float,d:int):
    intrest = p * n * r / 100
    print("The value of simple intrest is {:.2f}".format(intrest))
    total_amount = intrest + p

    for i in range(1,d+1):
        emi = total_amount / ((d+1)- i)
        print("{} month EMI is {:.2f} & remaining to be paid {:.2f}".format(i,emi,total_amount))
        total_amount = total_amount - emi



def compunt_int(p:float,q:float,r:float,d:int):
    total_amount = p * pow(1+ (0.01 * (r/q)), (q*d/12))
    intrest = total_amount - p
    print("The value of compound intrest is {:.2f}".format(intrest))

    for i in range(1,d+1):
        emi = total_amount / ((d+1)- i)
        print("{} month EMI is {:.2f} & remaining to be paid {:.2f}".format(i,emi,total_amount))
        total_amount = total_amount - emi


a = float (input("Enter the value of principal amount "))
b = float (input("Enter the compounding period in years "))
c = float (input("Enter the rate of intrest "))
d = int (input("Enter the number for calculating monthly instalment "))

simple_int(a,b,c,d)
print()
compunt_int(a,b,c,d)