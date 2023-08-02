# Q6.Remove the duplicate tuples from the list of tuple.
l = [ (1, 2, 3), (1, 2, 3), (1, 3, 2), (1, 2, 4)]

# if (1, 2) and (2, 1) are diffreent 

print(list(set(l)))

new_l = []
have = []

for x in l :
    tup = sorted(list(x));
    if tup not in have :
        new_l.append(x)  ;
        have.append(tup) ;
        
print(new_l)