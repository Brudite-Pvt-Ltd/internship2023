'''def odd_num_sum(list):
    odd_sum = 0
    for i in list:
        if i % 2!= 0:
            odd_sum += i
    return odd_sum

l = [1,2,3,4,5,6,7,8,9,10]
print(odd_num_sum(l))'''

# write a program to find a factorial of  a number

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# print(factorial(999))

def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

# Example usage:
num1 = 12
num2 = 18
result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result}")
