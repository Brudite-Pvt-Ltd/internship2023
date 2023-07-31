#2.Create a new list with unique elements from an existing list.

#method1 
l1 = list(set(l))
print(l1)

#method2 
l2 = list(dict.fromkeys(l))
print(l2)

#method3 brute force
l3 =[]
[l3.append(x) for x in l if x not in l3]
print(l3)

#method4 
import numpy as np
l4 =[]
l4 = np.unique(l)
print(l4)

#method 5 using counter
from collections import Counter
l5 = []
l5 = list(Counter(l))
print(l5)
