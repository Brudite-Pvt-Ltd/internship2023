#Implement a function to rotate an array by a specified number of positions to the left.

def rotate_left(arr , positions):
    if not arr:
        return arr 
    
    return arr[positions:] + arr[:positions]

arr=[10,20,30,40,50]
positions= 10
rotated_arr = rotate_left(arr, positions)
print(rotated_arr)