#2.Create a set with elements from 1 to 10. Check if it is a super set of {2,4,6}

created_set = {1,2,3,4,5,6,7,8,9,10}
Given_set = {2,4,6}

#Method 1
if Given_set == Given_set.intersection(created_set):
    print("created set",created_set," is a superset of set",Given_set)
else:
    print("created set ",created_set,"is not a superset of ",Given_set)
#Method 2
print(created_set.issuperset(Given_set))#Returns true is set is superset otherwise false
