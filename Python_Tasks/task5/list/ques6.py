l1=[2,3,5,6,9,2]
l2=[3,5,6,9,8,1]
l3=[]
for x in l1:
    if x in l2:
        l3.append(x)
print("common elements in list1 and list2 are :")
print(l3)         