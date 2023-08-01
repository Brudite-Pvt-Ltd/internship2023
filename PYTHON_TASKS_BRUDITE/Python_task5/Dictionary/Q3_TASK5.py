# Extract unique values in a given Dictionary
# D1={'list1':[4,7,10,20],'list2':[7,16,9,10],'list3':[13,10,4,8],'list4':[7,20,6,11]}

D1={'list1':[4,7,10,20],
    'list2':[7,16,9,10],
    'list3':[13,10,4,8],
    'list4':[7,20,6,11]}
set1=set()

for x in D1.values():
    for y in x:
        set1.add(y)
print("unique values in the given dict", set1)