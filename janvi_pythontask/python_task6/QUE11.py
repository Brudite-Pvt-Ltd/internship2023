#Write a Python program to create a list of given strings individually of the list using Python map function.
'''Eg.
Input: 
['Red', 'Blue', 'Black', 'White', 'Pink']
Output:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

'''

input_strings = ['Red', 'Blue', 'Black', 'White', 'Pink']

char_lists = list(map(list, input_strings))

print("Output:")
for char_list in char_lists:
    print(char_list)
