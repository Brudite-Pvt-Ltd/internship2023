# -*- coding: utf-8 -*-
"""
Q2.list1=[[2,4],[7,8],[9,10]]
list2=[[4,2],[8,9],[9,10]]
Find all the uncommon pairs
"""

    
# lists
l1 = [[2,4],[3,2],[7,8],[9,10],[5,6]]
l2 = [[4,2],[2,3],[8,9],[9,10],[6,7]]

#empty list
l3 = []
for x in l1:
    if x not in l2  and x[: : -1] not in l2:
        l3.append(x)

for x in l2:
    if x not in l1  and x[: : -1] not in l1:
        l3.append(x)
        
print(l3)