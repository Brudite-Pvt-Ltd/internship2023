# program 2 : Check for subset 


# creating a set with elements 1 to 10
s = { x for x in range(11) }


# creating subSet
sub_s = {2, 4, 6}


# checking
if ( s.issuperset(sub_s) ):
    print("Yes it's superSet")
else :
    print("No it's not superSet")