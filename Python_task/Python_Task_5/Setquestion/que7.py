#7.Write a function to perform set division (A/B) where A and B are sets, and the result is a set of tuples(a,b) for each a in A and bin 
#B, where a is divisible by b

A = {9,7,10,3,9,5,14,17,21}
B = {5,9,3,2,7}
ans =set()
for a in A:
    for b in B:
        if a%b == 0:
            ans.add((a,b))
print(ans) 