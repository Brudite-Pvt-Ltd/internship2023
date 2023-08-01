#Create a set with elements from 1to10 .Check if it is a subset of {0,5,10,15}
'''def substring(set1, set2):
    for i in set1:
     if i not in set2:
        return False
     return True

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {0,5,10,15}

print(substring(set1, set2))'''


# Create a set and repeatedly add an element until it reaches a size of 10.

'''def add_ele_set(size):
    s = set()
    for i in range(size):
        s.add(i)
    return s

set = add_ele_set(10)
print(set)'''


# Create a set of all the characters in the string "python programming".

'''def set_char(string):
    all_char = set()
    for c in string:
        all_char.add(c)
    return all_char

print(set_char("python programming"))'''


# Create a set of prime numbers between 1 and 50.

'''def prime_no(size):
    primes = set()
    for i in range(2, size):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.add(i)
    return primes


print(prime_no(50))'''


# Create a function that takes two sets and returns their Cartesian product as a set of tuples.

'''def cartesian_product(set1, set2):
    cartesian_set = set()
    for i in set1:
        for j in set2:
            cartesian_set.add((i,j))
    return cartesian_set

set1 = {1,2,3}
set2 = {'x','y'}
result = cartesian_product(set1, set2)
print(result)'''

# Write a function to check if two sets are disjoint

'''def is_disjoint(set1, set2):
    for i in set1:
        for j in set2:
            if i==j:
                return False
        else:
            return True
            

set1 = {31,23,3}
set2 = {40,3,31}
set3 = {14,30,5}

print(is_disjoint(set1, set2))
print(is_disjoint(set1, set3))'''


# Create a set of random integers and sort them in ascending order.

'''def sort_ascending(set1):
    sorted_set = set()
    for i in set1:
        sorted_set.add(i)     
    return sorted_set 

set1 = {2,5,1,6,4,9,8,7,3,10}
print(sort_ascending(set1))'''

 #Write a function to find the nth smallest element in a set

'''def smallest_ele(set_1, n):
    res = sorted(set_1)
    return res[n-1]

set1 = {9,3,5,1}
n = int(input("Enter the Nth position : "))
result = smallest_ele(set1, n)
print(result)'''

# Create a set with 1000 elements and measure the time taken to search for a specific element.
# Compare it with a list containing the same elements.

'''import time

def find_time(set, element):
    start_time = time.time()
    if element in set:
        end_time = time.time()
        return end_time - start_time
    else:
        return 0

s = set(range(1000))
l = list(range(1000))
element = 207
search_time_set = find_time(s, element)
search_time_list = find_time(l, element)
print(search_time_set)
print(search_time_list)'''

# Create a set of numbers, find all pairs of elements whose sum is a prime number

'''def prime_no(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_pairs(numbers_set):
    prime_pairs = []
    elements_list = list(numbers_set)
    n = len(elements_list)

    for i in range(n):
        for j in range(i + 1, n):
            num_sum = elements_list[i] + elements_list[j]
            if prime_no(num_sum):
                prime_pairs.append((elements_list[i], elements_list[j]))

    return prime_pairs

numbers_set = {1,2,3,4,5}
prime_sum_pairs = sum_pairs(numbers_set)
print("Pairs of elements whose sum is a prime number:")
for pair in prime_sum_pairs:
    print(pair)'''




