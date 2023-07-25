# 3. Sets:
ank_set = {16,22,10,1,4}

# 3.1. add(): Add an element to the set.
ank_set.add(15)
print(ank_set)

# 3.2. remove(): Remove an element from the set.
ank_set.remove(15)
print(ank_set)

# 3.3. discard(): Remove a specific element from the set if it exists, but do nothing if it does not.
ank_set.discard(89)
print(ank_set)
ank_set.discard(16)
print(ank_set)

# 3.4. union(): Create a new set that contains all elements from two sets (no duplicates).
new_set={1,2,3,4,5}
union_set=ank_set.union(new_set)
print(union_set)

# 3.5. intersection(): Create a new set that contains elements that exist in both sets.
intersect_set=ank_set.intersection(new_set)
print(intersect_set)








