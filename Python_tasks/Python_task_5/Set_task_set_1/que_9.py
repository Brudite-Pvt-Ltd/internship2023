# program 9 : check if two sets are equal or not 

# creating two sets

set1 = {1, 2, 3, 4, 5}
set2 = {2, 1, 4, 3, 5}

# method 1 : using == operater 

if set1 == set2 :
    print("sets are equal!")
else:
    print("sets are not equal!")
    
    
# method 2 : using symetirc difference

if  len( set1.symmetric_difference(set2) ) == 0 :
    print("sets are equal!")
else:
    print("sets are not equal!")
    