#write a program to count unique value in list python

list = [1,2,3,4,5,5,4,3,2,17,8,9,4]
num_values = len(set(list))
print("number of unique value:",num_values)




list2 = [1, 2, 2, 5, 8, 4, 4, 8]

l1 = []
count = 0

for item in list2:
	if item not in l1:
		count += 1
		l1.append(item)

print("No of unique items are:", count)





import numpy as np

a = [1, 2, 2, 4, 3, 6, 4, 8]

value= np.unique(a)

print("list of unique values:",value)
