#creating a set
set = {"hii","hello","namaste"}
print(set)
#Access Items
set = {"hii","hello","namaste"}
for x in set:
    print(x)
#add items
set = {"hii","hello","namaste"}
set.add("ram-ram")
print(set)
#update
set = {"hii","hello","namaste"}
set2 = ("hola","tata","bye")
set.update(set2)
print(set)
#remove items
set = {"hii","hello","namaste"}
set.remove("hii")
print(set)
#discarditems
set = {"hii","hello","namaste"}
set.discard("hii")
print(set)
#Join Two Sets
set = {"hii","hello","namaste"}
set2 = ("hola","tata","bye")
set3 = set.union(set2)
print(set3)
#Keep All, But NOT the Duplicates
set = {"hii","hello","bye"}
set2 = ("hii","tata","bye")
set.symmetric_difference_update(set2)
print(set)