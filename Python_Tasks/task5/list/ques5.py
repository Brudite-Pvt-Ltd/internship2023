
def sort(list):
    i=0
    j=0
    for i in range(0,len(list)):      
        for j in range(len(list)):
            if list[i][1]<list[j][1]:
                list[i],list[j]=list[j],list[i]
             
    return list

l1=[(1,2),(2,0),(3,1),(4,4)]
l2=sort(l1)
print("orignal list : ", l1)
print("sorted list : ", l2)
    

