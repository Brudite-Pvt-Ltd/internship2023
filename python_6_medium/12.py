# 12. Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times

username = input("enmter username here:")
password = input("enter your password")
for i in range(5):
     str = input("please re enter your password")
     if(str==password):
          print("correct pasword!")
     if i>5:
          print("incorrect")
     else:
          print("try again")
