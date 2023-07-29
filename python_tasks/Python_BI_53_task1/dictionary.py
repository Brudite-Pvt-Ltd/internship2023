# get method 

my_dict = {'nav': 1, 'man': 2, 'laksh': 3}
a = my_dict.get('man', 0)
print(a) # Output: 2
b = my_dict.get('harsh', 0)
print(b)  # Output: 0

#items method
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])


#popitem method 3 remove the last item
my_dict = {'a': 1, 'b': 2, 'c': 3}
item = my_dict.popitem()
print(item)  # Output: ('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2}


#update method 4
my_dict = {'a': 1, 'b': 2}
my_dict.update({'b': 3, 'c': 4})
print(my_dict) # Output: {'a': 1, 'b': 3, 'c': 4}

#clear method 5
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}
