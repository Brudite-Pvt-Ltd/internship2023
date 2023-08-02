# 1.Create two sets: {1,2,3,4} and {3,4,5,6}. Find the elements that are unique to each set
set1={1,2,3,4}
set2={3,4,5,6}
unique_set = set1.symmetric_difference(set2)
print(unique_set)