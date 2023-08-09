# -*- coding: utf-8 -*-
"""
que7
Write a Python function that finds the median of a list of numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3]
Sample Output: Median: 4.0
"""

number_list = [7, 2, 5, 1,4, 9, 3]
from functools import reduce
print(reduce(lambda x,y:x+y,number_list)/len(number_list))
    



