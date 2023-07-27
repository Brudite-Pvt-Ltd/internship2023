def sort(list):
    i=0
    j=0
    for i in range(0,len(list)):      
        for j in range(len(list)):
            if list[i]<list[j]:
                list[i],list[j]=list[j],list[i]
             
    return list

import numpy as np

n=3
l1=[[6,15,10],[14,9,12],[2,4,6]]
print("the input matrix is ")
for i in range(n):
   for j in range(n):
       print(l1[i][j], " ", end='')
   print()
print("")
l2=np.transpose(l1)
l3=[]
for x in l2:
    l3.append(sort(x))
l3=np.transpose(l3)
print("the output matrix is ")

print(l3)




   