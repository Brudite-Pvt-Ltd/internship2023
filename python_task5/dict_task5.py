# Create a dictionary of students and their scores,find and print the student with the highest score.

'''def highest_score(dict):
    highest_score = 0
    highest_score_student = ""
    for i in dict:
        if dict[i] > highest_score:
            highest_score = dict[i]
            highest_score_student = i
    return highest_score_student

dict = {"student1" : 100, "student2" : 79, "student3" : 80}
print(highest_score(dict))'''


# Write a program to rename a key in dictionary

'''def rename(dict,key,new_key):
    dict[new_key] = dict[key]
    del dict[key]
    return dict

dictionary = {"1": "a", "2": "b"}
print(rename(dictionary,"1","c"))'''


# Extract unique values in a given Dictionary
# D1 = {'list1' : [4,7,10,20] ,'list2' : [7,16,9,10] ,'list3' : [13,10,4,8] ,'list4' : [7,20,6,11]}

'''def unique_val(dict):
    val = set()
    for name, value in dict.items():
        for i in value:
            if i not in val:
                val.add(i)
    return list(val)

D1 = {'list1' : [4,7,10,20] ,'list2' : [7,16,9,10] ,'list3' : [13,10,4,8] ,'list4' : [7,20,6,11]}
print(unique_val(D1))'''


# Write a function that takes a dictionary and returns a list of keys whose values are greater than 
# a given number.

'''def func1(dict, num):
    return [k for k, v in dict.items() if v > num]

dict = {"1": 102, "2": 115, "3": 20, "4": 95}
print(func1(dict, 14))'''




# Replace Dictionary values from other Dictionary
# Dict1={'a’:1,’b’:2,’c’:3} Dict2={'a’:10,’c’:20,’d’:30}

'''def replace(dict1,dict2):
    for key,value in dict1.items():
        if key in dict2:
            dict1[key]=dict2[key]
        else:
            dict1[key]=value
    return dict1

D1 = {'a':1,'b':2,'c':3}
D2 = {'a':10,'c':20,'d':30}
print(replace(D1,D2))'''


# Create a function that takes a dictionary and returns a new dictionary where the keys and values
# are swapped.

'''def swap(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

dict = {'a': 10, 'b': 2, 'c': 20}
print(swap(dict))'''


# Write a program that removes duplicate values from a dictionary, keeping only the first occurrence
# of each value.

'''def swap(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

def rm_duplicate(dict):
    new_dict = {}
    for k, v in dict.items():
        if v not in new_dict:
            new_dict[v] = k
    return swap(new_dict)

dict = {"key1": 10, "key2": 15, "key3": 10, "key4": 15}
print(rm_duplicate(dict))'''


# Design a function that takes a list of dictionaries,each containing "name" and "salary" keys,
# and returns the name of the employee with the highest salary.

'''def salary(Dict):
    highest_salary = Dict[0]
    for i in Dict:
        if i["salary"] > highest_salary["salary"]:
            highest_salary = i
    return highest_salary["name"]

employees = [
    {"name": "siya", "salary": 700000},
    {"name": "diya", "salary": 200000},
    {"name": "Priya", "salary": 300000}]

print(salary(employees))'''



# Create a function that takes a string as input and returns the most common character and its
# frequency using a dictionary.

'''def freq(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return freq_dict[0]

print(freq("hellostringtest"))'''



# Write a function that takes a dictionary and returns a new dictionary containing only the key-value
# pairs where the key is a palindrome.

'''def palindrome_dict(d):
    new_dict = {}
    for key, value in d.items():
        if key.lower() == key[::-1].lower():
            new_dict[key] = value
    return new_dict

d = {'simis' : 1 , 'kiyik' : 2 , 'hyper' : 3}
print(palindrome_dict(d))'''