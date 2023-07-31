def cartesian_product(set1, set2):
    result = set()

    for i in set1:
        for j in set2:
            result.add((i, j))

    return result

set1 = {1,2}
set2 = {3,4,5}
result = cartesian_product(set1, set2)
print(result)  
