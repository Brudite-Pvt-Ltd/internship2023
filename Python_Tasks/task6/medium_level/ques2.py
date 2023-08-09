def unique(l1):
    l3=[]
    for i in l1:
        if i not in l3 :
            l3.append(i)
   
    return l3        






l1 = [1, 2, 2, 3, 4, 4, 5, 5,5]

u=unique(l1)
print("unique elements in list 1 are " , u)