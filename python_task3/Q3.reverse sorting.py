
list1 = [[6, 1, 4], [9, 8 , 14], [8, 9, 7]]

print("The original list is : " + str(list1))

for ele in list1:
	ele.sort(reverse=True)

print("the reverse list is :"+ str(list1))
