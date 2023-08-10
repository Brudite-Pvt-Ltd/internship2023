# 4.Given an array of size N The task is to rotate array by D elements towards right
# Sample Input: arr = [1, 2, 3, 4, 5], D = 2
# Sample Output: arr after rotation = [4, 5, 1, 2, 3]
def rotate_array(arr, D):
    n=len(arr)
    from_1_to_3 = arr[:n-D] 
    arr[:n-D] = [] #deleteing an aaray  from 0 based index to D-1
    arr.extend(from_1_to_3)
    return arr
    
arr=[1,2,3,4,5]
print(rotate_array(arr,2))

