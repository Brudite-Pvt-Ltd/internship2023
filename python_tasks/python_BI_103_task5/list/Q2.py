# Find the length of a list without using the len() function.

def list_length(list1):
    count = 0
    for item in list1:
        count += 1
    return count

list1 = [1,2,23,4,5,6,7]
print(list_length(list1))