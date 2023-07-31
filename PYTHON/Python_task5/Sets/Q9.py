# Create a set with 1000 elements and measure the time taken to search for a specific element.
# Compare it with a list containing the same elements.

import time

def find_time(set, element):
    start_time = time.time()
    if element in set:
        end_time = time.time()
        return end_time - start_time
    else:
        return 0

s = set(range(1000))
l = list(range(1000))
element = 207
search_time_set = find_time(s, element)
search_time_list = find_time(l, element)
print(search_time_set)
print(search_time_list)