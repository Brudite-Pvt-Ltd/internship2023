# program 7 :
    
def checkPower(num, target):
    if(num > target):
        return "NO" ;
    
    elif(num == target):
        return "YES";
    
    else:
        num *= 2
        ans = checkPower(num, target)
        return ans


n = int(input("Enter the number : "))
print(checkPower(1, n))
