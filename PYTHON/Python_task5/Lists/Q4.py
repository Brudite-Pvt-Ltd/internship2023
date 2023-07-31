# Find the median of a list without using the built-in median function.

def median(list):
    if len(list) == 0:
        return None
    list.sort()
    if len(list) % 2 == 0:
        return (list[len(list) // 2 - 1] + list[len(list) // 2]) / 2
    else:
        return list[len(list) // 2]
    
list = [4, 5, 3, 9, 10, 17]
print(median(list))