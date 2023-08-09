# program 7 :
    
lst_names = [ "name1", "name2", "name3", "name4", "name5" ]
lst_subjects = [ "OS", "DSA", "Maths", "History", "Chemistry" ]


# using for loops 

dict1 = {}

for x in range(len(lst_names)):
    dict1[lst_names[x]] = lst_subjects[x]
    
print(dict1)


# using dictonary comprehension

dict2 = { x : y for x,y in zip(lst_names, lst_subjects) }

print(dict2)