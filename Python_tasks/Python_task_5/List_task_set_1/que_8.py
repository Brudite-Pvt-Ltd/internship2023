# program 8 : 
    
from functools import reduce

#creating a list 
l = [1, 2, 3, 4, 5]

multi = reduce( lambda x,y : x*y , l )

# using list compr. to creating the new_list 
new_list = [ multi/x if x != 0 else None  for x in l]

print(new_list)