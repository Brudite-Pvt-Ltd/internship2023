user_str=str(input("Enter your string:  "))
character = str(input("Enter character to test: "))

result = lambda x,y: True if x[0]==y else False
print(result(user_str, character))