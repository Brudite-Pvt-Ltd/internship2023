# program 1 : find the element that are unique to each set 

s1 = {1,2,3,4}
s2 = {3,4,5,6}


# case :- if we want to find the unique elements for a set, that are not present in other set 

set1_diff = s1.difference(s2)
set2_diff = s2.difference(s1)

print(set1_diff)
print(set2_diff)


# case :- if we want to find the unique elements that are unique for both set

unique_for_both = set1_diff.union(set2_diff)

print(unique_for_both)
