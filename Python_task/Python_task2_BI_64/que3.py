# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:47:07 2023

@author: HP
"""

def eleexist(list,ele):
    if ele in list:
        return "element is exist"
    return "element is not exist"
list =[1,2,3,4,5]

print(eleexist(list, 7))
    
