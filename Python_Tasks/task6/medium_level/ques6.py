def power(x,y,z):
    if x > y:
        return False
    elif x==y:
        return True
    else:
        x=x*z
        return power(x,y,z)


n=int(input("enter numbner to be checked : "))
i=int(input("enter the power to be checked : "))
print(power(1,n,i))