# candidate = [[(id, name, aadhar, pan), [designation, experience, email, pin, phone,salary]]]
candidate = [[(2001, 'Rahul', '1234322341', 'HQ255234WQ'), ['Software Engineer', 3, 'rahul@gmail.com', '302022', '9877656723', 20000]],
             [(2002, 'Tina', '9873452345', 'HQ235534WQ'), ['Manager', 4, 'Tina@gmail.com', '302020', '9878776723', 10000]], 
             [(2003, 'Tanya', '9876752345', 'HQ233334WQ'), ['Team Lead', 2, 'Tanya@gmail.com', '302010', '9898646723', 12000]], 
             [(2004, 'Ram', '9873452309', 'HQ238834WQ'), ['Manager', 3, 'Ram@gmail.com', '302012', '9879895723', 10000]],
             [(2005, 'Rishav', '945672345', 'HQ230034WQ'), ['Software Engineer', 5, 'Rishav@gmail.com', '302012', '9879879876', 20000]], 
             [(2006, 'Lakshita', '9873458976', 'HQ211234WQ'), ['Software Engineer', 6, 'Lakshita@gmail.com', '302022', '9879874274', 20000]], 
             [(2007, 'Navpreet', '9873452123', 'HQ554234WQ'), ['Manager', 7, 'Navpreet@gmail.com', '302010', '9879872829', 10000]],
             [(2008, 'Vipul', '9873872345', 'HQ774234WQ'), ['Associate Developer', 3, 'Vipul@gmail.com', '302023', '987957423', 5000]], 
             [(2009, 'Vaibhav', '9873452312', 'HQ256234WQ'), ['Software Engineer', 4, 'Vaibhav@gmail.com', '302014', '9879876723', 20000]], 
             [(2010, 'Janvi', '9873452529', 'HQ223754WQ'), ['Associate Developer', 8, 'Janvi@gmail.com', '302016', '9879876723', 5000]]]


l1=list(filter(lambda x:x[1][0]=="Manager",candidate)) 
l2=list(filter(lambda x:x[1][0]=="Software Engineer",candidate))
l3=list(filter(lambda x:x[1][0]=="Associate Developer",candidate))
l4=list(filter(lambda x:x[1][0]=="Team Lead",candidate))
avg_m=0
avg_se=0
avg_ad=0
avg_tl=0
for x in l1:
    avg_m+=x[1][5]
m=avg_m//len(l1) 

for x in l2:
    avg_se+=x[1][5]
s=avg_se//len(l2)   
    
for x in l3:
    avg_ad+=x[1][5]
a=avg_ad//len(l3)
for x in l4:
    avg_tl=x[1][5]
t=avg_tl//len(l4)   


print("Aggregate of salaries of Managers :",m)
print("Aggregate of salaries Software Engineers :",s)
print("Aggregate of salaries of Associate Developers :",a)
print("Aggregate of salaries of Team lead:",t)