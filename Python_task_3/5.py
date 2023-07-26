# program 5 

# creating my list 
l = [[6, 15, 10], [14, 9, 12], [2, 4, 6]]

# getting the length of list
n = len(l)

# creating a new list of empty list of same size
new_l = [[] for i in range(n)]


# ittrating with range in lists
for i in range(0, n):
    # creating a empty list
    temp = []
    
    # extracting columns in temp
    for j in range(0, n):
        temp.append(l[j][i])
    
    # sorting it in reverse order
    temp.sort(reverse=True);
    for x in range(0, n):
        new_l[x].append(temp[x])


print(new_l)