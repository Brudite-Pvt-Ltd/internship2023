def get_key(d, value):
    for k, v in d.items():
        if v==value:
            return k
    return None
d = {'a':1, 'b':2, 'c':3, 'd':4}
key = get_key(d, 2)
key = get_key(d, 4)
print(key)