set1 = {1,2,3,45,6,7,8,9,14,12,13,15}
sorted_set = set()

while set1:
    min_ele = min(set1)
    sorted_set.add(min_ele)
    set1.remove(min_ele)

print(sorted_set) 
