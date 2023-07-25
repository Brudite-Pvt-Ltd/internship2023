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

list = [1,2,3,]
list2 = [4,5,6]
t = (list,list2)
print(t)
set = {2,2,3,4,5}
set(0)