"""que 8Write a function that takes a list of integers and returns a new list with each element replaced by the product 
of all the other elements in the original list , excluding the current element"""

l =[3,5,8,2,2,3,4]

#method 1
from functools import reduce
product = reduce(lambda x,y:x*y,l)

l1 = [product//x for x in l]
print("Method 1",l1)

#method 2
prdct = 1
for x in l:
    prdct *= x
    
l2 = [prdct//x for x in l]
print("Method 2 ",l2)