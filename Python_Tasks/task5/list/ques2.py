l1 = [3,2,4,2,1,7,88,1,22,26,2,3,1]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
        
print("the orignal list is :", l1)   
print("the list with only unique values is  ",l2)
         