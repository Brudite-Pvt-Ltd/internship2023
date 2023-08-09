def pair(a,b):
    l1=[]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j] == b:
                l1.append((a[i],a[j]))
    return l1



arr = [1, 2, 3, 4, 5]
k=6
p=pair(arr,k)
print("the number of pairs whose sum is equal to ",k , "are ", len(p),"pairs" )