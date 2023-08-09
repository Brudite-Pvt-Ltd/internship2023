input_string = "Hello, World!"
given_char = "h"

result= (lambda x:x[0]==given_char,input_string)
print(result[0](result[1]))