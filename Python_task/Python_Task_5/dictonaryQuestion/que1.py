#q1.Create two dictionaries, merge them into a new dictionary, with values from the second dictionary over writing those from the first in case of conflicts

dict1 = {'a': 10, 'b': 8,"s":32,"g":3}
dict2 = {'d': 6, 'c': 4,'s':5,"g":45}

dict3 ={}
for x,y in zip(dict1,dict2):
    dict3[x] = dict1[x]
    dict3[y] = dict2[y]
print(dict3)



dict1.update(dict2)
print(dict1)