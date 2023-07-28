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
'''QUE1. find the list of all the managers,software Engineers ,Team Lead , Associate Developer
QUE2. Find list of all the candidates having expirence more than 5
 QUE3. Find list of all the candidates with pan = 302012.
 QUE4.update all the emails of employeee with  Company domian name emails .  
 QUE5. Add a Base Salary as 10k for managers, 20k for software engineers, 5k developers, 12k for team lead.
 QUE6. find the highest salary in all designations
 QUE7. FIND THE

 '''
'''managers = list(filter(lambda x:x[1][0]=="Manager",candidate))
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
'''
#QUE4. Find list of all the emails of employeee with  Company domian name emails .  
'''emails= list(map(lambda x: x[1][2],filter(lambda x: x[1][2].replace("@","company@",),candidate)))
print(emails)


'''

update_email = lambda emp: (emp[0], [emp[1][0], emp[1][1], emp[1][2].replace("@", "@company"), emp[1][3], emp[1][4]])
candidate_with_company_emails = list(map(update_email, candidate))
print(candidate_with_company_emails )

