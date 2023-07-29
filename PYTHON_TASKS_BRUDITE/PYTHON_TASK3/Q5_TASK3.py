#Q5 Sort the column wise elements in a matrix [6,15,10] [14,9,12] [2,4,6]

[3, 2, 5],
[1, 4, 6],
[9, 8, 7]

import numpy as np

a = np.array(
[[3, 2, 5],
[1, 4, 6],
[9, 8, 7]]
) 

sorted_a = np.sort(a, axis=0)[::-1]

print(sorted_a)