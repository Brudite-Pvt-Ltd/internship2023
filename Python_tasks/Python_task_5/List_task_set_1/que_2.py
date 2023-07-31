# program 2 : create a new list of unique elements from existing list.

# creating a new list 
l = [1, 1, 2, 3, 1, 4, 4, 4, 4, 4]

# defining new_list
new_unique_list = []


# itrating in list l
for x in l :
    
    # checking for element in new_unique_list
    if x not in new_unique_list :
        new_unique_list.append(x)
        

# printing the new_list        
print(new_unique_list)

