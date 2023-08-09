# -*- coding: utf-8 -*-
"""
que2:
Create a function that takes a list and returns a new list with unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]
"""


def unique(l):
    return set(l)

l1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(unique(l1))
        