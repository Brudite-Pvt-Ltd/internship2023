#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
list= [1,2,3]
try:
    print(list[4])
except IndexError:
    print("Index is out of range")
