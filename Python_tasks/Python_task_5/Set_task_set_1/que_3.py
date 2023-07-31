# program 3 : make a set immutable

# creating a set
s = {1, 2, 3, 4, 5}


# making it immutable with frozenset
immu_set = frozenset(s)


# tring to add new element to immu_set
# immu_set.add(6)
# immu_set.remove(3)
# as we know it will give us error

# we cannot add, remove, update in frozent set

print(immu_set)
