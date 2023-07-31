#1.Create two sets:{1,2,3,4} and {3,4,5,6}. Find the elements that are unique to each set.

set1 = {1,2,3,4}
set2 = {3,4,5,6}

#Method 1 
set3 = {x for x in set1 if x not in set2} | {x for x in set2 if x not in set1}
print(set3)
#Method 2 using symmetric_difference built in function
print(set1.symmetric_difference(set2)|set2.symmetric_difference(set1))
#method 3 
set3 = set1-set2 | set2-set1
print(set3)
#method4
set3 = set1.difference(set2) | set2.difference(set1)
print(set3)
