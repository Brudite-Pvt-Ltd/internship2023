# 8. Write a Python function that counts the number of vowels in a given string.
# Sample Input: string = "Hello, World!"
# Sample Output: Number of vowels: 3

def vowels(string):
    str = string.lower()
    count = 0
    for i in str:
        if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count +=1
    return count
string = "Hello, World!"
print(vowels(string))

    