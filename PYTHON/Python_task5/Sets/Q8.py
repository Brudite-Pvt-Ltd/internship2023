# Write a function to find the nth smallest element in a set.

def smallest_ele(set_1, n):
    res = sorted(set_1)
    return res[n-1]

set1 = {9,3,5,1}
n = int(input("Enter the Nth position : "))
result = smallest_ele(set1, n)
print(result)

    
