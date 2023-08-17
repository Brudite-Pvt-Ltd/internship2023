password="mypassword"
username="root"
print(f"Username is '{username}'")
print(f"Password is '{password}'")
print("System checks only for password.")

u_name=str(input("Enter your username:  "))
u_password=str(input("Enter your password: "))
i=3
if(u_password==password and u_name==username):
    print("Access granted")
else:
    while u_password!=password:
        if(i==0):
            print("Access denied")
            break
        print(f'{i} chances left')
        u_password=str(input("Enter your password: "))
        i=i-1
    if(u_password==password):
        print("Access granted")

        