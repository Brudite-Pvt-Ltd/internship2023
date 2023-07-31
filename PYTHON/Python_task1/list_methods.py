r=['dog','cat','70','75','80']
a=['kya','kuch','bhi','7']
print(r)
r.append(1) #adds the value at the end of the list
print(r)
r.clear()  #removes all the items from the list
print(r)
r.insert(3,'7')  #inserts value at a given position
print(r)
r.extend(a)     #adds two list
print(r)
a.extend(r)
print(a)
a.reverse()       #reverse the list items
print(a)