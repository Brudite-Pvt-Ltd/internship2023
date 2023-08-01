d1={"mathura":11,"vanarasi":15,"ayodhya":12,"kailash":20 }
n=int(input("enter the value of the key to be searched"))
b=0
for i,j in d1.items():
    if j==n:
        b=1
        break
if b==1:    
    print("the key for value ",j,"is :",i)
else:
    print("element is not present")    
        
    