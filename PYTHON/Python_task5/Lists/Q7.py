# Shuffle a list randomly without using any built-in functions.
import random

def shuffle(list):
    for i in range(len(list) - 1):
        j = random.randint(i, len(list) - 1)
        list[i], list[j] = list[j], list[i]
    return list

list = [1,2,3,4,5]
print(shuffle(list))