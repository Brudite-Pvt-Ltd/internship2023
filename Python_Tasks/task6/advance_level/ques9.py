
    
x =input("enter the string to be encoded : ")
s = ''

i = 0
while i < len(x):
    char = x[i]
    count = 1

    j = i + 1
    while j < len(x) and x[j] == char:
        count += 1
        j += 1

    s += char + str(count)
    i = j

print(s)

        
   
    