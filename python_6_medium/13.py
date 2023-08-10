# 13. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample input: input_string = "Hello, World!", given_char = "H"
# Sample Output: True
input_string = "Hello, World!"
given = "h"

result= (lambda x:x[0]==given,input_string)
print(result[0](result[1]))