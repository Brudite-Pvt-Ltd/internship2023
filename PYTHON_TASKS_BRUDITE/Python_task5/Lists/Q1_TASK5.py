# 1. Remove an element from a list by its value

def ele_removed(list, val):
    if val in list:
        list.remove(val)
    return list