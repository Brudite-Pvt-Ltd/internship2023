# program 1 - search for an element in a list.


# creating a new list 

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# creating a search function
def my_search(l, target):
    
    # using linear search
    for x in range(len(l)):
        
        # if element found then, returning it's index
        if l[x] == target:
            return x
    
    # returning -1 if element is not present         
    return -1 ;
    
    
target = 6
res = my_search(l, target);


if(res != -1):
    print("Element found")
    print("Index (0 based) : ", res)
else:
    print("Element Not Fount")