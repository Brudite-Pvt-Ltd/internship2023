dict = {"one" :"first","two" :"second","three":"third"}

print(dict)       # {'one': 'first', 'two': 'second', 'three': 'third'}
print(len(dict))  # 3
print(type(dict)) #<class 'dict'>

#1st Method
# to get all the key and value in the dictonary use keys() method and values() method respectively.
key = dict.keys()
print(key)  #dict_keys(['one', 'two', 'three'])
value = dict.values() #dict_values(['first', 'second', 'third'])
print(value) 

#2nd Method
#add or update a  key and value to a dict then see that the key is also a updated
dict["four"] = "fourth"
dict.update({"five":"fifth"}) 
print(dict) # {'one': 'first', 'two': 'second', 'three': 'third', 'four': 'fourth', 'five': 'fifth'}
print(key)  # dict_keys(['one', 'two', 'three', 'four', 'five'])

#3rd Method
# a pop() method is used to remove a item from dictonary 
a = dict.pop("five")
print(a) #fifth a contains value of delted item
print(dict) #{'one': 'first', 'two': 'second', 'three': 'third', 'four': 'fourth'} deleted fifth give value

#4th method
# get() return the value of the item with specifed key
print(dict.get("two")) # Second

#5th Method
#copy() method is used to copy the dictionary 
dict1 = dict.copy()
print(dict1) # {'one': 'first', 'two': 'second', 'three': 'third', 'four': 'fourth'}
