# program 12 :
    
    
# existing users in database.
# stored as dictionary
 
# username(key) : password(value)   
list_of_users = {
        "user1001" : "password",
        "TestUser11" : "password_Test",
        "NewUser_01" : "new_password"
    }

cnt = 3 
b = 1
while(cnt):
    username = input("Enter the user name : ")
    if username not in list_of_users:
        print("user not found!")
    else :
        password = input("Enter the password : ")
        re_type = input("Re-Type the password : ")
        
        if re_type != password :
            print("Passwords are not same!")
        else :
            if list_of_users[username] == password :
                print("Login successful!")
                b = 0;
                break;
            else :
                print("username and password does not match!")
    
    cnt -= 1 
    
        
    
if(b):
    print("\n *** Try again Later ! ***")

