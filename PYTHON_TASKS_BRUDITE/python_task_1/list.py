# LIST OPERATIONS

# For printing a list
mylist = [True, 55, "Namaste world"]
print(mylist)

#For accessing a list
mylist= ["Hello", 99,"World"]
print(mylist[2])

#To determine if a specified item is present in a list
if "Hello" in mylist:
    print("Yes, 'Hello' is in the list")

#To change the values of any item in a list
mylist=["cow", "moneky", "cat"]
print(mylist)
mylist[0]= "dog"
print(mylist)

#To insert a new list item
mylist= ["black", "yellow", "green"]
print(mylist)
mylist.insert(2,"blue")
print(mylist)

#To add an item to the end of the list
mylist=["Red","Green","Blue"]
print(mylist)
mylist.append("orange")
print(mylist)

#To clear the list
mylist=["apple","mango","cherry"]
print(mylist)
mylist.clear()
print(mylist)

#TO REVERSE ITEMS OF LIST
mylist.reverse()
print(mylist)

#TO COPY ITEMS OF A LIST
mylist.copy()

#TO SORT A LIST
mylist.sort()
print(mylist)
