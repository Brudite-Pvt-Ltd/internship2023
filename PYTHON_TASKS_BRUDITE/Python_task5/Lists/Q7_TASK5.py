# Shuffle a list randomly withou tusing any built-in functions.


def shuf(List):
    import random
    newList=[]
    for i in List:
        i=random.randrange(len(List))
        newList+=i
    return newList
l1 = [1, 2, 3, 4, 5, 6, 7]
shuf(l1)