""" 
    method 1 - brute force 

"""


# creating two lists
list1 = [[2, 4], [7, 8], [9, 10]]
list2 = [[4, 2], [9, 10], [8, 9]]


uncommon_element = []

# applying for each loop on one list and checking that "is it in second link ?"
# and also checking it's reverse also because [2, 4] == [4, 2]

for x in list1 :
    if ((x not in list2) and (x[::-1] not in list2)) :
        uncommon_element.append(x)


# similliarly checking for the list 2
        
for x in list2 :
    if ((x not in list1) and (x[::-1] not in list1)) :
        uncommon_element.append(x)
        

print("uncommon elements =", uncommon_element)



"""
    method 2 - using set and tupple

"""


# creating set of tupples 
s1 = { tuple(sorted(x)) for x in list1 }
s2 = { tuple(sorted(x)) for x in list2 }

# using symetric_difference set function to find the uncommon elements 

uncommon_element = [ list(x) for x in s1.symmetric_difference(s2)]
print( "uncommon_elements =", uncommon_element)
