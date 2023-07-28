set = {"one","two","three","four"}

print(set)  #{'three', 'one', 'two', 'four'}
print(type(set)) #<class 'set'>
print(len(set)) #<class 'set'>


#1st Method 
#add() which is used to add elemetn
set.add("five") 
print(set) #{'three', 'one', 'two', 'four', 'five'}

#2nd Method
#To add items from another set into the current set, use the update() method.
set1 = {'first','second','third'}
set.update(set1)
print(set) # {'first', 'three', 'one', 'two', 'third', 'four', 'second', 'five'}
 #3rd Method
 # remove() remove the element from set
set.remove("one")
print(set) #{'five', 'three', 'third', 'four', 'second', 'first', 'two'}

#4th Method
#pop() remove a random item by using it 
set.pop()
print(set) #{'three', 'four', 'second', 'five', 'first', 'two'}

#5th method
# clear() this method empty the set
set.clear()
print(set) #set()
