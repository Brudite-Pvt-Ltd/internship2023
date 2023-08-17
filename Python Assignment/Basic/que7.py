user_str=str(input("Enter your string: "))
rev_str=user_str[::-1]
if(user_str != rev_str):
    print(f"'{user_str}' is an Anagram string.")
else:
    print(f"'{user_str}' is not an Anagram string.")
