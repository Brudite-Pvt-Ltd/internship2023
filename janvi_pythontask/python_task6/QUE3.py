#Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
arr = [1, 2, 3, 4, 5]
k = 6
# Sample Output: Pair count: 2
def sum_equal_to_k(arr,k):
    list1=set()
    for i in arr:
        for j in arr:
            if i+j==k and i!=j :
                list1.add(i)
                list1.add(j)
    print(list1)
    element=len(list1)//2
    return element

arr = [1, 2, 3, 4, 5]
k = 6
print(sum_equal_to_k(arr,k))

