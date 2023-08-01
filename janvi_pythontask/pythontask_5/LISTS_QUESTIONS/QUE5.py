#5.Implement a custom sorting function for a list of tuples based on the second element of each tuple.
def sort_by_second_element(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

# Example usage:
list_of_tuples = [(19,4), (6,39), (25,3), (14,2)]
sorted_list = sort_by_second_element(list_of_tuples)
print("Sorted list based on the second element:", sorted_list)