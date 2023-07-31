#4.Remove the maximum element from a set with out using the max() function
from functools import reduce
set1 = {2,4,85,14,1,3,8,9}
set2 = {x for x in set1 if x != reduce(lambda x,y: x if x > y else y,set1)}
print(set2)