user_string=str(input("Enter your string:  "))
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count=0
for letter in user_string:
    if letter in vowels:
        vowel_count+=1
print(f'Total vowels in provied string is {vowel_count}')