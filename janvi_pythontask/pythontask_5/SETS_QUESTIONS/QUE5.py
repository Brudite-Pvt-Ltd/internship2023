
#.Create a set of all possible sub sets from a given set

import itertools

s = {17, 21, 3, 4}
k = 2
subsets_of_set = list(itertools.combinations(s, k))

print(subsets_of_set)