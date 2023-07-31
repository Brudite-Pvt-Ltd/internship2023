# Shuffle a list randomly without using any built-in functions.
import random

def shuffle(list):
    x=len(list)
    for i in range(x - 1):
        j = random.randint(i, x- 1)
        list[i], list[j] = list[j], list[i]
    return list

list = [1,2,3,4,5]
print(shuffle(list))