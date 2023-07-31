#6.Given two arrays with unique elements, find the common elements between them.

arr1 = [1,2,3]
arr2 = [3,4,5]

common = [i for i in arr1 if i in arr2]
print(common)

#OR

print(set(arr1) & set(arr2))