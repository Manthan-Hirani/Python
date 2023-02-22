Sample_dict = [47, 64, 69, 37, 76, 83, 95, 97]
test_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Output = [47, 69, 76, 97]
print("Before sorting the list looks like this:",Sample_dict)

my_dict = list(test_dict.values())
# print(my_dict)

# Use .copy() or = as per requirement
Sample_dict = my_dict
# Sample_dict = my_dict.copy()

print("After sorting the list looks like this:",Sample_dict)