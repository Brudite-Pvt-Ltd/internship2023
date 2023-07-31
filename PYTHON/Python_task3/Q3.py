def sort(l):
    for a in range(0,len(l)):
        for b in range(a,len(l)):
            if l[a]<l[b]:
                temp = l[a]
                l[a] = l[b]
                l[b] = temp


list=[[6,1,4],[9,8,14],[8,9,7]]

list1 = []

for x in list:
    sort(x)
    list1.append(x)

print(list1)    