def get_max_min_keys(d):
    max_val = max(d.values())
    min_val = min(d.values())
    max_keys = [k for k, v in d.items() if v==max_val]
    min_keys = [k for k, v in d.items() if v==min_val]
    return max_keys, min_keys

d = {'a':1, 'b':2, 'c':3, 'd':1}
max_keys, min_keys = get_max_min_keys(d)
print("Keys having maximum values: ", max_keys)
print("Keys having minimum values: ", min_keys)
