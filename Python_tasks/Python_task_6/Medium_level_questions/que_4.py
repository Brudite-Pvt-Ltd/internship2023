# program 5:
    
arr = [1, 2, 3, 4, 5]
D = 2

roteted_arr = arr[len(arr)-D:] + arr[:len(arr)-D]

print(roteted_arr)
