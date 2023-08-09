user=input("enter the username")
pas=input("enter the password")
for i in range(3):
    str1=input("please re-enter the password")  
    if pas==str1:
        print("password is correct")  
        break
    if i<2:
        print("password is incorrect")
    else:
        print("abb bhut hua")
        
  

        
    