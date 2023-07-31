# Create a function that takes a dictionary and returns a new dictionary where the keys and values
# are swapped.

def swap(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

dict = {'a': 10, 'b': 2, 'c': 20}
print(swap(dict))