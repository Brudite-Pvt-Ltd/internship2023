#7. Write a Python program to merge two sorted arrays into a single sorted array.
arr1 = [1, 4, 5, 6, 5]
arr2= [3, 5, 7, 2, 5]
arr1.sort()
arr2.sort()
arr1.extend(arr2)
arr1.sort()
 

print ("merged list : "    + str(arr1))