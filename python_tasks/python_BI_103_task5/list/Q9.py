
def old_person(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list[:3]

l = [('laksh', 21), ('nav', 22), ('harsh', 19), ('ritvik', 23)]
print(old_person(l))