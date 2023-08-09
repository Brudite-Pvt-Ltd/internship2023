arr = [1, 2, 3, 4, 5]
d=2
if d > len(arr):
    d=d-len(arr)
print("orignal list is ",arr)
l2=arr[len(arr)-d:]+arr[:len(arr)-d]
print("rotated list is ", l2)    