# Q2. Find the length of a list without using the len() function.

def length(list):
    count = 0
    for i in list:
        count += 1
    return count

