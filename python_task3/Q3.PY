#QUestion 3 ---------------------------------------------

list1=[[6,1,4],[9,8,14],[8,9,7]]
list2=[]
for x in list1:
    n=len(x)
    for i in range(n):
        for j in range(n):
            if(x[i] >x[j]):
                (x[i], x[j]) = (x[j], x[i])

    list2.append(x)

print("new reverse list :-", list2)