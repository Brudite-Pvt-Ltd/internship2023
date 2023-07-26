# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:58:45 2023

@author: HP
"""

l = [1,4,2,6,3,4,2,6,1,3,8,6,9,6,12]

#Method 1 using typecasting
print(len(list(set((l)))))

#Method 2 using dictionary
print(len(list(dict.fromkeys(l))))

#Method 3 using Counter store in map 
from collections import Counter
print(len(list(Counter(l).keys())))


#Method 4  brute approach
l1 =[]
for i in l:
    if i not in l1:
        l1.append(i)
print(len(l1))

#Method 5 numpy library
#import numpy as np
#print(len(list(np.unique(l))))
