# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:50:13 2023

@author: visha
"""

list = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = 0
currentSum = 0 
idx = -1;

for i in range(0, len(list)):    
    currentSum += list[i]

    if currentSum > max_sum :
        idx = i 
        max_sum = currentSum
    
    if currentSum < 0:
        currentSum = 0 ;

sub_list = []
new= 0;
for i in range(idx, -1, -1):
    new += list[i]
    sub_list.insert(0, list[i])
    if(new== max_sum):
        break;
        
print(max_sum, sub_list)