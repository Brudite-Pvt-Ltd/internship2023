#Check if a list is palindrome
list = [1,2,2,1]
if list == list[::-1] :
    print("List is palindrome")
else :
    print("List is not palindrome")