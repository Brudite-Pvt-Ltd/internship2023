'''Write a Python program to create a list of given strings individually of the list using Python map function.
Eg.
Input: 
['Red', 'Blue', 'Black', 'White', 'Pink']
Output:
[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]'''


input_list = ["Red", "Blue", "Black", "White", "Pink"]
list_of_strings = list(map(lambda x: list(x), input_list))
print(list_of_strings)

