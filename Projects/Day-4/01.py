# 1.Write a Python program to check the validity of a password given by the user.
# The Password should satisfy the following criteria:
#     • Contain at least 1 letter between a and z
#     • Contain at least 1 number between 0 and 9
#     • Contain at least 1 letter between A and Z
#     • Contain at least 1 character from $, #, @
#     • Minimum length of password: 6
#     • Maximum length of password: 12

import re

regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,12}$"
password = input("Enter Password:")
check = re.findall(regex, password)

if (check):
    print("Password is valid")
else:
    print("Password is invalid")
