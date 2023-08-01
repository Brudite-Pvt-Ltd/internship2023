#3.Find the sum of all numeric elements in a list
def sum_of_numeric_elements(lst):
    total_sum = 0

    for item in lst:
        if isinstance(item, (int, float)):
            total_sum += item

    return total_sum


# Example usage:
my_list = [10, 12, 13,  4.5, 5.5]

result = sum_of_numeric_elements(my_list)
print(result) 