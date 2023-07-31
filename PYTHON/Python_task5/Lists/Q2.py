# Find the length of a list without using the len() function.

def length_list(list):
    count = 0
    for item in list:
        count += 1
    return count

list = [1,3,5,7,9]
print(length_list(list))