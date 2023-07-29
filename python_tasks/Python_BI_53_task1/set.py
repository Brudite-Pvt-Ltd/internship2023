#union method 1
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

#intersection method 2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

#issubset method 3
set1 = {1, 2}
set2 = {1, 2, 3, 4}
boolean=set1.issubset(set2)  
print(boolean) # Output: True

#isdisjoint method 4 checks if two sets have common element
set1 = {1, 2, 3}
set2 = {3, 4}
boolean=set1.isdisjoint(set2)
print(boolean)  # Output: false

#discard method 5 does't raise any error if the elements not
my_set = {1, 2, 3}
my_set.discard(4)
print(my_set)  # Output: {1, 3}