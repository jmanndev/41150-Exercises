# 4. Write a Python program to search the numbers (0-9) of length between 1
# to 3 in the given string "Exercises number 1, 12, 13, 1445 and 345 are
# important

import re

regex = "\\b[0-9]{1,3}\\b"
string = "Exercises number 1, 12, 13, 1445 and 345 are important"

p = re.compile(regex)
print(p.findall(string))
