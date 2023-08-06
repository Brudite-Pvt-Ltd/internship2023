def rotate_array(arr, D):
    n = len(arr)
    temp = arr[n - D:]  
    arr[D:] = arr[:n - D] 
    arr[:D] = temp  

# Sample Input
arr = [1, 2, 3, 4, 5]
D = 2

rotate_array(arr, D)

print("arr after rotation:", arr) 