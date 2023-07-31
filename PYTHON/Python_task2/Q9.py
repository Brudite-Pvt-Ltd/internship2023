#9. Implement a function to rotate an array by a specified number of positions to the left

def rotate_left(arr, positions):
    if not arr:
        return arr

    return arr[positions:] + arr[:positions]

# Using the func
arr = [1, 2, 3, 4, 5]
positions = 4
rotated_arr = rotate_left(arr, positions)
print(rotated_arr)  