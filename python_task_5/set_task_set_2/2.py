# 2.Create a set and repeatedly add an element until it reaches a size of 10.
emp_set = set()
while len(emp_set)< 10 :
     element = int(input("enter the element to add in set:"))
     emp_set.add(element)
     print(emp_set)