#6.find the highest salary in all designations.
candidate=[
  [('1','ankita',"1234567",  "234567"), 
  ["manager",6, "ankita@gmail.com", "jaipur",'9079075261','10000']],
   [('2','janvi',"1234568",  "234567"), ["software engineer",2, "janvi@gmail.com", "jaipur",'9079075262','20000']],
   [('3','faizal',"1234569",  "234569"), ["intern",2, "faizal@gmail.com", "kashmir",'9079075263','4000']],
    [('4','rishav',"1234560",  "234560"), ["manager",5, "rishav@gmail.com", "bhutan",'9079075264','10000']],
    [('5','lakshita',"12345611",  "2345611"), ["software engineer",2, "lakshita@gmail.com", "bikaner",'9079075265','20000']],
   [('6','navpreet',"12345612",  "2345612"), ["Associate developer",3, "navpreet@gmail.com", "kota",'9079075266','5000']],
   [('7','harshita',"12345613",  "234567"), ["software engineer",5, "harshita@gmail.com", "jaipur",'90790752617','20000']],
    [('8','aashi',"12345614",  "2345614"), ["software engineer",2, "aashi@gmail.com", "bandikui",'9079075268','20000']],
    [('9','mohit',"12345615",  "23456715"), ["manager",4, "mohit@gmail.com", "delhi",'9079075269','10000']],
    [('10','priyanshu',"12345616",  "2345616"), ["Associate developer",3, "priyanshu@gmail.com", "alwar",'9079075260','5000']],

]
from functools import reduce

# using reduce to find the maximum salary in all 
max_salary = reduce(lambda x, y : x if x[1][5] > y[1][5] else y  , candidate)
print("max_salary  : ", max_salary[1][5])
print("designation : ", max_salary[1][0])
