# create dictonary in python

Dict = {1: 'code', 2: 'run', 3: 'expriment'}
print(Dict)

# accessing a element from a Dictionary
Dict = {1: 'play', 'number': 'for', 3: 'results'}
  
print("Accessing a element using key:")
print(Dict['number'])
print("Accessing a element using key:")
print(Dict[1])


#Deleting Elements using del Keyword
Dict = {1: 'study', 'smart': 'For', 3: 'score'}
  
print("Dictionary =")
print(Dict)

del(Dict[1]) 
print("Data after deletion Dictionary=")
print(Dict)


# Accessing element using key
print(Dict['Dictionary1'])
Dict = {'Dictinary1': {1: 'simran'},
		'Dictinary2': {'Name': 'For'}}

print(Dict['Dictinary1'])
print(Dict['Dictinary1'][1])
print(Dict['Dictinary2']['Name'])

#some more dict operation 

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)

dict1.clear()
print(dict1)

print(dict2.get(1))

dict2.pop(4)
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
  
print(dict2.values())
