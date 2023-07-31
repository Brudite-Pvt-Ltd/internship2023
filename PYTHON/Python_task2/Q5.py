#5. Given an array of integers, check if it is a strictly increasing array (each element is greater than the previous one).

def strictly_inc(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False

    return True

aray = [5,4,3,2,1]
aray2 = [1,2,3,4,5]

print(strictly_inc(aray))
print(strictly_inc(aray2))