#Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
list_array = [1,2,3,4,5]
k = 6
count = 0
for i in range(len(list_array)):
    for j in range(i+1, len(list_array)):
        if list_array[i] + list_array[j] == k :
            count += 1
print(count)