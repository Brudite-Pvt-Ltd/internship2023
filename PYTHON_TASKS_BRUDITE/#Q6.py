#Q6.Implement a function to check if an array is a palindrome (reads the same forwards and backwards).

string = input("Enter the string: ")
if(string==string[::-1]):
    print("It is a palindrome ")
else:
    print("NOT PALINDROME")
    
    #SAME GOES FOR ARRAYS JUST CHANGE THE DATATYPE BY TYPECAS