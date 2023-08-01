
from collections import OrderedDict
d1 = {1: 'ababa', 2: 'bb', 3: 'india', 4: 'a', 5: 'csc'}
l = sorted(d1.items(), key=lambda x: len(x[1]))
d2=OrderedDict(l)
for i,j in d2.items():
    print(i,"",j)
    
    
