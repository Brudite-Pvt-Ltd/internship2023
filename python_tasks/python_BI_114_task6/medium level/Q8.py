def vowels(str):
    count=0
    str=str.lower()
    for i in str:
        if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
            count+=1
    return count
string = "Hello, World!"
print(vowels(string))