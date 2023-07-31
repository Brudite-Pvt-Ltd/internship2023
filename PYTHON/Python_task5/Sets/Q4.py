# Create a set of prime numbers between 1 and 50.

def prime_no(size):
    primes = set()
    for i in range(2, size):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.add(i)
    return primes


print(prime_no(50))