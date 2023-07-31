#3.Extract unique values in a given Dictionary 
# D1={'list1':[4,7,10,20],
#     'list2':[7,16,9,10],
#     'list3':[13,10,4,8],
#     'list4':[7,20,6,11]}

D1={'list1':[4,7,10,20],
     'list2':[7,16,9,10],
     'list3':[13,10,4,8],
     'list4':[7,20,6,11]}

new_list = []
for key in D1:
    new_list.extend(D1[key])
print(new_list)
unique_set = set(new_list)
print("unique_value:",unique_set)




