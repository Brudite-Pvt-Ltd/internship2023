num = int(input("Enter your number:  "))

def pow_checker(num, i):
    if 2**i == num:
        return True
    else:
        if i > num:
            return False
        else:
            return pow_checker(num, i+1)

a = pow_checker(num, 1)
if(a==True):
    print("yes")
else:
    print("no")