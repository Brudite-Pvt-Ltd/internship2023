
list1 = [ [2, 4], [7, 8], [9, 10] ]
list2 = [ [4, 2], [8, 9], [9, 10] ]

print ("The original list 1 : " + str(list1))
print ("The original list 2 : " + str(list2))

res_list = []
for i in list1:
	if i not in list2 and i[::-1] not in list2:
		res_list.append(i)
for i in list2:
	if i not in list1 and i[::-1] not in list1:
		res_list.append(i)
		
print ("The uncommon of two lists is : " + str(res_list))
