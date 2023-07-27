#Given an array of integers, check if it is a strictly increasing array (each element is greater than the previous one).

def strictly_inc(arr):
    for i in range (1,len(arr)):
        if arr[i] <= arr[i-1]:
            return True
     

arr = [100 ,90,80,70,60,50,40,30,20,10]
array1 = [10,20,30,40,50,60,70,80,90,100]

print(strictly_inc(arr))
print(strictly_inc(array1))