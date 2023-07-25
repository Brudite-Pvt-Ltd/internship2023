#6.Implement a function to check if an array is a palindrome (reads the same forwards and backwards).

def isPalindrome(ank):
    return ank == ank[::-1]
 
ank = "45454"
output= isPalindrome(ank)
 
if output:
    print("Yes")
else:
    print("No")