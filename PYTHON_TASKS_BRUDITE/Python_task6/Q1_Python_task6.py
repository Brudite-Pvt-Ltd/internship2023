# Q1. Write a Python program to find the common elements between two lists.

l1 = [1, 2, 3, 4, 5]
l2 = [7, 1, 3, 9, 6]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)