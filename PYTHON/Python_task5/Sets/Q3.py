# Create a set of all the characters in the string "python programming".

def set_char(string):
    all_char = set()
    for c in string:
        all_char.add(c)
    return all_char

print(set_char("python programming"))