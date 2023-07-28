candidate = [
    [ (2001, 'Rahul', "1234322341", "HQ255234WQ"), ["Software Engineer", 3, "rahul@gmail.com", "302022", "9877656723"]],
    [ (2002, 'Tina', "9873452345", "HQ235534WQ"), ["Manager", 4, "Tina@gmail.com", "302020", "9878776723"]],
    [ (2003, 'Tanya', "9876752345", "HQ233334WQ"),["Team Lead", 2, "Tanya@gmail.com", "302010", "9898646723"]],
    [ (2004, 'Ram', "9873452309", "HQ238834WQ"),  ["Manager", 3, "Ram@gmail.com", "302012", "9879895723"]],
    [ (2005, 'Rishav', "945672345", "HQ230034WQ"),["Software Engineer", 5, "Rishav@gmail.com", "302012", "9879879876"]],
    [ (2006, 'Lakshita', "9873458976", "HQ211234WQ"),["Software Engineer", 6, "Lakshita@gmail.com", "302022", "9879874274"]],
    [ (2007, 'Navpreet', "9873452123", "HQ554234WQ"),["Manager", 7, "Navpreet@gmail.com", "302010", "9879872829"]],
    [ (2008, 'Vipul', "9873872345", "HQ774234WQ"),   ["Associate Developer", 3, "Vipul@gmail.com", "302023", "987957423"]],
    [ (2009, 'Vaibhav', "9873452312", "HQ256234WQ"), ["Software Engineer", 4, "Vaibhav@gmail.com", "302014", "9879876723"]],
    [ (2010, 'Janvi', "9873452529", "HQ223754WQ"),   ["Associate Developer", 8, "Janvi@gmail.com", "302016", "9879876723"]]
]
"""
#que 1: list of all managers,software engineers, Associative Developers, and Team Leads
list_of_Mangers = list(filter((lambda x:x[1][0]=="Manager"),candidate))

list_of_Se = list(filter((lambda x:x[1][0]=="Software Engineer"),candidate)) 

list_of_AD = list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))

list_of_TL = list(filter((lambda x:x[1][0]=="Team Lead"),candidate))

print("List_of_Mangers",list_of_Mangers)
print(list_of_Se)
print(list_of_TL)
print(list_of_AD)
"""
"""

#que 2: list of candidate have expericnce more than 5
list_of_experienceMore5 =  list(filter((lambda x:x[1][1]>5),candidate))  
print(list_of_experienceMore5) 
"""
"""
#Que3  Candidate with pin = 302012
list_of_pin_302012 =  list(filter((lambda x:x[1][3]=="302012"),candidate))  
print(list_of_pin_302012)

"""
"""

#que4: update all emails of employee with company domain name emails
e = list(map((lambda x: ".company@".join(x[1][2].split('@')) ), candidate))
for i in range(0,len(candidate)):
    candidate[i][1][2]=e[i]
#print(candidate)
"""


"""
#que5 adding a base salary   

#usm = [ (x[1].append(10000) or x)  for x in  list(filter((lambda x:x[1][0]=="Manager"),candidate))]
#print(usm)

#uss = [ (x[1].append(20000) or x)  for x in list(filter((lambda x:x[1][0]=="Software Engineer"),candidate))]
#print(uss)

#ust = [ (x[1].append(12000) or x)  for x in list(filter((lambda x:x[1][0]=="Team Lead"),candidate))]
#print(ust)
#usa = [ (x[1].append(5000) or x)  for x in  list(filter((lambda x:x[1][0]=="Associate Developer"),candidate))]
#print(usa)
"""


"""
#que6 find the height salry in all desitnation
# from functools import reduce
# heighest_salary =reduce(lambda x,y : max(x,y),list(map(lambda x:x[1][5] ,candidate)))
# print(heighest_salary)
"""
"""
#que 7 aggregate salary of indivual destination
# print("aggregate salary of Manager =",(len(list_of_Mangers)*10000)/len(candidate))
# print("aggregate salary of Software Engg =",(len(list_of_Se)*20000)/len(candidate))
# print("aggregate salary of Team Lead =",(len(list_of_TL)*12000)/len(candidate))
# print("aggregate salary of Associate Developer=",(len(list_of_AD)*5000)/len(candidate))
"""
"""
#que 8 neighbour or pin in range of +-10
#target_pin = 302012
#pin_range_filterd = list(filter(lambda x:((int(x[1][3])>target_pin-10) and (int(x[1][3])<target_pin + 10)),candidate))
#print(pin_range_filterd))
"""
"""
#que 9 create a dictionary with tuple as key and List[1] as value.
dictcandidate = { x[0]:x[1] for x in candidate}
print(dictcandidate)
"""
"""
#que10 create a contact Directory where people can search phone numbers through name  or ID.
contact_directory = [([x[0][0],x[0][1],x[1][4]]) for x in candidate]
print(contact_directory)
"""