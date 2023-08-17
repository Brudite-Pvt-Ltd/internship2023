# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.

# Sample Input: n = 7
# Sample Output: Stones in a single pile = [2, 4, 6]
def test(n):    
    return [n + 2 * i for i in range(n)]   
n = 7
print("Number of piles:",n)
print("Number of stones in each pile:")
print(test(n)) 