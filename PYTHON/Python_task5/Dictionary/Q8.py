# Design a function that takes a list of dictionaries,each containing "name" and "salary" keys,
# and returns the name of the employee with the highest salary.

def salary(Dict):
    highest_salary = Dict[0]
    for i in Dict:
        if i["salary"] > highest_salary["salary"]:
            highest_salary = i
    return highest_salary["name"]

employees = [
    {"name": "John", "salary": 100000},
    {"name": "Mary", "salary": 200000},
    {"name": "Peter", "salary": 300000}]

print(salary(employees))