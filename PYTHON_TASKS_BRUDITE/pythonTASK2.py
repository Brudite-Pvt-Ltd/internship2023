import random
#Q1.Create an array of the first 10 even numbers (starting from 2).

even_numbers = []
current_number = 2

for current_number in range(2,22):
    if current_number % 2 == 0:
     even_numbers.append(current_number)
print(even_numbers)

#Q2.Given an array [1, 2, 3, 4, 5], reverse the elements and print the resulting array.

given_array = [1,2,3,4,5]
print(given_array)
reversed_array = given_array[::-1]
print(reversed_array)

#Q3.Write a Python function to check if an element exists in an array.

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#Q4.Given an array [1, 2, 3, 4, 5], shuffle the elements randomly to create a new array.

given_array=[1,2,3,4,5]
print(given_array)
random.shuffle(given_array)
print(given_array)

#Q5.Write a Python program to count the number of occurrences of a specific element in an array.

def count(lst, x):
    return lst.count(x)
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,count(lst, x)))


#Q6.Implement a function to check if an array is a palindrome (reads the same forwards and backwards).

string = input("Enter the string: ")
if(string==string[::-1]):
    print("It is a palindrome ")
else:
    print("NOT PALINDROME")
    
    #SAME GOES FOR ARRAYS JUST CHANGE THE DATATYPE BY TYPECAST
    
#Q7. Write a Python program to merge two sorted arrays into a single sorted array.

arr1=[1,2,3]
arr2=[4,5,6]
arr3 = arr1 + arr2
arr3.sort()
print(arr3)

#Q8.Given an array of integers, move all the zero elements to the end while maintaining the order of other elements.


A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
j = 0
for i in range(n):
    if A[i] != 0:
        A[j], A[i] = A[i], A[j]  # Partitioning the array
        j += 1
print(A)

#Q9.Write a Python function to find the second-largest element in an array.

list = [2, 1, 8, 7, 3, 0]
print("The given list is",list)
list.sort()
print("We sorted the list",list)
print("The second largest element of the list is", list[1])

#Q10.Given an array of integers, find the longest increasing subarray (consecutive elements in increasing order).

def printLongestIncSubArr( arr, n) :
    m = 1
    l = 1
    maxIndex = 0
    for i in range(1, n) :
        if (arr[i] > arr[i-1]) :
            l =l + 1
        else :
            if (m < l)  :
                m = l  
                maxIndex = i - m   
            l = 1   
    if (m < l) :
        m = l
        maxIndex = n - m
    for i in range(maxIndex, (m+maxIndex)) :
        print(arr[i] , end=" ")
arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
n = len(arr)
printLongestIncSubArr(arr, n)