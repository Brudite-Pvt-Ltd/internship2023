#DICTIONARY OPERATIONS

#CREATING AND PRINTING A DICTIONARY
mydict = {
    "age" : 20,
    "class" : 12,
    "name" :"Faisal"
}
print(mydict)

#ACCESSING DICTIONARY ITEMS
x = mydict["name"]
print(x)
x=mydict.get("age")
print(x)

#TO GET ALL KEYS
x=mydict.keys()
print(x)

#TO GET ALL THE VALUES
x=mydict.values()
print(x)

#TO CHECK IF KEY IS PRESENT
if "age" in mydict:
    print("YES, age is present")
    
#TO CHANGE THE VALUE OF ANY KEY
mydict["name"]= "Fizz"
print(mydict)

#TO REMOVE A SPECIFIED ITEM
mydict.pop("age")
print(mydict)

