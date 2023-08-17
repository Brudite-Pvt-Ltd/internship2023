num=int(input("Enter your number:  "))
a=num
reverse_num=0
while num>0:
    digit = num % 10
    reverse_num = reverse_num*10 + digit
    num //= 10
print(f'Reverse of the number {a} is {reverse_num}')