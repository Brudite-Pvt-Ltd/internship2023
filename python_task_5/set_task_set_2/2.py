# 2.Create a set and repeatedly add an element until it reaches a size of 10.
set = ()
while len(set)< 10 :
     element = int(input("enter the element to add in set:"))
     set.add(element)
     print(set)