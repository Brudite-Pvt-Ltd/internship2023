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

#Question 1 find list of all the Managers, Software Engineers, Team Lead and Associate Developer.

mang_list=list(filter(lambda x: x[1][0]=='Manager',candidate))
print("list of manager:-",mang_list)

associate_list=list(filter(lambda x: x[1][0]=='Associate Developer',candidate))
print("list of Associate Developer:-",associate_list)

se_list=list(filter(lambda x: x[1][0]=='Software Engineer',candidate))
print("list of Software Engineer:-",se_list)

teamleader_list=list(filter(lambda x: x[1][0]=='Team Lead',candidate))
print("list of team leader:-",teamleader_list)


#Question 2 list of candidate who has experience more then 5 yr

list1=list(filter(lambda x: x[1][1]>5,candidate))
print("list of candidate who has experience more then 5 yr:-",list1)

#Question 3 find list of all candidate with pin = 302012
list1=list(filter(lambda x: x[1][3]=='302012',candidate))
print("list of haveing same pin 302012:-",list1)


#Question 4 Update all the emails of employee with company domain name emails

update_email = lambda emp: (emp[0], [emp[1][0], emp[1][1], emp[1][2].replace("@", "@company"), emp[1][3], emp[1][4]])
candidate_with_company_emails = list(map(update_email, candidate))
print(candidate_with_company_emails )
print(list)

#Question 5  Add a Base Salary as 10k for managers, 20k for software engineers, 5k for associate developers, 12k for Team lead.

l1=[x[1].append("10000") or  x[1] for x in mang_list]
print(l1)
l2=[x[1].append("20000") or  x[1] for x in se_list]
print(l2)
l3=[x[1].append("5000") or  x[1] for x in associate_list]
print(l3)
l4=[x[1].append("15000") or  x[1] for x in teamleader_list]
print(l3)

#Question 6 find the highest salary

mappedlist=list(map(lambda x: x[1][5],candidate))
print(mappedlist)
heighest_salary=max(mappedlist,key=lambda x: int(x))

print("highest salary among all of them :-",heighest_salary)

#question 7 Aggregate sal of individual

object=int(candidate[1][1][5])
print("aggregate salary of maanger:-",object*len(mang_list)/len(candidate))
object=int(candidate[2][1][5])
print("aggregate salary of team leader:-",object*len(teamleader_list)/len(candidate))
object=int(candidate[8][1][5])
print("aggregate salary of software engineer:-",object*len(se_list)/len(candidate))
object=int(candidate[7][1][5])
print("aggregate salary of Associate developer:-",object*len(associate_list)/len(candidate))

#Question 8 neighbour or pin in range 

target_pin = 302010
neighbour_pin= list(filter(lambda x: (target_pin - 10) < int(x[1][3]) < (target_pin + 10), candidate))

for x in neighbour_pin:
    print("neighbours pin :-",x)

#Question 9 dict with tuples as key and list[1] as value

dictionary_of_candidate = dict(map(lambda x: (x[0], x[1]), candidate))
print("dict of candidate",dictionary_of_candidate)

#Question 10 create a contact dictionary

contact_directory = [([x[0][0],x[0][1],x[1][4]]) for x in candidate]
print("contact directory :-",contact_directory)
