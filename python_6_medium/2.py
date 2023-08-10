#Create a function that takes a list and returns a new list with unique elements of the first list.
# Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
# Sample Output: list2 = [1, 2, 3, 4, 5]


def unique_ele(list1):
    unique = list(set(list1))
    return unique
list1 = [1,2,2,3,4,4,5,5]
unique_elements_list = unique_ele(list1)
print(unique_elements_list)



