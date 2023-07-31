def is_prime(num):
    if num<2:
          return False
    
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        return True


set1={1,2,3,4,5,6,7,8,9,10}
pairs=set()
for num1 in set1:
        for num2 in set1:
            if num1 != num2 and is_prime(num1 + num2):
                pairs.add((num1, num2))
print("pairs of elements whoes sum is prime number",pairs)

