def swap(d1):
    return {value:key for key,value in d1.items()}

d1={'a': 1, 'b': 2, 'c': 3}
swapped_dict=swap(d1)
print("swapped dictionary:-", swapped_dict)