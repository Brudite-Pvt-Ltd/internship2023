#3.Find the sum of all numeric elements in a list

l =[1,3,5,7,8,9,23,56,"45","E"]

#Method1
s =0
for x in l:
    if isinstance(x,int):
        s += x
print(s)

#method 2
print(sum(map(lambda x:x if isinstance(x,int) else 0,l)))
