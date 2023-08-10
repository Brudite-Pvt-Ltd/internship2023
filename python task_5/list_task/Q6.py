#Find the intersection of two lists without using set operations
l1 = [1,2,3,4,5,6]
l2 = [4,5,6,7,8]
intersection = [x for x in l1 if x in l2]
print(intersection)