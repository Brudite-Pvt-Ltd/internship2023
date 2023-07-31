# Implement a function that takes a list of tuples,where each tuple contains a name and age,
# and returns the names of the three oldest people.

def old_person(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list[:3]

l = [('laksh', 30), ('nav', 20), ('ankita', 40), ('kanta', 50)]
print(old_person(l))