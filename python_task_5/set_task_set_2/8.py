# 8.Write a function to find the nth smallest element in a set.
set = {10, 5, 7, 3, 2, 8}
n = int(input("enter the number:")) #3rd smallest element
def smallest_element(set, n):
    sort_list = sorted(set)
    
    # Check if n is within the range of the list
    if 1 <= n <= len(sort_list):
        return sort_list[n - 1]
    else:
        return None

result = smallest_element(set, n)
print(f"The {n}th smallest element is:", result)