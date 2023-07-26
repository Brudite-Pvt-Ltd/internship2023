#Q5.Write a Python program to count the number of occurrences of a specific element in an array.

def count(lst, x):
    return lst.count(x)
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,count(lst, x)))
