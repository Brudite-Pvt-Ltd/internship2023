#9.Write a Python function to find the second-largest element in an array.
list1 = [15, 78, 67, 8, 85, 87, 87, 199, 93]
 
list2 = list(set(list1))
print(list2)
# Sorting the  list
list2.sort()
 
# Printing the second last element
print("Second largest element is:", list2[-2])