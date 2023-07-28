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

n=int(input("enter pin code"))
l7=list(filter(lambda x:int(x[1][3])>=n-10 and int(x[1][3])<=n+10,candidate))  
print(" the list of employees with pincode near by in range +-10")
print(l7)