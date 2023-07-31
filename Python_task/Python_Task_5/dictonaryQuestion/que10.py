"""
#10. Implement a function that takes a list of dictionaries, each representing a person's income and
expenses for a month. The keys in each dictionary are "name," "income, "and" expenses.
"Calculate the savings (income-expenses) for each person and return the result as a new dictionary with
the names as keys and savings as values"""



def take_list_of_dict(l):
    dict1 =dict()
    for x in l:
        dict1[x['name']]= (x['income']-x['expenses'])
    return dict1

def take_list_of_dict2(l):
    return {x['name']:x['income']-x['expenses'] for x in l }

        
l= [
    {"name": "John", "income": 5000, "expenses": 3000},
    {"name": "Alice", "income": 4500, "expenses": 4000},
    {"name": "Bob", "income": 6000, "expenses": 5500}
]
print(take_list_of_dict(l))
print(take_list_of_dict2(l))