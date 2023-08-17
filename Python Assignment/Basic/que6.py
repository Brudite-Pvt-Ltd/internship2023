num=int(input("Enter your number: "))
factor=[]
for i in range(1,num):
    if(num%i==0):
        factor.append(i)
if(sum(factor)==num):
    print(f'{num} is a Perfect number.')
else:
    print(f'{num} is not a Perfect number.')