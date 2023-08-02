# Q6. Create a list of all prime numbers upto a given number.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    list_of_prime = []
    for i in range(2, n):
        if is_prime(i):
            list_of_prime.append(i)
    return list_of_prime        

n = 20
print(prime_list(n))