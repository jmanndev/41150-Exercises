# Write a Python program that matches a string that has an 'a' followed by
# anything, ending in 'b'

import re

def inputValidation(prompt, errorMessage, regEx):
    while True:
        userInput = input(prompt)
        if not re.match(regEx, userInput):
            print(errorMessage)
        else:
            return userInput
            break


string = inputValidation("Enter string  ", "No match, try again", "^a.*b$")
print("Match")