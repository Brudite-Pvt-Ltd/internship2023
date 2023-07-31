# Write a program that removes duplicate values from a dictionary, keeping only the first occurrence
# of each value.

def swap(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

def rm_duplicate(dict):
    new_dict = {}
    for k, v in dict.items():
        if v not in new_dict:
            new_dict[v] = k
    return swap(new_dict)

dict = {"key1": 10, "key2": 15, "key3": 10, "key4": 5}
print(rm_duplicate(dict))