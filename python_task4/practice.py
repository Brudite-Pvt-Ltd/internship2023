
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
list_of_manager = list(filter((lambda x: x[1][0] == "Manager"),candidate))
list_of_Software  = list(filter((lambda x: x[1][0] == "Software Engineer"),candidate))
list_of_Teamleader = list(filter((lambda x: x[1][0] == "Team Lead"),candidate))
list_of_Associteddev = list(filter((lambda x: x[1][0] == "Associate Developer"),candidate))

print(list_of_manager)
print(list_of_Software)
print(list_of_Teamleader)
print(list_of_Associteddev)

#Q2.find list of all members having experince more then 5 yr. ?

list_of_expmore5 = list(filter((lambda x: x[1][1] > 5),candidate))
print(list_of_expmore5 )

#Q3.Find list of all the candidates with pan = 302012?

list_of_pin302012 = list(filter((lambda x: x[1][3] == "302012"),candidate))
print(list_of_pin302012)

#Q4Find list of all the emails of employeee with  Company domian name emails .


e = list(map((lambda x: ".company@".join(x[1][2].split('@')) ), candidate))
for i in range(0,len(candidate)):
    candidate[i][1][2]=e[i]
print(candidate)

#Q5.Add a Base Salary as 10k for managers, 20k for software engineers, 5k developers, 12k for team lead.

basic_salary = [10000 if x[1][0] == "Manager" else 20000 if x[1][0] == "Software Engineer" else 5000 if x[1][0] == "Associate Developer" else 12000 if x[1][0] == "Team Lead" else 0 for x in candidate]
print(basic_salary)

me = [x[1].append(10000) or x for x in list_of_manager ]
print(me)
se = [x[1].append(20000) or x for x in list_of_Software ]
print(se)
ad = [x[1].append(5000) or x for x in list_of_Associteddev ]
print(ad)
tl = [x[1].append(12000) or x for x in list_of_Teamleader]
print(tl)

#Q6.Find the Highest Salary in all Designations

Mang_list = list(filter((lambda x:x[1][0]=="Manager"),candidate))

Se_list = list(filter((lambda x:x[1][0]=="Software Engineer"),candidate)) 

Associate_list = list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))

Team_list = list(filter((lambda x:x[1][0]=="Team Lead"),candidate))

list1=[x[1].append(10000) or  x[1] for x in Mang_list] 

list2=[x[1].append(20000) or  x[1] for x in Se_list] 

list3=[x[1].append(5000) or  x[1] for x in Associate_list]

list4=[x[1].append(12000) or  x[1] for x in Team_list]  

from functools import reduce

max_sal = reduce(lambda x, y : x if x[1][5] > y[1][5] else y  , candidate)
print(max_sal[1][5])
print(max_sal[1][0])

#Q7.Find the Aggregate of salaries of Managers, Software Engineers, Team Lead and Associate Developer.

Mang_list = list(filter((lambda x:x[1][0]=="Manager"),candidate))

Se_list = list(filter((lambda x:x[1][0]=="Software Engineer"),candidate)) 

Associate_list = list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))

Team_list = list(filter((lambda x:x[1][0]=="Team Lead"),candidate))

list1=[x[1].append(10000) or  x[1] for x in Mang_list] 

list2=[x[1].append(20000) or  x[1] for x in Se_list] 

list3=[x[1].append(5000) or  x[1] for x in Associate_list]

list4=[x[1].append(12000) or  x[1] for x in Team_list]  

print("Aggregate salary of Manager =",(len(Mang_list)*10000))
print("Aggregate salary of Software Engg =",(len(Se_list)*20000))
print("Aggregate salary of Team Lead =",(len(Team_list)*12000))
print("Aggregate salary of Associate Developer =",(len(Associate_list)*5000))


#Q8. Find all the employees with pincode near by in range +-10.
#means -> if the input is 302015 then range upto 302005 to 302025 will be filtered.
 
pin = 302012
pin_range = list(filter(lambda x:((int(x[1][3]) > pin - 10) and (int(x[1][3]) < pin + 10)),candidate))
print(pin_range)


#Q9.Create a Dictionary with Tuple as Key and List[1] as value.


dict = { x[0] : x[1] for x in candidate }
print(dict)


#Q10.Create a Contact Directory where people can search phone numbers through name or ID.

target_name = ""
target_id = (input("enter emp_id : "))
if(target_id != ''):
    target = int(target_id)    
    matched_data =  list(filter( lambda x : x != None ,list(map(lambda x : [x[0][0], x[0][1], x[1][4]] if x[0][0] == target else None , candidate))))
    print(matched_data)
else :
    target_name = input("enter emp_name : ")
    if(target_name != ''):
        matched_data = list(filter(lambda x: x!=None ,list(map(lambda x : [x[0][0], x[0][1], x[1][4]] if str(x[0][1]).__contains__(target_name) == True else None , candidate )))) 
        for x in matched_data:
            print(x)
    else:
        print("Please enter id or name")