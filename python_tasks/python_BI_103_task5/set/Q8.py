def find_nth(my_set, n):
    sort_set = set()

    while my_set:
        min1= min(my_set)
        sort_set.add(min1)
        my_set.remove(min1)

    list1=list(sort_set)
    return list1[n-1]

        
my_set = {9, 3, 6, 1, 4}
n = 3
result = find_nth(my_set, n)
print(result)  
