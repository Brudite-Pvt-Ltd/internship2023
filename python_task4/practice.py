
# use of filter map and reduce functions in python  


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

#Q1.Find list of all manager ,software engineers, team leader and assoiated developer ?
'''list_of_manager = list(filter((lambda x: x[1][0] == "Manager"),candidate))
list_of_Software  = list(filter((lambda x: x[1][0] == "Software Engineer"),candidate))
list_of_Teamleader = list(filter((lambda x: x[1][0] == "Team Lead"),candidate))
list_of_Associteddev = list(filter((lambda x: x[1][0] == "Associate Developer"),candidate))

print(list_of_manager)
print(list_of_Software)
print(list_of_Teamleader)
print(list_of_Associteddev)'''

#Q2.find list of all members having experince more then 5 yr. ?

'''list_of_expmore5 = list(filter((lambda x: x[1][1] > 5),candidate))
print(list_of_expmore5 )'''

#Q3.Find list of all the candidates with pan = 302012?

'''list_of_pin302012 = list(filter((lambda x: x[1][3] == "302012"),candidate))
print(list_of_pin302012)'''

#Q4Find list of all the emails of employeee with  Company domian name emails .
#Q5.Add a Base Salary as 10k for managers, 20k for software engineers, 5k developers, 12k for team lead.

l1 = [x[1].append(2000) or x[1] for x in candidate]
print(l1)


