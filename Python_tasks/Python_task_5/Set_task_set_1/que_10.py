# program 10 : find the length of longest consicutive sequence(in any order)

s = {2, 1, 3, 6, 5, 8, 9, 10, 11, 13, 14}

# converting it into sorted list for traversal
l = list(sorted(s))
print(l)

max_len = 1;
temp = 1

for i in range(1,len(l)):
    if l[i-1] + 1 == l[i]:
        temp += 1
    else :
        temp = 1
        
    max_len = max(max_len, temp)
    
print(max_len)

