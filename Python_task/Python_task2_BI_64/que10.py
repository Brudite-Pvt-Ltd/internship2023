#10.Given an array of integers, find the longest increasing subarray (consecutive elements in increasing order).
def lis(list):
    n = len(list)
    if n == 0:
        return []

    max_length = 1
    current_length = 1
    end_index = 0

    for i in range(1, n):
        if list[i] > list[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                end_index = i - 1
            current_length = 1
    if current_length > max_length:
        max_length = current_length
        end_index = n - 1

    start_index = end_index - max_length + 1
    return list[start_index:end_index + 1]
list= [1, 2, 3, 1, 2, 3, 4, 5, 6]

result = lis(list)

print("The longest increasing subarray is:", result)
