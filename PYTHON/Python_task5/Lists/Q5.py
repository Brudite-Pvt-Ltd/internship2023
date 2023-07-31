# Split a list into evenly sized chunks.

def split(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]

list = [1,3,5,7,9,11]
n = 3   #this is chunk size
print(split(list, n))
