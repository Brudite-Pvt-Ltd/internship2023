# program 1 :

import os

file = open(os.path.dirname(__file__) + "\doc.txt")
f = file.read().split()

even_len_str = list(filter(lambda x : len(x)%2 == 0, f))

print(even_len_str)