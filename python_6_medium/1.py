#Write a Python program to find the common elements between two lists.
# Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
# Sample output: [4, 5]
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
l3 = []
for i in l1:
    if i in l2:
        l3.append(i)
        print(l3)
