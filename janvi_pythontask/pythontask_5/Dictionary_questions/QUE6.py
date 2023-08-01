''' Create a list of Dictionary , each containing “name“ and “age” Keys, 
 sort the list based on the ages of the people in ascending order '''

def sort_by_age(people_list):
    return people_list['age']

#list of dictionaries
people_list = [
    {'name': 'janvi', 'age': 21},
    {'name': 'bob', 'age': 20},
    {'name': 'ram', 'age': 22},
    
]

# Sort the list based on ages in ascending order
sorted_people_list = sorted(people_list, key=sort_by_age)

print("Sorted list of people based on age:", sorted_people_list )
