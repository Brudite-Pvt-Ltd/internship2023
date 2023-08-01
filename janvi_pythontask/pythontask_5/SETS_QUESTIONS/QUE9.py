#9.Write a program to check, two sets are equal or not .
def sets_are_equal(set1,set2):
    return set1 == set2

set1 = {1,2,3,4,5}
set2 = {5,8,2,1,4}

if sets_are_equal(set1,set2) :
    print("sets are equal")
else:
    print("sets are not equal")