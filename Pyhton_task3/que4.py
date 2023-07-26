# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:41:55 2023

@author: HP
"""

li = [[3,5,7],[5,8,3,2],[7,5,2,5,4],[1,2,7,4],[5,9,99,6,6,5],[1,2],[1,2,5]]

target = 7
count =0
for x in li:
    for i in x:
        if i == target:
            count += 1
if count>0:
    print("Target",target," is present" ,count,"times in a list")

        
    