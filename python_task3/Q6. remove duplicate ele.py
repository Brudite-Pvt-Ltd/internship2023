
def removeDuplicates(list1):
	
	return list(set([i for i in list1]))
		

list1 = [(10, 22), (35, 71), (63, 96), (71, 22)]
print(removeDuplicates(list1))
