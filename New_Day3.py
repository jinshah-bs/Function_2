# day = input("Today is: (First letter should be capital) ")
# print("So today is {}".format(day))
# Temp = int(input("How about the temperature? "))
# Rainy = False
# if day == "Sunday" and (Temp <30 or Rainy == False):
#     print(f"So we can Blast today, as the temperature is {Temp} is less than 30 and today is {day}")
# else:
#     print("Go and sleep")

name = "Divakar"
letter = input("type one letter: ")
if letter.casefold() not in name.casefold():
    print(f"The letter, {letter} is not in {name}")
else:
    print("Sorry, f************k of")