# 5.Write a function that takes a string as an argument and returns the number of vowels in the string. If the string is empty, the function should raise a ValueError with the message "The string is empty."

import re

def vowels(string):
    if (len(string) == 0):
        raise ValueError("The string is empty.")
    else:
        regex_for_vowel = "[aeiouAEIOU]"
        return (len(re.findall(regex_for_vowel, string)))

# string = "Hey, This is strong that contains 10 vowels"
# print(vowels(string))
s = ""
print(vowels(s))
