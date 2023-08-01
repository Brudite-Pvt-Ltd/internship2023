#Remove an element from a list by its value# Remove an element from a list by its value.

'''def ele_removed(list, val):
    if val in list:
        list.remove(val)
    return list

list = [10,30,50,72,93]
value = 50
print(ele_removed(list, value))'''


# Find the length of a list without using the len() function.

'''def length_list(list):
    count = 0
    for item in list:
        count += 1
    return count

list = [1,2,3,4,5,6]
print(length_list(list))'''


# Find the frequency of each element in a list and store it in a dictionary.

'''def freq(list):
    freq_dict = {}
    for i in list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict

list = [1, 2, 3, 1, 2, 1, 2, 3]
print(freq(list))'''



# Find the median of a list without using the built-in median function.

'''def median(list):
    if len(list) == 0:
        return None
    list.sort()
    if len(list) % 2 == 0:
        return (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
    else:
        return list[len(list) // 2]
    
list = [7, 5, 3, 9, 1, 1]
print(median(list))'''


# Split a list into evenly sized chunks.

'''def split(list, n):
    return [list[i:i + n] for i in range(0, len(list), n)]

list = [1,3,5,7,9,11]
n = 3   
print(split(list, n))'''



# Create a list of all prime numbers up to a given number.

'''def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    list_of_prime = []
    for i in range(2, n):
        if is_prime(i):
            list_of_prime.append(i)
    return list_of_prime        

n = 100
print(prime_list(n))'''


# Shuffle a list randomly without using any built-in functions.
'''import random

def shuffle(list):
    for i in range(len(list) - 1):
        j = random.randint(i, len(list) - 1)
        list[i], list[j] = list[j], list[i]
    return list

list = [1,2,3,4,5]
print(shuffle(list))'''

# Find the maximum product of three elements in a list.

'''def max_product(l):
    maxi = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] * l[j] * l[k] > maxi:
                    maxi = l[i] * l[j] * l[k]
    return maxi
    

list = [1,3,5,7,9,8,6,4,2]
print(max_product(list))'''

# Implement a function that takes a list of tuples,where each tuple contains a name and age,
# and returns the names of the three oldest people.

'''def old_person(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list[:3]

l = [('harshit', 30), ('simran', 20), ('somya', 40), ('siya', 50)]
print(old_person(l))'''


'''Write a function that takes a list of integers as input and rearranges the elements so that
all negative elements appear before the non-negative elements, and the order of elements within 
each category remains unchanged.The goal is to do this in-place,i.e.,without using any additional
data structures.For example,given the list:[3,-1,-4,2,0,-5,6,-2],after rearranging,the output
should be:[-1,-4,-5,-2,3,2,0,6].''' 

'''def re_arrange(list):
    left_ptr = 0  

    for right_ptr in range(len(list)):
        if list[right_ptr] < 0:
            for i in range(right_ptr, left_ptr, -1):
                list[i], list[i-1] = list[i-1], list[i]
            left_ptr += 1
    return list

l = [3,-1,-4,2,0,-5,6,-2]
print(re_arrange(l))'''