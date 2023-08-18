# -*- coding: utf-8 -*-
"""
que4
Given an array of size N. The task is to rotate array by D elements towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
"""
arr = [1, 2, 3, 4, 5]
D = 2

for i in range(0,len(arr)-D):
    arr.append(arr[0])
    arr.pop(0)
    
print(arr)
