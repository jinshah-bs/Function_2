name = input("What is your name? ")
print(f"So your are {name}")
age = int(input("Please enter your age: "))
ageBarrier = 18
maxAge = 60

if ageBarrier <= age <= maxAge :
    print(f"So, {name},You are {age} years old, and eligible for license")
elif age > maxAge:
    print(f"Go to hell!!, Mr.{name}")
else:
    print("Sorry, you have to wait {0} more years to get license, Mr.{1}".format(ageBarrier-age,name))

# if age>=18 and age <=60:
#     print(f"So, {name},You are {age} years old, and eligible for license")
# elif age > maxAge:
#     print(f"Go to hell!!, Mr.{name}")
# else:
#     print("Sorry, you have to wait {0} more years to get license, Mr.{1}".format(ageBarrier-age,name))



# if age > maxAge:
#     print(f"Go to hell!!, Mr.{name} " * 2)
# elif age >= ageBarrier:
#     print(f"So, {name},You are {age} years old, and eligible for license")
# else:
#     print("Sorry, you have to wait {0} more years to get license, Mr.{1}".format(ageBarrier-age,name))