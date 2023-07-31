#7. Write a Python function to remove all duplicates from an array and return the result

arr1 = [1, 5, 3, 6, 3, 5, 6, 1]

result = list(set(arr1))
print(result)

#OR

result2 = [*set(arr1)]    #returns a dictionary which has to be converted to list
print(result2)