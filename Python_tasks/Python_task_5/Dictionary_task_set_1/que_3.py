# program 3 : find the keys with maximum and minimum value in dictionary


# creating a dictionary

dic = { 'a':1, 'b': 2, 'c':3, 'd':4, 'e':5 }


mn = ''
mn_val = 1e8
mx = ''
mx_val = -1e8

for x in dic.keys() :
    if dic[x] < mn_val:
        mn_val = dic[x]
        mn = x
    
    if dic[x] > mx_val:
        mx_val = dic[x]
        mx = x 
    
print("max valued key : ", mx)
print("min valued key : ", mn)
