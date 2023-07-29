#Question 5 ----------------------------------------------
def sorting(list):
    list2 = []
    for i in range(len(list[0])):
        list1 =[]
        for j in list:
            list1.append(j[i])
        list2.append(list1)
    

    return list2

def reverse(list):
    list1 = []
    for x in list:
        n=len(x)
        for i in range(n):
            for j in range(n):
                 if x[i]>x[j]:
                    (x[i],x[j])=(x[j],x[i])
       
        list1.append(list)
    return list

l = [[6,15,10],[14,9,12],[2,4,6]]

l1 = sorting(l)

l2 = reverse(l1)

l3 = sorting(l2)

print(l3)