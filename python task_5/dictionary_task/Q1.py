def merge_dict(dict1, dict2): 
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 5, 'c': 6, 'e': 7}
merged_dict = merge_dict(dict1, dict2)
print(merged_dict)