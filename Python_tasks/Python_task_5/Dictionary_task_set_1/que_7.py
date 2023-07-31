# program 7 : create a dictionary witt key = string and val = string length


# creating a list of names 

names = [ "baru", "aaiku", "chingiri", "rhin", "nova", "isagi", "bachira", "rio" ]


# function to create dictionary

def create_dic(l):
    dic = {}
    for x in l :
        dic[x] = len(x)
    
    return dic
    
dic = create_dic(names)

print(dic)
    