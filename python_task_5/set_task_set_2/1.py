# 1.Create a set with elements from 1 to 10.Check if it is a subset of {0,5,10,15}.
set = set(range(1,11))
print("Set with elements from 1 to 10:", set)
another_set = {0, 5, 10, 15}
print(another_set)
is_subset = set.issubset(another_set)
print("Is the set is a subset of {0, 5, 10, 15}?", is_subset)