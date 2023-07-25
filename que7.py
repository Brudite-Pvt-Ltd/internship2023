#7. Write a Python program to merge two sorted arrays into a single sorted array.

list1 = [1,4,6,9,12]
list2 = [2,4,6,7,23,45,78]

list1.extend(list2)
list1.sort()
print(list1)