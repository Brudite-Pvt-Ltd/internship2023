#Given two arrays with unique elements, find the common elements between them.

array1 = [6,8,9,2,4]
array2 = [1,3,7,6,0]

common = [i for i in array1 if i in array2]
print (common)

print(set (array1) & set (array2))
