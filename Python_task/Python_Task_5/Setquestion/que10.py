#10You ,are given a set of positive integers. Write a function to find the length of the longest consecutive sequence 
#of numbers that can be formed by arranging the elements in any order.

s = {4,7,2,8,9,12,1,9,5,11,17,18,16,15,14,1,3,6}

sorted(s)
print(s)
t = -1
count =0
macount = -1
for x in s:
    if t == -1:
        t = x+1
        count += 1
    elif(t==x):
        t += 1
        count += 1
    else:
        if macount < count:
            macount = count
        t = x+1
        count = 1
if macount>count:
    print("length of the longest consecutive sequence",macount)
else:
    print("length of the longest consecutive sequence",count)

