

List = [1, 2, 2, 1, 3, 4, 6, 8, 9, 0]

""" 
    method 1  - using set   
"""

print( "Count =", len(set(List)))


"""
     method 2  - using Counter
"""

from collections import Counter

print("Count =" ,len(Counter(List)))

"""
     method 3  - using loops
"""

newList = []
for x in List :
    if x not in newList :
        newList.append(x)

print("count =", len(newList))


"""
     method 4  - using numpy
"""

import numpy as np

print("count =", len(np.unique(List)))

"""
     method 5 - list compr.
"""

print( "Count =", len({i for i in List}))