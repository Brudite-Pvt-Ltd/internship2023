# Q4.Create a set of prime numbers between 1 and 50.

set=set()
for num in range(1, 51):
 if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           set.add(num)

print("set of prime number",set)