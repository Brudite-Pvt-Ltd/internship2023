from collections import defaultdict
l1 = ["one", "two", "three", "four", "five", "six"]
d1 = defaultdict(list)

for i in l1:
    d1[len(i)].append(i)

for i,j in d1.items():
    print(i ,"characters :", j)
