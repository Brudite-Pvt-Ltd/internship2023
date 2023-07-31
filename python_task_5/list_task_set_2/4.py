# 4.Find the median of a list without using the built-in median function.
list = [3, 5, 4, 7, 2]
n = len(list)
print("length of list is:", n)
list.sort()
print("sorted list:", list)

if n%2 == 0:
    median1 = list[n//2]
    median2 = list[n//2 - 1]
    median = (median1+median2)/2
else:
    median = list[n//2]
print("median is :", median)