# Write a function to check if two sets are disjoint

def is_disjoint(set1, set2):
    for i in set1:
        for j in set2:
            if i==j:
                return False
        else:
            return True
            

set1 = {1,2,3}
set2 = {4,5,6}
set3 = {1,3,5}

print(is_disjoint(set1, set2))
print(is_disjoint(set1, set3))