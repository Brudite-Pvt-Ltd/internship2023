#que5 Implement a custom sorting function for a list of tuples based on the second element of each tuple

l =[(2,6,3,4),(1,2,5,8,3),(8,4,5,9,2,3),(8,9),(1,0,7)]

# for i in range(len(l)-1):
    
#     for x in range(i,len(l)-1):
#         if l[i][2]>l[x][2]:
#             l[i][2],l[x][2] = l[x][2],l[i][2]
print(l," ")
for i in range(len(l)):
    for j in range(i,len(l)):
        if (l[i])[1]>(l[j])[1]:
            # temp = l[i]
            # l[i] =l[j]
            # l[j] = temp
            l[i],l[j]=l[j],l[i]
            
print(l)