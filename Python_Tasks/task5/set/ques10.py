s1={4,2,3,6,7,8,1,}
l1=sorted(s1)
ml = 1
cl = 1
for i in range(0,(len(l1)-1)):
    if l1[i]+1 == l1[i+1]:
        cl+=1
    else:
        cl=1
    ml=max(ml,cl)    
print("the longest consecutive sequence is : ", ml)    