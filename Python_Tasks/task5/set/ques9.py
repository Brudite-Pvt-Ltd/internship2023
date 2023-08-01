s1={3,4,6,5}
s2={5,6,3,4}
b=0
if len(s1)==len(s2):
    for x in s1:
        if x not in s2:
            b=1
else:
    b=1
if b==0 :
    print ("sets are equal")
else:
   print( "sets are not equal")           