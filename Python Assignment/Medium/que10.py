n=int(input("Enter the total numbers of stone piles:  "))

if(n%2==0):
    for i in range(1,n+1):
        print(f'Total stone in pile {i} is {n}')
        n += 2
else:
    for i in range(1,n+1):
        print(f'Total stone in pile {i} is {n}')
        n += 2