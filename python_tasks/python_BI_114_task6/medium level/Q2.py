def unique(l):
    l1=list()
    for i in l:
        if i  not in l1:
            l1.append(i)
    return l1
list1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(unique(list1))