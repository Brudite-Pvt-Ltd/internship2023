#wap to count all unique values in list.
list = [1,2,3,1,2,3,4,5,6]
set_method = set(list)
c= len(set_method)
print(c)

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