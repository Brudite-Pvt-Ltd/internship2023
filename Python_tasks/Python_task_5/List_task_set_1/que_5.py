# question 5 : sorting the list of tuples according to it's 2nd element.


# creating a list of tuples
l = [ (1,2,3,4), (3, 1, 5, 6), (1,3,2,), (2,4) ]

# creating my_sort function 
def my_sort(l):
    
    # using bubble sort
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[i][1] < l[j][1]):
                l[i], l[j] = l[j], l[i]

    return l

l = my_sort(l)

print("Sorted List :" , l)