# candidate = [[(id, name, aadhar, pan), [designation, experience, email, pin, phone]]]
candidate = [
    [ (2001, 'Rahul sharma', "1234322341", "HQ255234WQ"),
        ["Software Engineer", 3, "rahul@gmail.com", "302022", "9877656723"]],
        [ (2002, 'Tina sharma', "9873452345", "HQ235534WQ"),
        ["Manager", 4, "Tina@gmail.com", "302020", "9878776723"]],
        [ (2003, 'Tanya verma', "9876752345", "HQ233334WQ"),
        ["Team Lead", 2, "Tanya@gmail.com", "302010", "9898646723"]],
        [ (2004, 'shri Ram', "9873452309", "HQ238834WQ"),
        ["Manager", 3, "Ram@gmail.com", "302012", "9879895723"]],
        [ (2005, 'Rishav jain', "945672345", "HQ230034WQ"),
        ["Software Engineer", 5, "Rishav@gmail.com", "302012", "9879879876"]],
        [ (2006, 'Lakshita jain', "9873458976", "HQ211234WQ"),
        ["Software Engineer", 6, "Lakshita@gmail.com", "302022", "9879874274"]],
        [ (2007, 'Navpreet singh', "9873452123", "HQ554234WQ"),
        ["Manager", 7, "Navpreet@gmail.com", "302010", "9879872829"]],
        [ (2008, 'Vipul singh', "9873872345", "HQ774234WQ"),
        ["Associate Developer", 3, "Vipul@gmail.com", "302023", "987957423"]],
        [ (2009, 'Vaibhav sahu', "9873452312", "HQ256234WQ"),
        ["Software Engineer", 4, "Vaibhav@gmail.com", "302014", "9879876723"]],
        [ (2010, 'Janvi verma', "9873452529", "HQ223754WQ"),
        ["Associate Developer", 8, "Janvi@gmail.com", "302016", "9879876723"]]
]

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