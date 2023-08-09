# -*- coding: utf-8 -*-
"""
que6
Write a Python program to check if a number is a power of two using recursion.
"""

def ispower2(num):
    if isinstance(num, float):
        return False
    if num ==1:
        return True
    return ispower2(num/2)
    

print(ispower2(8))

