# program 9 :
    
lst = list(map(int, input("Enter the list : ").split()))


# using try catch to handle the error.
for i in range( len(lst) + 2 ):
    try :
        print(lst[i])
    
    except IndexError :
        print(IndexError)
        
