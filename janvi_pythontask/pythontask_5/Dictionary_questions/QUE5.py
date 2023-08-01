# Write a program to rename a key of a Dictionary.
def rename_key(dictionary, old_key, new_key):
    if old_key in dictionary:
        dictionary[new_key] = dictionary.pop(old_key)


dictionary = {'rajasthan': 10, 'uttarakhand': 5, 'sikar': 15, 'mumbai': 3}

# Rename 'sikkim' key to 'uttarpradesh'
rename_key(dictionary, 'mumbai', 'madhyapradesh')

# Output the updated dictionary
print("Updated dictionary after renaming:")
print(dictionary)