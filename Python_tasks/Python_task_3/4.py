# program 4


# creating a new list 
l = [[1,2,3],[1,3,4],[4,5,6,4,5,6],[1,5,6,8]]

# t is target value that we want to serach in the list
t = 4

# cnt is for counting the occurence of the target value
cnt = 0



# itterating all the elements in list and checking it to target
for i in l :
    for j in i :
        if t == j:
            cnt += 1 


# printing the occurence of target
if(cnt > 0):
    print( "Present ")
    print( "Count =", cnt)
else:
    print("Not Present")
            
    