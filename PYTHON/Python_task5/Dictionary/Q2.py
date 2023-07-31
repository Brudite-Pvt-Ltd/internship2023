# Write a program to rename a key in dictionary

def rename(dict,key,new_key):
    dict[new_key] = dict[key]
    del dict[key]
    return dict

dictionary = {"key1": "value1", "key2": "value2"}
print(rename(dictionary,"key1","naya_key"))