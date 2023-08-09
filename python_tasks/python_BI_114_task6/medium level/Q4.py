def rotate_array(arr, D):
    n=len(arr)
    temp = arr[:n-D] 
    arr[:n-D] = [] #deleteing an aaray  from 0 based index to D-1
    arr.extend(temp)
    return arr
    
arr=[1,2,3,4,5]
print(rotate_array(arr,2))
