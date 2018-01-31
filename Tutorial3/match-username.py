# Write a Python program to match a string that contains only upper and
# lowercase letters, numbers, and underscores

import re

def inputValidation(prompt, errorMessage, regEx):
    while True:
        userInput = input(prompt)
        if not re.match(regEx, userInput):
            print(errorMessage)
        else:
            return userInput
            break


string = inputValidation("Enter string  ", "No match, try again", "^[A-z1-9_]*$")
print("Match")