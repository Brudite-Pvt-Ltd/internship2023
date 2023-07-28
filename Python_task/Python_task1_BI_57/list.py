list = ['mango','apple','banana','grapes']


print(list)
print(len(list))
print(type(list))

#1st method
#insert() method is used for update and insert a new element in list
list.insert(3,"pyaz")
print(list) #['mango', 'apple', 'banana', 'pyaz', 'grapes']
list.insert(5,"bhindi")
print(list) #['mango', 'apple', 'banana', 'pyaz', 'grapes', 'bhindi']

#2nd Method
#append() method is used to add a new elemet in list
list.append("masala")
print(list) #['mango', 'apple', 'banana', 'pyaz', 'grapes', 'bhindi', 'masala']

#3rd Method
#extend() Method is used to merge two different list
list1 =('knife','gas','kadai')
list.extend(list1)
print(list) #['mango', 'apple', 'banana', 'pyaz', 'grapes', 'bhindi', 'masala', 'knife', 'gas', 'kadai']

#4th Method
# sort() method is used to sort the list
list.sort()
print(list) # ['apple', 'banana', 'bhindi', 'gas', 'grapes', 'kadai', 'knife', 'mango', 'masala', 'pyaz']

#5th method
#copy()  method is used to copy the list
list1 = list.copy()
print(list1) #['apple', 'banana', 'bhindi', 'gas', 'grapes', 'kadai', 'knife', 'mango', 'masala', 'pyaz']