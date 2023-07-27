list1 = [[2,4],[7,8],[9,10]]
list2 = [[4,2],[8,9],[9,10]]
#find uncommon pairs
list=[]
for i in list1:
    if i  not in list2 and  i[::-1] not in list2:
        list.append(i)
        for i in list2:
            if i not in list1 and i[::-1] not in list1:
                list.append(i)
                print(list)