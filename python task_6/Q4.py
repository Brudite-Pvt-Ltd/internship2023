#Given an array of size N The task is to rotate array by D elements towards right
arr = [1,2,3,4,5]
d = 3
def arr_rotate(r, arr, d) :
    a = r.index(d)
    n = len(arr)
    arr[:] = arr[n-d:] + arr[:n-d]
    return arr

'''def rotate(R, D, n):
    a = R.index(D)
    list1 = []
    list1 = R[a+1:]+R[0:a+1] 
    return list1


if name == 'main':
    arr = [1, 2, 3, 4, 5]
    D = 3
    n = len(arr)

    # Function call
    arr = rotate(arr, D, n)
    for i in arr:
        print(i, end=" ")'''