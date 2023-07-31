# program 4 : removing the max element from set without max function 

# creating a new set s 
s = {1, 2, 3, 4, 5, 6, 7}


# finding the max element (Iterating in set)
mx = -1e9

for x in s:
    if x > mx:
        mx = x 
    

# removing the element 
s.remove(mx)


# set after removing the max element 
print(s)
