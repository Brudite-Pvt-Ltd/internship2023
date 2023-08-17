# Write a Python function that counts the number of vowels in a given string.
# Sample Input: string = "Hello, World!"
# Sample Output: Number of vowels: 3
def vow(string , vowles):
    final =  [i for i in string if i in vowles ]
    
    print(len(final))
    print(final)
    
string =  "Hello , World!"
vowles = "AaEeIiOoUu"
vow(string , vowles);