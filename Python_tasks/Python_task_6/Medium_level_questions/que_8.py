# program 8 :
    
string = "Hello, World!"

string = string.lower()

cnt = 0
for x in string:
    if x == 'a' or x=='e' or x=='i' or x=='o' or x=='u':
        cnt += 1
        
print(cnt)