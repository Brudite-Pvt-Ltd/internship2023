#Q8. Write a function to find the nth smallest element in a set.
def smallest_element(set1, n):
    a = sorted(set1)
    return a[n-1]

s1 = {9,3,5,1}
n = int(input("Enter the Nth position : "))
result = smallest_element(s1, n)
print(result)