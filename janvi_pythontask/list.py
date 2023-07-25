#accessing item in a list.

list = ["janvi","lakshita","faisal"]
print(list[2])
print(list[-1])

#range of index
list = ["janvi","lakshita","faisal"]
print(list[1:3])

#change item value.
list = ["janvi","lakshita","faisal"]
list[2] = "shivi"
print(list)

#Insert Items
list = ["janvi","lakshita","faisal"]
list.insert(2,"siri")
print(list)

#Append Items
list = ["janvi","lakshita","faisal"]
list.append("siri")
print(list)

#To determine if a specified item is present in a list
if "janvi" in list:
    print("Yes, 'janvi' is in the list")

    #To clear the list
mylist=["apple","mango","cherry"]
print(mylist)
mylist.clear()
print(mylist)
