# Write a python program that will prompt the user for his name, age, and
# phone number and will ask him “Are you married?”. Name should only
# contain characters. Age should only contain an age between 7 and 100
# and the question should only accept “yes” or “no” Each input should be
# evaluated and checked whether it is a valid input or not using try-except
# and meaningful errors should be thrown properly

import re

re_name = "^[A-z]*$"
re_phone = "^(\d\s?){10}$"
re_married = "^[y,n][e,o]s?$"


def inputAge(prompt, errorMessage):
    while True:
        try:
            userInput = int(input(prompt))
            if 7 > userInput or userInput > 100:
                raise ValueError
        except ValueError:
            print(errorMessage)
            continue
        else:
            return userInput
            break


def inputValidation(prompt, errorMessage, regEx):
    while True:
        userInput = input(prompt)
        if not re.match(regEx, userInput):
            print(errorMessage)
        else:
            return userInput
            break


name = inputValidation("Whats your name? ", "  Enter only letters", re_name)
age = inputAge("How old are you? ", "  Enter a number between 7 and 100: ")
phone = inputValidation("Whats your phone number? ", "  Enter 10 digits, whitespace is ignored", re_phone)
married = inputValidation("Are you married? ", "  Enter yes or no", re_married)


print("Name - " + str(name))
print("Age - " + str(age))
print("Phone - " + str(phone))
print("Married - " + str(married))
