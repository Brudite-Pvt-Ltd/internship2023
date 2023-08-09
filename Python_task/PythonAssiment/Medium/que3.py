# -*- coding: utf-8 -*-
"""
que3 
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5],  k = 6
Sample Output: Pair count: 2
"""
def sumpaircount(l,s):
    unordered_map ={}
    count =0
    for i in range(len(l)):
        if s - l[i] in unordered_map:
            count += unordered_map[s-l[i]]
        if l[i] in unordered_map:
            unordered_map[l[i]] += 1
        else:
            unordered_map[l[i]] =1
        
    return count

def 

l =[0,1,2,3,4,5,6]
s =6


print(sumpaircount(l, s))
