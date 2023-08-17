num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1_factor=[num1*x for x in range(1,100)]
num2_factor=[num2*x for x in range(1,100)]

for val in num1_factor:
    if val in num2_factor:
        print(f"LCM of {num1} and {num2} is {val}")
        break
