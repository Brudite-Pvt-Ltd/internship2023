string = str(input("Enter your string:  "))
alpha = num = 0
for char in string:
    if char.isdigit() == True:
        alpha += 1
    elif char.isalpha() == True:
        num += 1
print(f'num = {num}, alpha = {alpha}')