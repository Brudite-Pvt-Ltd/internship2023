list1=[1,2,2,4,5,3]
list2=[3,3,4,2,0]
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
        list2.remove(i)
print(list3)        