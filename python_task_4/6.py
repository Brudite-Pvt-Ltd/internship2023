#6.find the highest salary in all designations.
# candidate=[
#   [('1','ankita',"1234567",  "234567"), 
#   ["manager",6, "ankita@gmail.com", "jaipur",'9079075261','10000']],
#    [('2','janvi',"1234568",  "234567"), ["software engineer",2, "janvi@gmail.com", "jaipur",'9079075262','20000']],
#    [('3','faizal',"1234569",  "234569"), ["intern",2, "faizal@gmail.com", "kashmir",'9079075263','4000']],
#     [('4','rishav',"1234560",  "234560"), ["manager",5, "rishav@gmail.com", "bhutan",'9079075264','10000']],
#     [('5','lakshita',"12345611",  "2345611"), ["software engineer",2, "lakshita@gmail.com", "bikaner",'9079075265','20000']],
#    [('6','navpreet',"12345612",  "2345612"), ["Associate developer",3, "navpreet@gmail.com", "kota",'9079075266','5000']],
#    [('7','harshita',"12345613",  "234567"), ["software engineer",5, "harshita@gmail.com", "jaipur",'90790752617','20000']],
#     [('8','aashi',"12345614",  "2345614"), ["software engineer",2, "aashi@gmail.com", "bandikui",'9079075268','20000']],
#     [('9','mohit',"12345615",  "23456715"), ["manager",4, "mohit@gmail.com", "delhi",'9079075269','10000']],
#     [('10','priyanshu',"12345616",  "2345616"), ["Associate developer",3, "priyanshu@gmail.com", "alwar",'9079075260','5000']],

# ]
# from functools import reduce

# # using reduce to find the maximum salary in all 
# max_salary = reduce(lambda x, y : x if x[1][5] > y[1][5] else y  , candidate)
# print("max_salary  : ", max_salary[1][5])
# print("designation : ", max_salary[1][0])

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

#        in 1.part, we are adding salary 
#        in 2.part, we are finding the highest salary.


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


# importing reduce
from functools import reduce

# using reduce to find the maximum salary in all 
max_salary = reduce(lambda x, y : x if x[1][5] > y[1][5] else y  , candidate)
print("max_salary  : ", max_salary[1][5])
print("Designation : ", max_salary[1][0])
