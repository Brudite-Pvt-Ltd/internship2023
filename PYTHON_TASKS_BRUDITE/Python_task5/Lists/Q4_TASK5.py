# Q4 Find the median of a list without using the built-in median function.

list=[4, 9, 2, 6, 1, 3, 8]
n = len(list)
print("length of list is:", n)

if n % 2 == 0:
    median1 = list[n//2]
    median2 = list[n//2 - 1]
    median = (median1 + median2) / 2
else:
    median = list[n//2]
print("median is :", median)