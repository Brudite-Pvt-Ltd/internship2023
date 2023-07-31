#6.Create a list of Dictionary, each containing “name“ and “age” Keys, sort the list based on the ages of the people in ascending order

l =[{'name':'vipul','age':22},{'name':'vaibhav','age':23},{'name':'pankaj','age':21},{'name':'vishal','age':20},{'name':'akshat','age':18}]
#method1
t= sorted(l, key=lambda x: x["age"])
print(t)
#method2

for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]['age']>l[j]['age']:
            l[i],l[j]= l[j],l[i]

print(l)

