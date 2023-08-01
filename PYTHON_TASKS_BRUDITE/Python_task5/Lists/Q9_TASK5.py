# Q9. Implement a function that takes a list of tuples, where each tuple
# contains a name and age,and returns the names of the three oldest people.

def reqdfunc(list):
    list.sort(key=lambda x: x[1], reverse=True)
    return list[:3]

data = [('Fizz', 18), ('Harry', 23), ('Ram', 19), ('bob', 25)]
print(reqdfunc(data))