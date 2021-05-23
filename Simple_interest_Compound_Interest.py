import math
p=float(input('enter the principle amount'))
n=float(input('enter the duration in years'))
r=float(input('enter the rate of interest'))
i=float(input('''enter 1 for Simple Interest
enter 2 for Compound Interest'''))
print()
if i==1:
    simple_interest=p*n*r/100
    EMI=(p+simple_interest)/(n*12)
    x=math.ceil(EMI)
    print('the principal amount {} is'.format(p))
    print('the total interest for {} years at {} % rate of simple_interest is {}' .format(n,r,simple_interest))
    print('the monthly installments to be paid for {} months is{}' .format((n*12),x) )

elif i==2:
    compound_interest=p*(pow((1+r/100), n))-p
    installment=((p+compound_interest)/(n*12))
    total_money_paid=installment*n*12
    print('the principal amount {} is'.format(p))
    print('the total interest for {} years at {} % rate of compound-interest is {}' .format(n,r,compound_interest))
    print('the EMI to be paid for {} months is {}' .format((n*12),installment))
    print('the total money paid at the end of {} months will be {}' .format((n*12),(p+compound_interest)))
else:
    print('check interest type again')