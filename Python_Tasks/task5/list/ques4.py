l1=[1,1,2,1,1]
l2=[]
for i in range(len(l1),0,-1):
     l2.append(l1[i-1])
     
if l1==l2:
    print("list is pailindrome")
else:
    print("list is not a palindrome")    
