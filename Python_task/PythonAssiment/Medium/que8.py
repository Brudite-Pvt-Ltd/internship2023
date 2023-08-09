# -*- coding: utf-8 -*-
"""
que8
Write a Python function that counts the number of vowels in a given string.
Sample Input: string = "Hello, World!"
Sample Output: Number of vowels: 3
"""
string = "Hello, World!"

vowels ='aeiou'
count =0
from collections import Counter
l=Counter(string.lower())
for x in l:
    if x in vowels:
        count += l[x]
        
print(count)



