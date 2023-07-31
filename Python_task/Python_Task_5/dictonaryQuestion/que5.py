#5.Write a  program to rename a key of a Dictionary


dict1 ={'a':4,'b':8,'d':4,'t':6,'n':9,'q':1,'o':10}

key_rename = 'b'
renamed_key = 'c'
dict1[renamed_key] = dict1.pop(key_rename)
print(dict1)
renamed_key ='f'
key_rename ='t'

dict2={renamed_key if x==key_rename else x:y for x,y in dict1.items()}
print(dict2)


# dict1[renamed_key] = dict1[key_rename]
# del dict1[key_rename]
# print(dict1)