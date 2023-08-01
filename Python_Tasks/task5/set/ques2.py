s1={1,2,3,4,5,6,7,8,9,10}
s2={2,4,6}
b=0
for x in s2:
    if x not in s1:
        b=1
if (b==0):
    print("yes set1 is superset of ", s2)
else:
     print("no set1 is not superset of ", s2)
        