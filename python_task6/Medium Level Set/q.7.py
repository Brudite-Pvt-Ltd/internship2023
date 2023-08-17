# Write a Python function that finds the median of a list of numbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3]
# Sample Output: Median: 4.5
number_list = [7 ,2 ,5 ,1 ,9 ,3]
print(" The original list of number is :"+ str(number_list))

number_list.sort()
print(number_list)
mid = len(number_list) // 2
res = number_list[mid] + number_list[~mid] /2

print(" The median of list is :"+ str(res))

    