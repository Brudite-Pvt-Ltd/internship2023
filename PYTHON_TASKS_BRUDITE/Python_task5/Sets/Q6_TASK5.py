# Q6. Write a function to check if two sets are disjoint.

def disjoint_set(set1,set2):
    for x in set1:
        if x in set2:
            return ("not disjoint")
    return ("disjoint sets")
        