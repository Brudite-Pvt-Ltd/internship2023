import time
set1=set(range(1000))
list1=list(range(1000))
element=450

start_time = time.time()
print(element  in set1)
end_time = time.time()
set_search_time = end_time - start_time


start_time = time.time()
print(element  in list1)
end_time = time.time()
list_search_time = end_time - start_time

print(f"Set search time: {set_search_time:.6f} seconds")
print(f"List search time: {list_search_time:.6f} seconds")