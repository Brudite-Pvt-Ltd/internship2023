# Remove an element from a list by its value.

def remove_element(list1, value):
    if value in list1:
        list1.remove(value)
    return list1


list1 = [1,2,23,4,5,6,7]
value = 6
print(remove_element(list1, value))
