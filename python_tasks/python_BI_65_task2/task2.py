# Question 1 --------------------------------------

array1= [3,6,9,12,5]

# Create a new empty array
array2 = []

# Multiply each element by 2 
for num in array1:
    new_num = num * 2
    array2.append(new_num)

print(array2)

#Question 2 -----------------------------------------

array= [3,6,9,12,15]
max_val=max(array)
min_val=min(array)

print("max value :-", max_val)
print("min value :-", min_val)

#Question 3 -----------------------------------------

array1 = [1, 2, 3]
array2 = [4, 5, 6]
concat_array = array1 + array2
print("Concatenated array:", concat_array)

#Question 4 ------------------------------------------

array = [3, 6, 9, 12, 15]
array_sum = sum(array)

print("Sum of all elements:", array_sum)

#Question 5 -------------------------------------------

array = [1, 2, 3, 4, 5,]
boolean=0
for i in range(1, len(array)):
    if array[i] <= array[i - 1]:
        boolean =1
        break
    
    
if boolean==0:
    print("Array is strictly increasing")
else: print("Array is not strictly increasing")

#Question 6 -------------------------------------------

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

set1 = set(array1)
set2 = set(array2)

common_elements = set1.intersection(set2)
common_elements = list(common_elements)

print("Common elements:", common_elements)

#Question 7 -------------------------------------------

def remove_duplicates(arr):
    unique_set = set(arr)

    unique_list = list(unique_set)
    return unique_list

array = [1,4,6,4,5,2,3,1]
result = remove_duplicates(array)

print("modified array:", result)

#Question 8 --------------------------------------------

def max_subarray_sum(arr):
    

    max_sum = arr[0]
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(array)

print("Subarray with maximum sum:", result)


#Question 9 -----------------------------------------------

def rotate_left(arr, positions):
    rotated_array = arr[positions:] + arr[:positions]
    return rotated_array
array = [1,5,7,2,8,3,5,4]
positions = 2
result = rotate_left(array, positions)

print("Array after left rotation:", result)

#Question 10 ------------------------------------------

def find_intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = set1 & set2
    return list(intersection)

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
result = find_intersection(array1, array2)
print("Intersection of the arrays:", result)

