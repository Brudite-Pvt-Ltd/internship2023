#Write a Python function to remove all duplicates from an array and return the result.

array1 = [ 1,4,7,8,2,6,1,7,9,9]

result = list (set(array1))
print(result)

result1 = [*set(array1)]
print(result1)