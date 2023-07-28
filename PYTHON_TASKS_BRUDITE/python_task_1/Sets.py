# SET OPERATIONS

#FOR PRINTING A SET
myset={"hello", "Hi","Hola","hello"}
print(myset) #it will print hello once because duplicates are not allowed in sets

#For accessing a set
myset={"banana", "apple", "cherry"}
for x in myset:
    print(x)
myset={"apple","banana","chery"}
print("cherry" in myset) # TRUE or FALSE

#FOR ADDIDNG ITEMS IN A SET
myset={"red","blue","green"}
print(myset)
myset.add("orange")
print(myset) #It can add orange anywhere because set in unordered

#FOR REMOVING ANY ITEM IN A SET
myset={"red","green","yellow"}
print(myset)
myset.remove("red")
print(myset)

#FOR JOINING TWO OR MORE SETS
s1={"a","b","c"}
s2={1,2,3}
s3=s1.union(s2)
print(s3)

#FOR INTERSECTION(DUPLICATES)
s1={"red","green","blue"}
s2={"hello","red","world"}
s1.intersection_update(s2)
print(s1)
z = s1.intersection(s2)
print(z)

#TO REMOVE ALL ELEMENTS FROM A SET
s1={"microsoft","google","amazon"}
print(s1)
s1.clear()
print(s1)