"""
1.Write a Python program to find the common elements between two lists.
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
Sample output: [4, 5]
"""

l1 = [1, 2, 3, 4, 5] 
l2 = [4, 5, 6, 7, 8]


#method 1 using list comphrehension 
output = [x for x in l1 if x in l2]
print(output)
#method 2 using set
output2 = set(l1).intersection(set(l2))
print(list(output))