





user=input("enter username : ")
pswd=input("enter password : ")
rpswd=input("re enter the password : ")
b=0
n=3
if pswd!=rpswd:
    for i in range(0,n):
        rpswd1=input("re entered password is wrong, renter the password again : ")
        
       
        if rpswd1 == pswd:
            
            b=1
            break
        else:
            print("re-entered password is wrong chance left : ", n-i-1)
else:
    b=1
if(b==1):
    print("\n *** login succefull *** \n")
else: 
    print("\n *** invalid credentials***\n")        