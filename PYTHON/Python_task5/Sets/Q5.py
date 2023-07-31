# Create a function that takes two sets and returns their Cartesian product as a set of tuples.

def cartesian_product(set1, set2):
    cartesian_set = set()
    for i in set1:
        for j in set2:
            cartesian_set.add((i,j))
    return cartesian_set

set1 = {1,2,3}
set2 = {'x','y'}
result = cartesian_product(set1, set2)
print(result)

