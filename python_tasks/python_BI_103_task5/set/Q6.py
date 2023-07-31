def check_disjoint_set(set1,set2):
    for x in set1:
        if x in set2:
            return ("not disjoint")
    return ("disjoint sets")
        
set1={1,2,3,4}
set2={5,6,7,8}
result=check_disjoint_set(set1,set2)
print(result)