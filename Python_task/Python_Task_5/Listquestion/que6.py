#6. Find the intersection of two lists without using set operations

l1 = [2,4,2,6,3,8,43,21]
l2 = [2,1,3,5,43,6,9,7,10]

l3 =[]
for x in l1:
    if x in l2 and x not in l3:
        l3.append(x)
print(l3)
