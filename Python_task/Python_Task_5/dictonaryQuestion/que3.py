#3.Write a python program to get keys with maximum and minimum value in a Dictionary

dict1 ={'a':4,'b':8,'d':4,'n':6,'n':9,'q':1,'o':10}

key_list = list(dict1.keys())
value_list = list(dict1.values())

maxvalue = [x for x in dict1 if dict1[x]==max(value_list)]
print("key having maximum value",maxvalue)

minvalue = [x for x in dict1 if dict1[x]==min(value_list)]
print("key having minimum value",minvalue)

maxindex = value_list.index(max(value_list))
minindex = value_list.index(min(value_list))
print("Key with max value is",key_list[maxindex])
print("Key with min value is",key_list[minindex])
    
