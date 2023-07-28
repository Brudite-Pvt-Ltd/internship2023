#Q6.Implement a function to check if an array is a palindrome (reads the same forwards and backwards).

def isPalindrome(a):
    return a == a[::-1]
 
a= [1,2,3,4,1]
output= isPalindrome(a)
 
if output:
    print("Yes")
else:
    print("No")