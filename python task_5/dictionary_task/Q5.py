def rename_key(d, old_key, new_key):
    if old_key in d:
        d[new_key] = d.pop(old_key)
    return d
d = {'a':1, 'b':2, 'c':3, 'd':4}
d = rename_key(d, 'a', 'x')
print(d)