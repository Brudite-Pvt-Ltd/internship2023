# -*- coding: utf-8 -*-
"""

que 9
Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range
"""

try:
    l =[1,2,4,45,23,235,32]

    for i in range(len(l)+1):
        x =l[i]
except Exception as e:
    print("handling the list index out of range :",e)
finally:
    pass


