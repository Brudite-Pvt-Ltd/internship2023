f=open("doc.txt","r")
data=f.read()
new_string=[]
for i in data.split():
    if len(i)%2==0:
        new_string.append(i)
print(new_string)
f.close()