# program 9 : maximum difference between two elements.


# creating a list 

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# approach : finding the minimum and maximum elements in list 
# then just simply subtract them to find the maximum diff. 
# in the list

# mx to store maximum
# initalizing with min. value
mx = -1e9        

# mn to store minimum
# initalizing with max. value
mn = 1e9


for x in l :
    mx = max(x, mx)
    mn = min(x, mn)
    
    
max_diff = mx - mn
print("Maximum Difference :", mx - mn)