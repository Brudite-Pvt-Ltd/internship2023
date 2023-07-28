# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:12:00 2023

@author: HP
"""
#define a function to arrage a list as first element of each row in a first column and so..o
def arrange(l):
    l12 = []
    for i in range(len(l[0])):
        l11 =[]
        for x in l:
            l11.append(x[i])
        l12.append(l11)

    return l12


#define a function to reverse
def reverse(l):
    l1 = []
    for x in l:
         x.sort(reverse=True)
         l1.append(x)
    return l 


l = [[6,15,10],[14,9,12],[2,4,6]]
#print a orginal list
print(l)
#calling a function arrage() 
l12 = arrange(l)
#calling a function reverse()
l1 = reverse(l12)
#calling a function arrage
al = arrange(l12)
print(al)


