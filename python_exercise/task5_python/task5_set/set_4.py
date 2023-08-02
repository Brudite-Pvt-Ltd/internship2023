# Remove the maximum element from a set without using the max() function
set = {1,2,3,4,7,5,9,4}
set1 = sorted(set)
print(set1)
maximum_element= set1[-1]
set1.remove(maximum_element)
print(set1)