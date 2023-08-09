"""
que2
Write a program to count the the lines in a file “demo.txt” 
"""
with open("demo.txt",'r') as f:
    count = len(f.readlines())
print("In demo.txt file there is a ",count,"line")