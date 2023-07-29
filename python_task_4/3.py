#3.find list of all cadidate with pin =302012 .
candidate=[
    [('1','ankita',"1234567",  "234567"), 
     ["manager",6, "ankita@gmail.com","302012", "jaipur",'9079075261']],
    [('2','janvi',"1234568",  "234567"), ["software engineer",2, "janvi@gmail.com","302012", "jaipur",'9079075262']],
    [('3','faizal',"1234569",  "234569"), ["intern",2, "faizal@gmail.com","302013", "kashmir",'9079075263']],
    [('4','rishav',"1234560",  "234560"), ["manager",5, "rishav@gmail.com","302017", "bhutan",'9079075264']],
    [('5','lakshita',"12345611",  "2345611"), ["software engineer",2, "lakshita@gmail.com","302018" ,"bikaner",'9079075265']],
    [('6','navpreet',"12345612",  "2345612"), ["Associate developer",3, "navpreet@gmail.com","303019", "kota",'9079075266']],
    [('7','harshita',"12345613",  "234567"), ["software engineer",5, "harshita@gmail.com","302213", "jaipur",'90790752617']],
    [('8','aashi',"12345614",  "2345614"), ["software engineer",2, "aashi@gmail.com","302245", "bandikui",'9079075268']],
    [('9','mohit',"12345615",  "23456715"), ["manager",4, "mohit@gmail.com","302014", "delhi",'9079075269']],
    [('10','priyanshu',"12345616",  "2345616"), ["Associate developer",3, "priyanshu@gmail.com","302234", "alwar",'9079075260']],
]

pin=list(filter(lambda x:x[1][3]=="302012",candidate))  
print("list of all candidate with pin = 302012.")
print(pin)