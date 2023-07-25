dict = {'aaa': 1, 'bbb': 2, 'ccc': 3}  #1 pop

removed = dict.pop('bbb')
print(removed)   
print(dict)         

                                       
dict2 = {'ccc': 3, 'ddd': 4}           #2 update
dict.update(dict2)
print(dict)

keys = dict.keys()
values =dict.values()                 #3 key and values
items = dict.items()

print(keys)  
print(values)
print(items)



value = dict.get('aaa')             #4 get
print(value)


default =0                          #5 formkeys
DICT=dict.fromkeys(keys, default)
print(DICT)



