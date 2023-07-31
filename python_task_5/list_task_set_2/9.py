#9.Implement a function that takes a list of tuples, where each tuple contains a name and age, and returns the names of the three oldest people.
def old_person(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list[:3]

list = [('laksh', 21), ('nav', 22), ('ankita',19), ('mohit',25)]
print(old_person(list))