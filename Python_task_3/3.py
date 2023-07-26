# program 3


# using bubble sort in reverse manner.
def my_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if(arr[i] > arr[j] ):
                (arr[i], arr[j]) = (arr[j], arr[i])
            
    return arr;


# creating my list
l = [[4, 1, 5], [4, 5, 12], [3, 5, 3]]

# creating answer list
new_l = []

# ittrating all the element and using my_sort function to sort it in reverse order.
for x in l :
    x =  my_sort(x)
    
    # appending in new list 
    new_l.append(x)
    
    
print(new_l)