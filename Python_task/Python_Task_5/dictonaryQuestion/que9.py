#9.Write a program for rearrange the sequence of elements based on length of character in value

dict1 = {'a':'first','b':'second','c':"third",'d':"fourth",'e':'five'}


l= list(dict1.values())
l.sort(key=len)
dict2 = dict()
for x in l :
    
    for key,y in dict1.items():
        if dict1[key] == x:
            dict2[key] =x

print(dict2)