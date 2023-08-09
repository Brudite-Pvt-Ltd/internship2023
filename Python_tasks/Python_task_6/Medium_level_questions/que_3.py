# program 3 :
    
arr = [1, 2, 3, 4, 5]
k = 6

mp = {}
cnt = 0;
for x in arr :
    if k >= x and ( k-x in mp ):
        cnt += 1
    else:
        mp[x] = 1
        
print(cnt)
 
