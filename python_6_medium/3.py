# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
# Sample Input: arr = [1, 2, 3, 4, 5],  k = 6
# Sample Output: Pair count: 2
arr = [1, 2, 3, 4, 5]
k=6
list1=set()
for i in arr :
    for j in arr:
        if i+j==k and i!=j:
            list1.add(i)
            list1.add(j)
count=len(list1)//2
print(count)