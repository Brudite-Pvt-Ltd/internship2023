dict={1: 'hello', 2: 'world', 3: 'namaste', 4: 'duniya'} #dictionary initialize

print(dict)  #print the dictionary items

dict2=dict.copy()  #copy the dictionary items
print(dict2)

dict[0]= 'I' #adding elements in the dictionary
print(dict)

dict.pop(3)  #removes the item with specifies key value
print(dict)

print(dict.get(1))  #gives value of the specified key

dict.update({2: 'earth'})  #update the value at specified key
print(dict)

dict.clear() #clears the dictionary
print(dict)