# Create a list of all prime numbers up to a given number.

def is_prime(n):
    prime_list = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    return prime_list

n = 100
print(is_prime(n))
