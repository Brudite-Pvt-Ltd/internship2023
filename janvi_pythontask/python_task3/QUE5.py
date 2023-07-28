#how to sort it coloumn wise.
[3, 2, 5],
[1, 4, 6],
[9, 8, 7]
import numpy as np
matrix = np.array(
[[3, 2, 5],
[1, 4, 6],
[9, 8, 7]]) 
sorted_matrix = np.sort(matrix, axis=0)[::-1]

print(sorted_matrix )

