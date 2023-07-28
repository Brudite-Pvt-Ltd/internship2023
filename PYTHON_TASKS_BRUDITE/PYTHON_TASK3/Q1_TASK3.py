# Q1.WAP to count all unique values in the list.
      
      #METHOD 1
      
list = [1,2,3,4,3,6,2,5]
by_set = set(list)
a = len(by_set)
print("Number of unique values are:",a)
     
     #METHOD 2
    
list = [1, 2, 2, 5, 8, 4, 4, 8]
l1 = []
count = 0

for item in list:
    if item not in l1:
        count += 1
        l1.append(item)

print("No of unique items are:", count)

    #METHOD 3

import numpy as np

list = [1,2,3,4,3,6,2,5]
unique_val = np.unique(list)
a = len(unique_val)
print("No od unique values are:",a)
