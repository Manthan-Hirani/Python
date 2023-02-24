# 2.  Write python program that accepts a sentence and calculate the number of words, digits, uppercase letters and lowercase letters.

import re
string = "Hello, this is a STRING havig small-case, UPPER-CASE and numbers like, 212 3246 and 355456."
lst = re.split(" ",string)
print("Total numbers of Words:", len(lst))

regex_for_lower_case = "[a-z]"
regex_check_small_casse = re.findall(regex_for_lower_case, string)
print("Total numbers of smallcase letters:", len(regex_check_small_casse))

regex_for_upper_case = "[A-Z]"
regex_check_upper_casse = re.findall(regex_for_upper_case, string)
print("Total numbers of uppercase letters:", len(regex_check_upper_casse))

regex_for_digits = "[0-9]"
regex_check_digits = re.findall(regex_for_digits, string)
print("Total numbers of digits:", len(regex_check_digits))
