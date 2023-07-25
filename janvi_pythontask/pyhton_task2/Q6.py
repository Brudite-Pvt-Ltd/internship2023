#6. Implement a function to check if an array is a palindrome (reads the same forwards and backwards)
string=input("Enter string:")
if(string==string[::-1]):
   print("The string is a palindrome")
else:
   print("The string isn't a palindrome")