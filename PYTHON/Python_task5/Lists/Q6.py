# Create a list of all prime numbers up to a given number.

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

n = 100
print(prime_list(n))
           