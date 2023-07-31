# Remove an element from a list by its value.

def ele_removed(list, val):
    if val in list:
        list.remove(val)
    return list

def ele_remove_2(list, val):  #method 2
    index = list.index(val)
    list.pop(index)
    return list

list = [1,3,5,7,9]
value = 5
print(ele_removed(list, value))
# print(ele_remove_2(list, value)) method 2 output