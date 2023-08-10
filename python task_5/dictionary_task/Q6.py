def sort_age(people):
    sorted_people = sorted(people, key = lambda p:p['age'])
    return sorted_people

people = [
    {'name' : 'Shivani', 'age':21},
    {'name' : 'Ravikant', 'age':22},
    {'name' : 'vikas', 'age':20},
    {'name' : 'vishal', 'age':23},
    {'name' : 'ojal', 'age':20}
]
sorted_people = sort_age(people)
print(sorted_people)