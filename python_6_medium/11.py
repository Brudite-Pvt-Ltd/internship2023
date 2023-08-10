# 11. Write a Python program to create a list of given strings individually of the list using Python map function.
# Eg.
# Input: 
# ['Red', 'Blue', 'Black', 'White', 'Pink']
# Output:
# [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]
input = ["Red", "Blue", "Black", "White", "Pink"]
output = list(map(lambda x: list(x), input))
print(output)
