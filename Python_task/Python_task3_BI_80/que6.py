# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:47:01 2023

@author: HP
"""

l =[(1,2,3),(3,2,1),(1,2,3),(3,3,3)]

#if we consider a (1,2) != (2,1)
print(list(set(l)))



# in this i consider that (1,2) == (2,1)


#initialize a empty list
al = []
s = []
for x in l:
    tup = sorted(list(x))
    if tup not in s:
        al.append(x)
        s.append(tup)
print(al)

#answer is different for both as condition's are different
