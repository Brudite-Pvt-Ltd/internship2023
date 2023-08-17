start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))
Sum=0
for num in range(start, end+1):
    if(num%2!=0):
        Sum+=num
print(f'Sum of all odd numbers between {start} and {end} is {Sum}')