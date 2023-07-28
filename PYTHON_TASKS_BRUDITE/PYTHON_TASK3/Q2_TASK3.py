# Q2.list1 = [[2,4],[7,8],[9,10]] list2=[[4,2],[8,9],[9,10]] Find all the uncommon pairs.

l1 = [[2,4],[7,8],[9,10]]
l2 = [[4,2],[8,9],[9,10]]

new_list = []

for i in l1:
    if i not in l2 and i[::-1] not in l2:
        new_list.append(i)
        for i in l2:
            if i not in l1 and i[::-1] not in l1:
                new_list.append(i)
                print(new_list)