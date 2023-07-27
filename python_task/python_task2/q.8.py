#Given an array of integers, find the subarray with the maximum sum.

def max_subarray_sum(arr):
    if not arr:
        return 0 
    
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range (1, len(arr)):
        current_sum = max(arr[1] , current_sum + arr[i])
        max_sum = max(max_sum , current_sum)

        return max_sum
    arr = [-5 , -4 , 3 , 6 , -6 , -8 , -9 , 4 , -1]
    max_sum = max_subarray_sum(arr)
    print("Maximun sum:",max_sum)