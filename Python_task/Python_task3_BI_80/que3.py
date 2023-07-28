# -*- coding: utf-8 -*-
"""
Q3.list1=[[6,1,4],[9,8,14],[8,9,7]]
Result=[[6,4,1],[14,9,8],[9,8,7]]
Reverse sorting
"""

# reverse sorting method
import numpy as np

def sorting(l):
    
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if l[i]<l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] =temp
            
#list
l = [[9,5,7],[9,5,8],[7,9,8],[1,5,2]]


#empty lists
l1 =[]
l2 = []

#method 1 using sorting
for x in l:
     sorting(x)
     l1.append(x)
print(l1)  

     