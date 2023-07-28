
def sort(list):
    i=0
    j=0
    for i in range(0,len(list)):      
        for j in range(len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
             
    return list       
            
            
    

list1=[[6, 1, 4], [9, 8, 14], [8, 9, 7]]
newList = []
for i in list1:
    newList.append(sort(i))
print(newList)            