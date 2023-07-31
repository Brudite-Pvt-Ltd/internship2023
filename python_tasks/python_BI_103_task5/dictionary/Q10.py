def palindrome_dict(d):
    new_dict = {}
    for key, value in d.items():
        if key.lower() == key[::-1].lower():
            new_dict[key] = value
    return new_dict

d = {'navan' : 1 , 'pop' : 2 , 'preet' : 3}
print(palindrome_dict(d))