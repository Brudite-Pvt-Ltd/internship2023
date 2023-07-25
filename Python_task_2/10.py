# program 10

array1 = [1, 2, 3, 4, 5]
array2 = [3, 5, 6, 7, 8]

ans = []
for x in array1:
    if x in array2:
        ans.append(x)
        array2.remove(x)
        
print(ans)
