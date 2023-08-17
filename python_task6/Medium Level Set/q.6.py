#Write a Python program to check if a number is a power of two using recursion.
# Python program to check if given
# number is power of 2 or not
def pow(n):
    if(n == 0):
        return False
    while (n != 1):
        if(n % 2 != 0):
            return False
        n = n//2
    return True

if(pow(94)):
    print("yes")
else:
    print("no")
        
            