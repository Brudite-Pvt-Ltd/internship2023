#print this dictionary
dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  :  1987
}
print(dict) 
#change values
dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  :  1987
}
dict["year"]=2013
print(dict) 
#update dictionary
dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  :  1987
}
dict.update({"brand":"audi"})
print(dict) 
#add items
dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  :  1987
}
dict["color"] = "red"
print(dict) 
#Removing Items

dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  :  1987
}
dict.popitem()
print(dict) 
#The del keyword removes the item with the specified key name:
dict = {
    "brand" : "ford",
    "model" : "mustang",
    "year"  :  1987
}
del dict["model"]
print(dict) 


#TO GET ALL THE VALUES
x=dict.values()
print(x)

#TO COPY DICTIONARY ITEMS
dict2=dict.copy()
print(dict2)

#TO CHECK IF KEY IS PRESENT
if "age" in dict:
    print("YES, age is present")





