# program 7 : finding the aggregate of all the Designation


# candidate = [[(id, name, aadhar, pan), [designation, experience, email, pin, phone]]]
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

# using update() to adding the salary according to there post

def update(x):
    if x[1][0] == "Manager":
        return int(10000)
    elif x[1][0] == 'Associate Developer':
        return int(5000)
    elif x[1][0] == 'Software Engineer':
        return int(20000)
    elif x[1][0] == 'Team Lead':
        return int(12000)
        
    
# using map to map the values of candidates.

adding_salary = list( map(lambda x : x[1].append(update(x)) or x  , candidate) )

# sotoring the total salary of perticuler post
# as in order = [sde, manager, team_lead, ass_dev]
salary_in_order = [0, 0, 0, 0]
no_of_persons = [0, 0, 0, 0]

def seg(x) :
    if x[1][0] == "Manager":
        return (1, x[1][5])
    elif x[1][0] == 'Associate Developer':
        return (3, x[1][5])
    elif x[1][0] == 'Software Engineer':
        return (0, x[1][5])
    elif x[1][0] == 'Team Lead':
        return (2, x[1][5])

temp_data = list(map(seg, candidate))

for x in temp_data:
    no_of_persons[x[0]] += 1
    salary_in_order[x[0]] += x[1]

avg_sal = []
for i in range(len(salary_in_order)):
    avg_sal.append(salary_in_order[i]/no_of_persons[i])

print("avg of software eng. :" , avg_sal[0] )
print("avg of Manger :" , avg_sal[1] )
print("avg of Team Lead :" , avg_sal[2] )
print("avg of Ass_Dev :" , avg_sal[3] )
