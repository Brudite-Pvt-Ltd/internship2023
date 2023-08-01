l1=[2,3,4.5,'vishal',4,5,'sharma',4]
n=0
for i in l1:
    if type(i) == str:
        n+=0
    else:
        n+=i
print("the sum of total numbers in list is : ", n)        