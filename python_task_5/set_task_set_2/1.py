# 1.Create a set with elements from 1 to 10.Check if it is a subset of {0,5,10,15}.
set = {1, 2, 3, 4, 5, 6, 7, 8, 9 ,10,}
print(set)
another_set = {0, 5, 10, 15}
print(another_set)
if set .issubset(another_set):
    print("this is subset of set")
else:
    print("this is not subset of set")