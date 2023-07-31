# program 1 : merging two dictionary ( with over-writing )


# creating two dictionaries

dic1 = { 'a':1, 'b':2, 'c':3, 'd':4 }
dic2 = { 'c':5, 'd':6, 'e':7, 'f':8 }

# method : doing manualy 

for x in dic2 :
    dic1[x] = dic2[x] 
    
print(dic1)

# method : using in-built function

dic1 = { 'a':1, 'b':2, 'c':3, 'd':4 }
dic2 = { 'c':5, 'd':6, 'e':7, 'f':8 }


dic1.update(dic2)
print(dic1)




