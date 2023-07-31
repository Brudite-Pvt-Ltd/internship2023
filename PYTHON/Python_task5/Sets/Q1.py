# Create a set with elements from 1 to 10 . Check if it is a subset of {0,5,10,15}.

def kya_substring_h(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {0,5,10,15}

print(kya_substring_h(set1, set2))