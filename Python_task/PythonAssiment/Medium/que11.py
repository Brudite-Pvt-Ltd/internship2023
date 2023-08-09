# -*- coding: utf-8 -*-
"""
que 11
Write a Python program to create a list of given strings individually of the list using Python map function.
Eg.
Input: 
['Red', 'Blue', 'Black', 'White', 'Pink']
Output:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

"""
l=['Red', 'Blue', 'Black', 'White', 'Pink']

for i in range(len(l)):
    l[i] = list(l[i])
print(l)
