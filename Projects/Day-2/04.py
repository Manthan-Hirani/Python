first_set = {50, 44, 35}
second_set = {57, 83, 50, 23, 44, 78, 5, 35, 92}

print(first_set)
print(second_set)

sub_set = first_set.issubset(second_set)
super_set = first_set.issuperset(second_set)

if (sub_set or super_set):
    second_set = second_set.difference(first_set)

print(second_set)