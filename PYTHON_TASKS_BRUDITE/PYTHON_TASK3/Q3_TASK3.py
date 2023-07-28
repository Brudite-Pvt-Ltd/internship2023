# Q3. list1 = [[6,1,4],[9,8,14],[8,9,7]] 
# Result = [[6,4,1],[14,9,8],[9,8,7]] 
# Reverse sorting.

list1 = [[6,1,4],[9,8,14],[8,9,7]] 

for sublist in list1:
    sublist.sort(reverse=True)
print(list1)