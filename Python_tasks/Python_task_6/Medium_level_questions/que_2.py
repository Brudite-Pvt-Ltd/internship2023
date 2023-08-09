# program 2 :
    
list1 = [1, 2, 2, 3, 4, 4, 5, 5]

list2 = [ ]

for x in list1 :
    if x not in list2 :
        list2.append(x)
        
print(list2)