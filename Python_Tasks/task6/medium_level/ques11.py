
l = ['Red', 'Blue', 'Black', 'White', 'Pink']
l2 = list(map(lambda x: list(x), map(str, l)))
print(l2)
