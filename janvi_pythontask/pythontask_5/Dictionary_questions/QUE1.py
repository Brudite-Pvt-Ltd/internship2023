#1.Create two dictionaries,merge them into a new dictionary,with values from the second dictionary over writing those from the first in case of conflicts
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example dictionaries
dict1 = {'janvi': 21, 'shivamat': 24, 'jaipur': 22}
dict2 = {'buzzz': 25, 'harshit': 20, 'jodhpur': 22}

# Merge the dictionaries
result_dict = merge_dictionaries(dict1, dict2)

print("Merged dictionary with values from the second dictionary overwriting the first:", result_dict)