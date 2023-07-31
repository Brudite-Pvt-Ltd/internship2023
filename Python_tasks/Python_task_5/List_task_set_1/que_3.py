# program 3 : sum of all numeric elements in a list


# creating a list 
l = [0, "bade", 2, 3, 4, 5, 6, "adv", 8, 9]

sum = 0 ;

for x in l :
    
    # checking for integer
    if(isinstance(x, int)) :
        sum += x 
        
    
print("Sum = ", sum)
        