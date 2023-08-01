l1 = [3,2,4,5,6,7,88,1,22,26]
n = int(input("enter the number to be searched"))
b=0
for i in range(len(l1)):
    if n == l1[i]:
        b=1
if (b==0):
    print("element is not there ")
else:
    print("element found")    
        
    