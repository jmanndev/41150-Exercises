# 2. Write a Python program to construct the
# following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


def inputNumber(prompt):
    while True:
        try:
            userInput = int(input(prompt))
        except (ValueError):
            print("   Not a number! Try again.")
            continue
        else:
            return userInput
            break


length = inputNumber("Enter number: ")

for i in range(1-length, length):
    for j in range(0, length - abs(i)):
        print('*', end="")
    print('')
