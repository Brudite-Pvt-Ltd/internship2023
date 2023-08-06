#Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
def login():
    max_attempts = 3
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    while max_attempts > 0:
        retype_password = input("Re-Type Password: ")
        if retype_password == password:
            print("Login successful!")
            break
        else:
            max_attempts -= 1
            if max_attempts > 0:
                print(f"Password mismatch! You have {max_attempts} more attempts.")
            else:
                print("Incorrect password. Maximum attempts reached.")
    
    if max_attempts == 0:
        print("Login failed. Maximum attempts reached.")

# Call the login function
login()
