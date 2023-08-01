s1 = {5, 10, 15, 20, 25}
ml = 0

for n in s1:
    if n - 1 not in s1:
        curr = n
        cl = 1

        while curr + 1 in s1:
            curr += 1
            cl += 1

        ml = max(ml, cl)

print("The length of the longest consecutive sequence is", ml)
