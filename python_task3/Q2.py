#Question 2--------------------------------------------
def find_uncommon_pairs(list1, list2):
    uncommon_pairs = [pair for pair in list1 if pair not in list2] + [pair for pair in list2 if pair not in list1]
    return uncommon_pairs


list1 = [[2, 4], [7, 8], [9, 10]]
list2 = [[4, 2], [8, 9], [9, 10]]

set1 = set()  

uncommon_pairs = find_uncommon_pairs(list1, list2)

for pair in uncommon_pairs:
    set1.add(tuple(sorted(pair)))

print("Uncommon pairs:")
for pair in set1:
    print(pair)