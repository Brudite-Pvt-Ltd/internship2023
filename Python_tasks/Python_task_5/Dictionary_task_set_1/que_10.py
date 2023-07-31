# program 10 :
    

l = [
    {"name": "isagi", "income": 50, "expenses": 20},
    {"name": "baru", "income": 100, "expenses": 49},
    {"name": "nagi", "income": 87, "expenses": 20},
    {"name": "rio", "income": 44, "expenses": 12}
]

new_dict = {}

for x in l :
    new_dict[x["name"]] = x["income"] - x["expenses"]
    

print(new_dict)