# Question 6: Find the Highest Salary in all Designations.

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

