# Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is
# incorrect give chance to enter it again but it should not be more than 3 times.

print('Enter correct username and password ')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='26082002@' and username=='simran_kaur':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1