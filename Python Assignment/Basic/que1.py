num = int(input("Enter your number:  "))

if(num%5 == 0 & num%3 == 0):
    print("Brudite - Python Training")
elif(num%5 == 0):
    print("Python Training")
elif(num%3 == 0):
    print("Brudite")
else:
    print("Number is neither divisible by 5 nor 3")