#Write a Python program to find the intersection of two arrays (elements that are present in both arrays).

def array_intersection(a,b):
    s1 = set(a)
    s2 = set(b)
    intersection = s1.intersection(s2)
    return list(intersection)
a = [1,2,3,4,5]
b = [3,5,7,8,9]
res = array_intersection(a,b)
print(res)