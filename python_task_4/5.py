#5.add a base salary as 10k for managers,20k for software engineers, 5k for associate managers and 4k for interns.
candidate=[
    [('1','ankita',"1234567",  "234567"), 
     ["manager",6, "ankita@gmail.com", "jaipur",'9079075261']],
    [('2','janvi',"1234568",  "234567"), ["software engineer",2, "janvi@gmail.com", "jaipur",'9079075262']],
    [('3','faizal',"1234569",  "234569"), ["intern",2, "faizal@gmail.com", "kashmir",'9079075263']],
    [('4','rishav',"1234560",  "234560"), ["manager",5, "rishav@gmail.com", "bhutan",'9079075264']],
    [('5','lakshita',"12345611",  "2345611"), ["software engineer",2, "lakshita@gmail.com", "bikaner",'9079075265']],
    [('6','navpreet',"12345612",  "2345612"), ["Associate developer",3, "navpreet@gmail.com", "kota",'9079075266']],
    [('7','harshita',"12345613",  "234567"), ["software engineer",5, "harshita@gmail.com", "jaipur",'90790752617']],
    [('8','aashi',"12345614",  "2345614"), ["software engineer",2, "aashi@gmail.com", "bandikui",'9079075268']],
    [('9','mohit',"12345615",  "23456715"), ["manager",4, "mohit@gmail.com", "delhi",'9079075269']],
    [('10','priyanshu',"12345616",  "2345616"), ["Associate developer",3, "priyanshu@gmail.com", "alwar",'9079075260']],
]
def salary(x):
  if x[1][0] == "manager":
        return int(10000)
  elif x[1][0] == 'Associate developer':
        return int(5000)
  elif x[1][0] == 'software engineer':
        return int(20000)
  elif x[1][0] == 'intern':
        return int(4000)
add_salary = list(map(lambda x : x[1].append(salary(x)) or x , candidate) )
for x in add_salary :
    print(x)

