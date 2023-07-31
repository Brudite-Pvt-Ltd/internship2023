#4. Write a program, which return the key for a given value


def get_key(value):
    l =[]
    for x,y in dict1.items():
        if y == value:
            l.append(x)    
    return l

dict1 ={'a':4,'b':8,'d':4,'t':6,'n':6,'q':1,'o':10}
value=6
ans =[x for x in dict1 if dict1[x]==value]
print(ans)

print(get_key(value))

print(list(dict1.keys())[list(dict1.values()).index(value)])
