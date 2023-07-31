# Create a set and repeatedly add an element until it reaches a size of 10.

def add_ele_set(size):
    s = set()
    for i in range(size):
        s.add(i)
    return s

set = add_ele_set(10)
print(set)
    