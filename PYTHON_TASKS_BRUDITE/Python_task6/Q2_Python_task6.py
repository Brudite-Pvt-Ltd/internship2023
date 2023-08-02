# Q2. Create a function that takes a list and 
# returns a new list with unique elements of the first list.

def unique_list(list):
    return set(list)
unique_list = [1,1,12,4,4,5,9]
result = unique_list
print(result)