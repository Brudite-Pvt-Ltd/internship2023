list1 = [[2,4],[7,8],[9,10]]
list2 = [[4,2],[8,9],[9,10]]

list3 = []
for x in list1:
    if x not in list2  and x[::-1] not in list2:
        list3.append(x)

for x in list2:
    if x not in list1  and x[::-1] not in list1:
        list3.append(x)
        
print(list3)