# 1. Write a python program that act as a cashier which will prompt the user
# for numbers that can be either integers or floats until the user enters 0.
# The program should accumulate all the entered numbers up until the 0
# and provide the total before and after tax. Tax is 0.05


def inputNumber(prompt):
    while True:
        try:
            userInput = float(input(prompt))
        except (NameError, ValueError, SyntaxError):
            print("   Not a number! Try again.")
            continue
        else:
            return userInput
            break


total = 0

while True:
    n = inputNumber("Enter value (0 to end): ")
    if n == 0:
        break
    else:
        total += n

print("Before tax: " + str(total))
print("After tax: " + str(total*1.05))

