#3.Create a set {1,2,3}, make it immutable.

set1 = {1,2,3}

#set is a mutable but frozenset is a constructor that is a set which has a property of immutable
set2 = frozenset(set1)

#set2.add(34)
set1.add(23)
#set2 is a frozenset so by after adding element in it it gives an error 
print(set2)