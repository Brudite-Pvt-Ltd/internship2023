#4.Check if a list is a palindrome
list = [1,2,3,2,1]
if list==list[::-1]:
    print("list is palindrome")
else:
    print("list is not a palindrome")