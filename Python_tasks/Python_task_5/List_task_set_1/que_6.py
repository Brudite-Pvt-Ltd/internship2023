# program 6 : program to find intersection between two lists


# creating two lists 
l1 = [1, 2, 3, 4, 5, 6]
l2 = [4, 5, 6, 7, 8, 9]


# creating a new list to store the intersection
intersection = [] 

for x in l1 :
    
    # if the element is present in second list then, storing it.
    if x in l2 :
        intersection.append(x)


print(intersection)