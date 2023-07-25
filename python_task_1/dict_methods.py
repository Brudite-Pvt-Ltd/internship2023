#2. Dictionaries:
ank_dict = {'apple': 1, 'banana': 2, 'orange': 3}

# 2.1. keys(): Get  list of all keys in the dictionary.
key_ls=ank_dict.keys()
print(key_ls)

# 2.2. values(): Get a list of all values in the dictionary.
val_ls=ank_dict.values()
print(val_ls)

# 2.3. items(): Get a list of key-value pairs in the dictionary.
item_ls=ank_dict.items()
print(item_ls)

# 2.4. get(): Retrieve the value for a given key. 
apple_value = ank_dict.get('apple', 0)
print(apple_value)
banana_value = ank_dict.get('banana', 1)
print(banana_value)

# 2.5. pop(): Remove and return the value for a given key.
remove_item = ank_dict.pop('banana')
print(remove_item)


