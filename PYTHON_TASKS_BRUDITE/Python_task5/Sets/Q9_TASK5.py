# Create a set with 1000 elements and measure the time taken to search for a specific element.
# Compare it with a list containing the same elements.

import time

s1=set(range(1000))
l1=list(range(1000))
element= 547

start_time = time.time()
print(element  in s1)
end_time = time.time()
set_search_time = end_time - start_time


start_time = time.time()
print(element  in l1)
end_time = time.time()
list_search_time = end_time - start_time

print(f"Set search time: {set_search_time:.6f} seconds")
print(f"List search time: {list_search_time:.6f} seconds")