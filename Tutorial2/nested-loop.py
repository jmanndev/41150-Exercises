# 2. Write a Python program to construct the following pattern, using a nested
# for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def printRow(numOfStars):
    for i in range(0, numOfStars):
        print('*', end="")
    print('')

biggestRowLength = 5
for i in range(biggestRowLength):
    printRow(i)

# Reverse loop
for i in range(biggestRowLength, 0, -1):
    printRow(i)