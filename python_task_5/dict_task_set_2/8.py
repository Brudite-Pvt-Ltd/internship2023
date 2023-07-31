#8. Design a function that takes a list of dictionaries,each containing "name" and"salary" keys ,and returns the name of the employee with the highest salary.
def highest_sal(list):
    highest_salary = 0
    highest_salary_employee = None
    
    for x in list:
          if 'salary' in x and x['salary'] > highest_salary:
            highest_salary = x['salary']
            highest_salary_employee = x['name']
            
    return  highest_salary_employee
            
list=[{'name': 'ank','salary':75500},
       {'name': 'yaddu','salary':45000},
       {'name': 'vinit','salary':65000},
       {'name': 'goyal','salary':80000},
       {'name': 'sudhs','salary':860000}]
result=highest_sal(list)
print(result)