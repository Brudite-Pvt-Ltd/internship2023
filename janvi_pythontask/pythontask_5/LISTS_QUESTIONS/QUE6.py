def intersection(list, list1):
    intersection_result = []
    for element in list:
        if element in list1 and element not in intersection_result:
            intersection_result.append(element)
    return intersection_result

# Example usage:
list = [91,34,3,2,1]
list1 = [3,43,5,1,8]
result =intersection(list, list1)
print("Intersection of the two lists:", result)