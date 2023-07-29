#1.find list of all manager , software engineers, intern and associate developer
# candidate=[[(id,Name,Aadhar,pan),[designation,experience,email,phone,address]]]
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

manager= list(filter(lambda x:x[1][0]=='manager',candidate))
print(manager)

software_engineer= list(filter(lambda x:x[1][0]=='software engineer',candidate))
print(software_engineer)

intern= list(filter(lambda x:x[1][0]=='intern',candidate))
print(intern)

Associate_developer= list(filter(lambda x:x[1][0]=='Associate developer',candidate))
print(Associate_developer)




