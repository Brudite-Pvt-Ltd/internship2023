d1={"mathura":11,"vanarasi":15,"ayodhya":12,"kailash":20 }
old=input("enter the key which has to be changed : ")

b=0
for i in d1.keys():
    if i==old:
        new=input("enter the value of modified key : ")
        d1[new]=d1.pop(old)
        b=1
        break
    else:
        b=0
            

if b==1:
    print("modified dictionary is : ",d1)
else:
    print("key to be replaced is not found")    
    
    
         
        