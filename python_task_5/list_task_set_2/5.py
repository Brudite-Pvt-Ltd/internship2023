#5.Split a list in to evenly sized chunks
def split(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]

list = [1,3,5,7,9,11]
n = 2
print(split(list, n))
