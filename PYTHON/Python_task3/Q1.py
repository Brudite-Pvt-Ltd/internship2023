#Q1. WAP to count all unique values in the list.

#method 1
list1 = [9,7,5,7,3,9]

set_method = set(list1)

c = len(set_method)
print(c)

#method2
 
list2 = [9,7,5,7,3,9]

unq_list = list()
unq_items = 0

for i in list1:
    if i not in unq_list:
        unq_list.append(i)
        unq_items += 1

print(unq_items)

#method 3

#list3 = [9,7,5,7,3,9]

dict = {'kuchbhi' : [9,7,5,7,3,9]}

unq_items = list({ele for val in dict.values() for ele in val})
count = len(unq_items)
print(count)