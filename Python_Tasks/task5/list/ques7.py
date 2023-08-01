l1=[2,3,5,6,9,2]
l2=[3,5,6,9,8,4]
a=len(l1)
b=len(l2)

if a == b:
    l3=[]
    for x in range(0,a):
        i=l1[x]*l2[x]
        l3.append(i)
    print("pair wise product of two lists is ")    
    print(l3)    
else:
    print("pairwise product is not possible ")        
