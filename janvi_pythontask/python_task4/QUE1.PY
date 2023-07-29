#candidate = [[(2001,Name,aadhar,pan),[designation,experience,email,address,phone]]]

candidate = [
    [ (2001, 'Rahul', "1234322341", "HQ255234WQ"),
        ["Software Engineer", 3, "rahul@gmail.com", "302022", "9877656723"]],
        [ (2002, 'Tina', "9873452345", "HQ235534WQ"),
        ["Manager", 4, "Tina@gmail.com", "302020", "9878776723"]],
        [ (2003, 'Tanya', "9876752345", "HQ233334WQ"),
        ["Team Lead", 2, "Tanya@gmail.com", "302010", "9898646723"]],
        [ (2004, 'Ram', "9873452309", "HQ238834WQ"),
        ["Manager", 3, "Ram@gmail.com", "302012", "9879895723"]],
        [ (2005, 'Rishav', "945672345", "HQ230034WQ"),
        ["Software Engineer", 5, "Rishav@gmail.com", "302012", "9879879876"]],
        [ (2006, 'Lakshita', "9873458976", "HQ211234WQ"),
        ["Software Engineer", 6, "Lakshita@gmail.com", "302022", "9879874274"]],
        [ (2007, 'Navpreet', "9873452123", "HQ554234WQ"),
        ["Manager", 7, "Navpreet@gmail.com", "302010", "9879872829"]],
        [ (2008, 'Vipul', "9873872345", "HQ774234WQ"),
        ["Associate Developer", 3, "Vipul@gmail.com", "302023", "987957423"]],
        [ (2009, 'Vaibhav', "9873452312", "HQ256234WQ"),
        ["Software Engineer", 4, "Vaibhav@gmail.com", "302014", "9879876723"]],
        [ (2010, 'Janvi', "9873452529", "HQ223754WQ"),
        ["Associate Developer", 8, "Janvi@gmail.com", "302016", "9879876723"]]
]
'''Question 1: find list of all the Managers, Software Engineers, 
Team Lead and Associate Developer.
Question 2:  find list of all candidates having experience more than 5.
Question 3: find list of all candidate with pin = 302012.
Question 4: Update all the emails of employee with company domain name 
emails.
Question 5: Add a Base Salary as 10k for managers, 20k for software 
engineers, 5k for associate developers, 12k for Team lead.
Question 6: Find the Highest Salary in all Designations.
Question 7: Find the Aggregate of salaries of Managers, Software Engineers, 
Team Lead and Associate Developer.
Question 8: Find all the employees with pincode near by in range +-10.
means -> if the input is 302015 then range upto 302005 to 302025 will be filtered.
Question 9: Create a Dictionary with Tuple as Key and List[1] as value.
Question 10: Create a Contact Directory where people 
can search phone numbers through name or ID.
 '''
managers = list(filter(lambda x:x[1][0]=="Manager",candidate))
print(managers)
SoftwareEngineer = list(filter(lambda x:x[1][0]=="Software Engineer",candidate))
print(SoftwareEngineer)
TeamLead= list(filter(lambda x:x[1][0]=="Team Lead",candidate ))
print(TeamLead)
AssociateDeveloper= list(filter(lambda x:x[1][0]=="Associate Developer",candidate))
print(AssociateDeveloper)

#QUE2. Find list of all the candidates having expirence more than 5
experience_more_than_5 = list(filter(lambda x:x[1][1]>5,candidate))
print(experience_more_than_5)

#QUE3. Find list of all the candidates with pan = 302012.
pan_candidates= list(filter(lambda x:x[1][3]=="302012",candidate))
print(pan_candidates)

#QUE4. Find list of all the emails of employeee with  Company domian name emails .  
emails= list(map(lambda x: x[1][2],filter(lambda x: x[1][2].replace("@","company@",),candidate)))
print(emails)




update_email = lambda emp: (emp[0], [emp[1][0], emp[1][1], emp[1][2].replace("@", "@company"), emp[1][3], emp[1][4]])
candidate_with_company_emails = list(map(update_email, candidate))
print(candidate_with_company_emails )


'''#question 5 : adding a base salary'''


def update(i):
  if i[1][0] == "Manager":
        return int(10000)
  elif i[1][0] == 'Associate Developer':
        return int(5000)
  elif i[1][0] == 'Software Engineer':
        return int(20000)
  elif i[1][0] == 'Team Lead':
        return int(12000)


adding_salary = list( map(lambda i : i[1].append(update(i)) or i  , candidate) )
for i in adding_salary :
    print(i)
  




# importing reduce
from functools import reduce

# using reduce to find the maximum salary in all 
max_salary = reduce(lambda x, y : x if x[1][5] > y[1][5] else y  , candidate)
print("max_salary  : ", max_salary[1][5])
print("Designation : ", max_salary[1][0])



# Dictionary to store the aggregate of designations
designation_aggregate = {}

# Iterate through the candidate list
for candidate_info in candidate:
    designation = candidate_info[1][0]  # Get the designation from the inner list
    if designation in designation_aggregate:
        designation_aggregate[designation] += 1
    else:
        designation_aggregate[designation] = 1

# Print the aggregate
for designation, count in designation_aggregate.items():
    print(f"{designation}: {count}")
#QUE8
pincode = 302012
emp = list(filter(lambda x: (pincode-10) < int(x[1][3]) and (pincode+10) > int(x[1][3])  , candidate))
for x in emp:
    print(x)


dic = {x[0] : x[1] for x in candidate}
for key, val in dic.items() :
    print( key , " : ", val)
    
#Que10 create a contact Directory where people can search phone numbers through name  or ID.
contact_directory = [([x[0][0],x[0][1],x[1][4]]) for x in candidate]
print(contact_directory)
    