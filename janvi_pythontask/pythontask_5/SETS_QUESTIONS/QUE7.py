#7. Write a function to perform set division(A/B)where A and B are sets,and the result is a set of tuples(a,b)for each a inAandbinB,where a is divisible by
'''def set_division(A, B) :
    result = set()
for a in A:
   for b in B:
       if a % b==0:
            result.add((a,b))
'''

''#print("Set Division (A/B):", result_set) ''


def set_division(A, B):
    result = set()
    for a in A:
        for b in B:
            if a % b == 0:
                result.add((a, b))
    return result

# Example sets
A = {14, 15, 40, 95}
B = {25, 57}


# Perform set division
result_set = set_division(A, B)

print("Set Division (A/B):", result_set)