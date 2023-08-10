#6. Write a Python program to check if a number is a power of two using recursion.
def power(num):
    if num==0:
        return False
    while(num!=1):
        if(num%2!=0):
            return False
        num=num//2
    return True

num=[25, 32, 21, 64, 27]
for n in num:
    print(f"{n} is power of 2 :",power(n))