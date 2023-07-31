#10. Write a Python program to find the intersection of two arrays (elements that are present in both arrays).

def array_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = set1.intersection(set2)
    return list(intersection)

aray1 = [1, 2, 3, 4]
aray2 = [4, 3, 7, 8]
res = array_intersection(aray1, aray2)
print(res)


