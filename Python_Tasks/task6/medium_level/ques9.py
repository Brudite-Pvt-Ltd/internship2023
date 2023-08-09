l1=[1,2,3,4,5,6]
a=0
for i in range(0,len(l1)):
    try:
        a=l1[i]+l1[i+1]
        print(a)
    except IndexError as error:
        print(error)
        
        