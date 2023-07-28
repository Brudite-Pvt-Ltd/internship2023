#Q9.Write a Python function to find the second-largest element in an array.

list = [2, 1, 8, 7, 3, 0]
print("The given list is",list)
list.sort()
print("We sorted the list",list)
print("The second largest element of the list is", list[-2])
