def highest_sal(list1):
    highest_salary = 0
    highest_paid_employee = None
    
    for x in list1:
          if 'salary' in x and x['salary'] > highest_salary:
            highest_salary = x['salary']
            highest_paid_employee = x['name']
            
    return  highest_paid_employee
            
list1=[{'name': 'nav','salary':65500},
       {'name': 'harsh','salary':45000},
       {'name': 'laksh','salary':65000},
       {'name': 'mani','salary':80000},
       {'name': 'ritvik','salary':70000}]
result=highest_sal(list1)
print(result)
