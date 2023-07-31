#7.Write a program that removes duplicate values from a dictionary,keeping only the first occurrence of each value.
d1={'a':8,'b':9,'c':3,'d':8,'e':3}
set1=set()
remove_key=[]
for key,value in d1.items():
    if value in set1:
        remove_key.append(key)
    else:
        set1.add(value)
for x in remove_key:
    d1.pop(x)
print("unique dict:-",d1)