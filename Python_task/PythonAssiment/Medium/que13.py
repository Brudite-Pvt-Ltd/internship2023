# -*- coding: utf-8 -*-
"""
que 13
Write a Python program to find if a given string starts with a given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H"
Sample Output: True
"""
string = "Hello, world!"
given_char = "H"
s= lambda string,given_char: True if given_char == string[0] else False
print(s(string,given_char))
