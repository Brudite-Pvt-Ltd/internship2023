# program 4 :   find the key for given value 


# creating a dictionary

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# taking input from user to find value 

target = int(input("Enter the target Value : "))

key = 'NA'

for x in dic :
    if dic[x] == target:
        key = x ;
        break
    
if key == 'NA':
    print("Target not found")
else :
    print("Key =", key)