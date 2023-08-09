# -*- coding: utf-8 -*-
"""
que 12
Create a login page backend to ask users to enter the username and password.
Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
 
"""
username = input("Username: ")
password = input("Password: ")
confirm_password = input("Confirm_password: ")
for i in range(2):
    if confirm_password!=password:
        confirm_password = input("Re-Enter Confirm_password: ")
        if i ==1:
            print("Unauthorized access")
            break
    else:
        print("Successfull login")
        break