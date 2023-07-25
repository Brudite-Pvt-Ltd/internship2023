#4. Given an array [1, 2, 3, 4, 5], shuffle the elements randomly to create a new array.



import random

list =[1,2,3,4,5]
print(list)
slist = list.copy()
random.shuffle(slist)
print(slist)
