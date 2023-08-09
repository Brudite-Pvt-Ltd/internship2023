def common_list(l1,l2):
    co_list=list()
    for i in l1:
        for j in l2:
            if i==j:
                co_list.append(i)
    return co_list
l1=[12,3,4,5,]
l2=[4,5,6,7,8]
print(common_list(l1,l2))

