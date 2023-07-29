#Question 6------------------------------------------------

list=[(1,2),(2,4),(4,5),(4,2),(1,2)]
set=set()
for x in list:
    if x is not set:
       set.add(tuple(sorted(x)))

print(set)