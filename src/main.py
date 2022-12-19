from operation import *

firstNumber = int(input("Fisrt Number = "))
secoundNumber = int(input("Sec Number = "))

print("select operation: ")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")

selectedOption = int(input("your choosee : "))

if selectedOption == 1:
    addition(firstNumber, secoundNumber)
elif selectedOption == 2:
    subtraction(firstNumber, secoundNumber)
elif selectedOption == 3:
    multiplication(firstNumber, secoundNumber)
elif selectedOption == 4:
    division(firstNumber, secoundNumber)
else:
    print("Sorry, I don't have any option")
