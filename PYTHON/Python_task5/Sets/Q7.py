# Create a set of random integers and sort them in ascending order.

def sort_ascending(set1):
    sorted_set = set()
    for i in set1:
        sorted_set.add(i)     #sets are inherently sorted
    return sorted_set 

set1 = {9,5,2,1,6,3,8,4,7,10}
print(sort_ascending(set1))

