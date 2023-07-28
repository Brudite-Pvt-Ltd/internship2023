# 1. upadate() 
		
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  
	
# Output: {1, 2, 3, 4, 5}

	
# 2. symmetric_difference_update()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  

# Output: {1, 2, 4, 5}


# 3. pop()

my_set = {1, 2, 3, 4, 5}
popped_element = my_set.pop()
print(popped_element)  

# Output: (an arbitrary element, e.g. in my case : 1)


# 4. issubset()

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
result = set1.issubset(set2)
print(result)  

# Output: True


# 5. isadjsubset()

set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  

# Output: True
