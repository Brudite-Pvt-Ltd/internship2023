# Create a set of numbers, find all pairs of elements whose sum is a prime number

def prime_no(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_pairs(numbers_set):
    prime_pairs = []
    elements_list = list(numbers_set)
    n = len(elements_list)

    for i in range(n):
        for j in range(i + 1, n):
            num_sum = elements_list[i] + elements_list[j]
            if prime_no(num_sum):
                prime_pairs.append((elements_list[i], elements_list[j]))

    return prime_pairs

numbers_set = {1,2,3,4,5}
prime_sum_pairs = sum_pairs(numbers_set)
print("Pairs of elements whose sum is a prime number:")
for pair in prime_sum_pairs:
    print(pair)