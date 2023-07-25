# Dictionary :-

# 1. get()
	 
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict.get('b', 0)
print(value)  

# Output: 2


# 2. setdefault()

my_dict = {'a': 1, 'b': 2}
value = my_dict.setdefault('c', 3)
print(my_dict)  					# Output: {'a': 1, 'b': 2, 'c': 3}
print(value)    					# Output: 3


# 3. items()

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  

# Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 4. formkeys()

keys = ['a', 'b', 'c']
default_value = 0
my_dict = dict.fromkeys(keys, default_value)
print(my_dict)  

# Output: {'a': 0, 'b': 0, 'c': 0}


# 5. popitem()

my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_item = my_dict.popitem()
print(popped_item)  

# Output: ('c', 3) (in Python 3.7+)
