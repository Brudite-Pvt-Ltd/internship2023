#Implement a custom sorting function for a list of tuples based on the second element of each tuple
list = [(1,2),(3,4),(2,3)]
list.sort(key = lambda x:x[1])
print(list)